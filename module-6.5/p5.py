numbers = [1, 2, 3, 4, 5, 6]
ev_sq = list(map(lambda x : x * x, filter(lambda i : i % 2 == 0, numbers)))
print(ev_sq)