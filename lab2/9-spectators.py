def get_unlucky_spectators(matrix):

    position_tuples = []

    matrix_transpose = list(zip(*matrix))

    for c in range(len(matrix_transpose)):
        for l in range(1, len(matrix_transpose[0])):
            if matrix_transpose[c][l] <= max(matrix_transpose[c][:l]):
                position_tuples.append(tuple((l, c)))
    return position_tuples


def main():
    spectators_heights = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]
    result = get_unlucky_spectators(get_unlucky_spectators(spectators_heights))
    print(result)


if __name__ == "__main__":
    main()
