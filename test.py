import main
import time

def basic_test():
    print("starting basic test")
    
    main.init()
    time.sleep(1)
    
    # test power on
    print("\ntest 1: power on sequence")
    if main.power_on():
        print("pass")
    else:
        print("fail")
        return
    
    time.sleep(1)
    
    # test voltage reading
    print("\ntest 2: voltage readings")
    v5 = main.read_5v()
    v3 = main.read_3v3()
    print(f"5v: {v5:.2f}")
    print(f"3.3v: {v3:.2f}")
    
    if v5 > 4.5 and v3 > 3.0:
        print("pass")
    else:
        print("fail")
    
    time.sleep(1)
    
    # test monitoring
    print("\ntest 3: monitoring for 5 seconds")
    for i in range(10):
        if not main.check_voltages():
            print("fail - voltage fault detected")
            return
        time.sleep(0.5)
    print("pass")
    
    # test power off
    print("\ntest 4: power off sequence")
    main.power_off()
    time.sleep(0.5)
    
    if main.ctrl_5v.value() == 1 and main.ctrl_3v3.value() == 1:
        print("pass")
    else:
        print("fail")
    
    print("\nall tests complete")

if __name__ == "__main__":
    basic_test()
