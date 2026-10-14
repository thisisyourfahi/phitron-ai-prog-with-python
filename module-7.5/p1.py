def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

create_file('notes.txt', 'Hello, this is my first file.\nI am currently learning python file-handling.\n')