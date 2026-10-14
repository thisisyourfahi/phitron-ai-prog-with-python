def add_log(message):
    with open('log.txt', 'a+') as file:
        file.write(f'{message}\n')
        print('[Success] Log added.') 

add_log('user logged in.')
add_log('file uploaded.')
add_log('user logged out.')