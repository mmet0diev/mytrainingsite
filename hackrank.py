from cmath import *

# def print_formatted(number):
#     # your code goes here
#     # Decimal
#     # Octal
#     # Hexadecimal(capitalized)
#     # Binary
#     output = ""
#     for i in range(1, number + 1):
#         width = len(str(bin(number))[2:])
#         output += str(i).rjust(width) + " "
#         output += str(oct(i))[2:].rjust(width) + " "
#         output += str(hex(i))[2:].upper().rjust(width) + " "
#         output += str(bin(i))[2:].rjust(width)
#         if i < number:
#             output += "\n"

#     print(output)


# print("--------e--------\n"
#           "------e-d-e------\n"
#           "----e-d-c-d-e----\n"
#           "--e-d-c-b-c-d-e--\n"
#           "e-d-c-b-a-b-c-d-e\n"
#           "--e-d-c-b-c-d-e--\n"
#           "----e-d-c-d-e----\n"
#           "------e-d-e------\n"
#           "--------e--------\n")

# def print_rangoli(size):
#     # your code goes here
#     a = chr(97)
#     rangoli = ""
#     letters = []

#     # add letters to list
#     for i in range(97, 97 + size):
#         letters.append(chr(i))

#     letters1 = []
#     for i in range(97 + size - 1, 96, -1):
#         letters1.append(chr(i))

#     lets = ""
#     for l in letters:
#         for i in range(len(letters1)):
#             lets+=letters1[i]

#         rangoli+=lets


#     print(letters)
#     print(letters1)
#     print(rangoli)


# print_rangoli(3)

# Problem/Solution - Polar Coordinates
n = input()

complex_n = complex(n)

print(abs(complex_n))
print(phase(complex_n))