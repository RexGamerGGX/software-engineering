import os

def clear_console():
    # Check the operating system and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For Linux and macOS
        