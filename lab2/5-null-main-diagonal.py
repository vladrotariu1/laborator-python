def null_on_main_diagonal(matrix):
    new_matrix = []

    number_rows = len(matrix)
    number_columns = len(matrix[0])

    for row_index in range(number_rows):
        new_row = []

        for column_index in range(number_columns):
            if row_index == column_index:
                new_row.append(0)
            else:
                new_row.append(matrix[row_index][column_index])

        new_matrix.append(new_row)

    return new_matrix


def main():
    input_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    result = null_on_main_diagonal(input_matrix)
    print(result)


if __name__ == "__main__":
    main()
