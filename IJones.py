def read_file(file_to_read):

    with open(file_to_read, "r") as plate_file:
        plate_params = list(plate_file.readline().split(" "))
        plate_width = int(plate_params[0])
        plate_height = int(plate_params[1])
        plate = []

        for line in plate_file:
            plate.append(line)

    return plate_height, plate_width, plate

def ijones(height, width, plate):
    result_path = [[0 for _ in range(width)] for _ in range(height)]
    paths_to_letter = {}

    for row in range(height):
        current_letter = plate[row][0]
        result_path[row][0] = 1
        paths_to_letter[current_letter] = paths_to_letter.setdefault(current_letter, 0) + 1

    for column in range(1, width):
        new_paths_to_letter = {}
        for row in range(height):
            current_letter = plate[row][column]
            result_path[row][column] = paths_to_letter.get(current_letter, 0)
            if plate[row][column-1] != current_letter:
                result_path[row][column] += result_path[row][column-1]
            new_paths_to_letter[current_letter] = new_paths_to_letter.setdefault(current_letter, 0) + result_path[row][column]
        for letter in new_paths_to_letter:
            paths_to_letter[letter] = paths_to_letter.setdefault(letter, 0) + new_paths_to_letter[letter]

    if height == 1:
        return result_path[0][width-1]

    return result_path[0][width-1] + result_path[height-1][width-1]

def write_file(file_to_write, result):
    with open(file_to_write, "w") as result_file:
        result_file.write(str(result))
if __name__ == '__main__':
    a = read_file("in.txt")
    b = ijones(*a)
    print(b)
    write_file("out.txt", b)