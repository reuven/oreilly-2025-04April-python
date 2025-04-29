def menu(options):
    while True:
        choice = input(f'Choose one from {options}: ').strip()
    
        if choice in options:
            return choice
    
        print(f'{choice} is invalid; try again')
