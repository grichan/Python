import math
import numpy as np


k = 4
prty = 0
#k = input("How long should the data be??? ") # data bits#
H = ['1010101', '0110011', '0001111']

if k == 4:
    prty = 3
    check_array = [5] * 7 
    check_pos = [0] * 4
    print("4 bits of data")
elif k == 11:
    check_array = [5] * 14
    prty = 4	
    print("11 bits of data")    

for i in range(0, k):
    pow2 = pow(2, i) - 1
    check_pos[i] = pow2 
    if pow2 < len(check_array):
        check_array[pow2] = 0

print(check_array)

for i in range(0, len(check_array)):
    if check_array[i] != 0:
        check_array[i] = input("Enter Bit data: ")

print(check_array)
print(check_pos)

for i in range(0, len(check_pos)):
    pos = check_pos[i]

    for j in range(pos, len(check_array)):
