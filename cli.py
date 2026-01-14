import main
import sys

def show_help():
    print("\ncommands:")
    print("  on    - power on")
    print("  off   - power off")
    print("  stat  - show status")
    print("  mon   - monitor mode")
    print("  quit  - exit\n")

def cli():
    main.init()
    show_help()
    
    while True:
        try:
            cmd = input("> ").strip().lower()
            
            if cmd == "on":
                main.power_on()
            elif cmd == "off":
                main.power_off()
            elif cmd == "stat":
                main.status()
            elif cmd == "mon":
                print("monitoring... ctrl+c to stop")
                try:
                    main.monitor_loop()
                except KeyboardInterrupt:
                    print("\nmonitoring stopped")
            elif cmd == "quit":
                main.power_off()
                print("bye")
                break
            elif cmd == "help":
                show_help()
            else:
                print("unknown command")
                
        except KeyboardInterrupt:
            print("\nuse 'quit' to exit")
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    cli()
