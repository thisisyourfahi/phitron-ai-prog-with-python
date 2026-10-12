def introduce(name, age):
    print(f'My name is {name} and I am {age} years old.')

inp = input('Only provide fist name and age.')
name, age = inp.split()
age = int(age)

introduce(name, age)