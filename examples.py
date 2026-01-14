import main
import time

# basic usage example

def example_startup():
    # initialize
    main.init()
    print("initialized")
    time.sleep(1)
    
    # power on sequence
    print("\nstarting power sequence...")
    success = main.power_on()
    
    if not success:
        print("startup failed")
        return
    
    # check status
    print("\nchecking status...")
    main.status()
    
    # run for a while
    print("\nrunning for 10 seconds...")
    for i in range(20):
        if not main.check_voltages():
            print("fault detected!")
            break
        time.sleep(0.5)
    
    # shutdown
    print("\nshutting down...")
    main.power_off()
    
    print("done")

def example_mission():
    # simulated mission profile
    main.init()
    
    print("t-10: pre-flight check")
    time.sleep(2)
    
    print("t-5: powering up avionics")
    main.power_on()
    time.sleep(1)
    
    print("t-0: launch")
    time.sleep(5)
    
    print("t+5: monitoring in flight")
    for i in range(30):
        main.check_voltages()
        time.sleep(0.5)
    
    print("t+20: landing sequence")
    time.sleep(2)
    
    print("t+22: powering down")
    main.power_off()
    
    print("mission complete")

if __name__ == "__main__":
    # run basic example
    example_startup()
    
    # uncomment for mission simulation
    # example_mission()
