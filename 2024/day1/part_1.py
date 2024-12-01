import os

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, 'input.txt')

with open(input_file_path, 'r') as file:
    data = file.read()

    list_1 = []
    list_2 = []

    for line in data.splitlines():
        parts = line.split()
        list_1.append(parts[0])
        list_2.append(parts[1])

    list_1.sort()
    list_2.sort()

    zipped_lists = list(zip(list_1, list_2))

    distances = [abs(int(x)-int(y)) for x, y in zipped_lists]

    print(sum(distances))