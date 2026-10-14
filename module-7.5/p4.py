def read_from_position(filename, position):
    try:
        with open(filename, 'r') as file:
            file.seek(position)
            print(file.read())
    except Exception as e:
        print(e)

read_from_position('notes.txt', 7)