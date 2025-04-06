from ohce import Ohce, RealClock

def main(name=None, clock=None):
    """
    Main function that handles the application interaction.
    
    Args:
        name (str, optional): User name, will be prompted if not provided
        clock: Clock object for time-based greetings, uses system time if not provided
    """
    if name is None:
        name = input("Please enter your name: ")
    
    ohce = Ohce(name, clock)
    
    # Show greeting
    print(ohce.greet())
    
    # Main loop
    while ohce.is_running():
        text = input("> ")
        result = ohce.process_input(text)
        print(result)

if __name__ == "__main__":
    main()