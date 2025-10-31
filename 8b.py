def squares():
    for i in range(5):
        yield i**2
square_generator=squares()
for square in square_generator:
    print(square)
