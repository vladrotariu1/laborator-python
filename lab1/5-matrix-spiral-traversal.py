def spiral_traversal(matrix):
    result = []

    if len(matrix) == 0:
        return result

    number_rows = len(matrix)
    number_columns = len(matrix[0])
    seen = [[0 for i in range(number_columns)] for j in range(number_rows)]
    direction_row = [0, 1, 0, -1]
    direction_column = [1, 0, -1, 0]
    direction_index = 0

    current_row_index = 0
    current_column_index = 0

    for i in range(number_rows * number_columns):
        result.append(matrix[current_row_index][current_column_index])
        seen[current_row_index][current_column_index] = True
        next_row_index = current_row_index + direction_row[direction_index]
        next_column_index = current_column_index + direction_column[direction_index]

        # Verificam daca urmatoarea pozitie din directia curenta este valida,
        # altfel vom schimba directia
        if 0 <= next_row_index < number_rows and 0 <= next_column_index < number_columns and not(seen[next_row_index][next_column_index]):
            current_row_index = next_row_index
            current_column_index = next_column_index
        else:
            direction_index = (direction_index + 1) % 4
            current_row_index += direction_row[direction_index]
            current_column_index += direction_column[direction_index]
    return result


input_matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print(spiral_traversal(input_matrix))
