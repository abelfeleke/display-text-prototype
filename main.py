import os
import random

if __name__ == '__main__':

    file_dict = {}
    directory = '/Users/abelfeleke/Desktop/display-text-prototype/texts'
    files = [f for f in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, f))
             and f.endswith('.txt')]

    for i, filename in enumerate(files):
        with open(os.path.join(directory, filename), 'r') as file:
            file_dict[i] = file.read()

    random_value = random.choice(list(file_dict.keys()))
    txt = file_dict[random_value]

    user_inputs = []
    while True:
        print('{} <->'.format(txt), user_inputs)
        user_input = input("Enter a phrase (or 'q' to quit): ")
        if user_input == 'q':
            break
        user_inputs.append(user_input)








