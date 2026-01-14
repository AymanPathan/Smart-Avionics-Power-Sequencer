import machine
import time

# pin setup
ctrl_5v = machine.Pin(7, machine.Pin.OUT)
ctrl_3v3 = machine.Pin(8, machine.Pin.OUT)
vsense_5v = machine.ADC(26)
vsense_3v3 = machine.ADC(27)

# voltage limits
v5_min = 4.75
v5_max = 5.25
v3_min = 3.2
v3_max = 3.45

rails_on = False

def init():
    global rails_on
    ctrl_5v.value(1)  # off
    ctrl_3v3.value(1)  # off
    rails_on = False
    print("power sequencer ready")

def read_5v():
    raw = vsense_5v.read_u16()
    voltage = (raw / 65535) * 3.3 * 2
    return voltage

def read_3v3():
    raw = vsense_3v3.read_u16()
    voltage = (raw / 65535) * 3.3 * 2
    return voltage

def power_on():
    global rails_on
    print("starting sequence")
    
    # enable 5v
    ctrl_5v.value(0)
    time.sleep(0.1)
    
    v5 = read_5v()
    print(f"5v: {v5:.2f}")
    
    if v5 < v5_min:
        print("5v failed")
        power_off()
        return False
    
    # enable 3.3v
    ctrl_3v3.value(0)
    time.sleep(0.1)
    
    v3 = read_3v3()
    print(f"3.3v: {v3:.2f}")
    
    if v3 < v3_min:
        print("3.3v failed")
        power_off()
        return False
    
    rails_on = True
    print("power on complete")
    return True

def power_off():
    global rails_on
    ctrl_3v3.value(1)
    time.sleep(0.05)
    ctrl_5v.value(1)
    rails_on = False
    print("power off")

def check_voltages():
    v5 = read_5v()
    v3 = read_3v3()
    
    fault = False
    
    if v5 < v5_min or v5 > v5_max:
        print(f"fault: 5v = {v5:.2f}")
        fault = True
    
    if v3 < v3_min or v3 > v3_max:
        print(f"fault: 3.3v = {v3:.2f}")
        fault = True
    
    if fault:
        power_off()
        return False
    
    return True

def status():
    print("\n--- status ---")
    print(f"5v rail: {'on' if ctrl_5v.value() == 0 else 'off'}")
    print(f"3.3v rail: {'on' if ctrl_3v3.value() == 0 else 'off'}")
    if rails_on:
        print(f"5v: {read_5v():.2f}")
        print(f"3.3v: {read_3v3():.2f}")
    print("--------------\n")

def monitor_loop():
    while True:
        if rails_on:
            if not check_voltages():
                print("shutdown due to fault")
        time.sleep(0.5)

# main
if __name__ == "__main__":
    init()
    
    # auto start for testing
    # power_on()
    # monitor_loop()
