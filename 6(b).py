def create_file_and_count_occurence():
    file_name = input('Enter the file name to create:')
    with open(file_name, 'w') as file:
        print('Enter the contents of file(press enter to finish):')
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')
    
    print('\n Contents of file:')
    with open(file_name, 'r') as file:
        print(file.read())
    
    letter = input('\n Enter the letter to count to occurences:')
    with open(file_name, 'r') as file:
        content = file.read()
        count = content.count(letter)
        print(f"The letter {letter} occurs {count} times in file")

create_file_and_count_occurence()
