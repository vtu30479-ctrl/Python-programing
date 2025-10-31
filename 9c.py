def openf(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print('File contents:')
            print(contents)
    except FileNotFoundError:
        print('Error: File not found')

filename = input('Enter a file name:')
openf(filename)
