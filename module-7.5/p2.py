def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = list(map(str.strip, lines))
            for i in range(len(lines)):
                print(f'{i + 1}: {lines[i]}')
    except Exception as e:
        print(e)

read_lines('notes.txt')