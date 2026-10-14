def safe_read(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print('Error: File not found.')
    else:
        print(file.read(), end='')
    finally:
        print('Operation complete.')

safe_read('log.txt')
safe_read('missing.txt')