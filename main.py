def process_numbers(start, end):
    squares = []
    for num in range(start, end + 1):
        squares.append(num ** 2)

    odd_squares = []
    even_squares = []
    for square in squares:
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)