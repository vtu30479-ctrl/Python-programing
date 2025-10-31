def create_file_and_count_words():

    file_name = input("Enter the file name to create: ")
    with open(file_name, 'w') as file:
        print("Enter the contents of the file (press Enter to finish):")
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')

    print("\nContents of the file:")
    with open(file_name, 'r') as file:
        print(file.read())

    with open(file_name, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        print(f"\nThe number of words in the file is: {word_count}")

create_file_and_count_words()
