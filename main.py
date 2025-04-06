from ohce import Ohce, RealClock
import sys

def main(name=None, clock=None):
    """
    Main function that handles the application interaction.
    
    Args:
        name (str, optional): User name, will be prompted if not provided
        clock: Clock object for time-based greetings, uses system time if not provided
    """
    try:
        if name is None:
            name = input("Please enter your name: ")
        
        ohce = Ohce(name, clock)
        
        # Show greeting
        print(ohce.greet())
        print(f"Type '{Ohce.STOP_COMMAND}' to exit.")
        
        # Main loop
        while ohce.is_running():
            text = input("> ")
            result = ohce.process_input(text)
            print(result)
            
    except KeyboardInterrupt:
        print(f"\nAdios {name}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())