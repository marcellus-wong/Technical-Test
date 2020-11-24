import numpy as np
import math

stored_pizzeria_possibilities=[]

user_input_beginning = []
print('Insert input variables (N and M). Press the "Enter" key to start a new line.')
print('Then input variables (X, Y and K) for each new pizzeria, creating a new line for each new pizzeria.')
print('Once you have finished entering all inputs, press the "Enter" key twice to get the output')

while True:
    line = input()
    if line:
        user_input_beginning.append(line)
    else:
        break
text = ' '.join(user_input_beginning)
lines_new = ' '.join(user_input_beginning)
user_input = lines_new.split()

print('\n')

def matrix_build():
    matrix_int = int(user_input[0])
    zero_matrix = np.zeros((matrix_int,matrix_int))


    number_of_pizz = int(user_input[1])


    for k in range(1, number_of_pizz + 1):

        if k==1:
            multiplication_factor = 0
        else:
            multiplication_factor = (k-1)*3


        x_coord = int(user_input[2+multiplication_factor])-1
        y_coord = int(user_input[3+multiplication_factor])-1
        distance = int(user_input[4+multiplication_factor])

        zero_matrix[x_coord, y_coord] = 1


        try:
            for x in range(distance+1):
                if x_coord + x > matrix_int:
                    pass
                else:
                    zero_matrix[x_coord+x, y_coord]=1
        except IndexError:
            pass


        try:
            for x in range(distance+1):
                if x_coord - x < 0:
                    pass
                else:
                    zero_matrix[x_coord-x, y_coord]=1
        except IndexError:
            pass


        try:
            for x in range(distance+1):
                if y_coord + x > matrix_int:
                    pass
                else:
                    zero_matrix[x_coord, y_coord+x]=1
        except IndexError:
            pass


        try:
            for x in range(distance+1):
                if y_coord - x < 0:
                    pass
                else:
                    zero_matrix[x_coord, y_coord-x]=1
        except IndexError:
            pass


        try:
            for x in range(distance):
                for y in range(distance):
                    if x_coord + x > matrix_int or y_coord + y > matrix_int or x + y > distance:
                        pass
                    else:
                        zero_matrix[x_coord + x, y_coord + y] = 1
        except IndexError:
            pass


        try:
            for x in range(distance):
                for y in range(distance):
                    if x_coord + x > matrix_int or y_coord - y < 0 or x + y > distance:
                        pass
                    else:
                        zero_matrix[x_coord + x, y_coord - y] = 1
        except IndexError:
            pass


        try:
            for x in range(distance):
                for y in range(distance):
                    if x_coord - x < 0 or y_coord + y > matrix_int or x + y > distance:
                        pass
                    else:
                        zero_matrix[x_coord - x, y_coord + y] = 1
        except IndexError:
            pass


        try:
            for x in range(distance):
                for y in range(distance):
                    if x_coord - x < 0 or y_coord - y < 0 or x + y > distance:
                        pass
                    else:
                        zero_matrix[x_coord - x, y_coord - y] = 1
        except IndexError:
            pass



        stored_pizzeria_possibilities.append(zero_matrix)
        split_matrix = np.array_split(stored_pizzeria_possibilities,number_of_pizz)
        zero_matrix = np.zeros((matrix_int,matrix_int))
    New = sum(split_matrix)
    Maximum_output = New.max()
    print('Maximum number is ', Maximum_output)


print(matrix_build())