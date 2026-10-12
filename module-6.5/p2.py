def batch_generator(lst, batch_size):
    for i in range(0, len(lst), batch_size):
        yield lst[i : i + batch_size]

data = [1, 2, 3, 4, 5, 6, 7, 8]
batch_size = 3
x = batch_generator(data, batch_size)
print(next(x))
print(next(x))
print(next(x))