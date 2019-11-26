import numpy as np
from collections import deque
plain_text = "0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111"


key = "1110 1110 1111 1111 1100 1100 1101 1101 1010 1010 1011 1011 1110 1111 1100 1011".replace(" ","")
def join_name(table,strs , breaks = 4, conviction = 1):
    strs = strs.replace(" ","")
    res =""
    for index, key in enumerate(table,start=1):
        res += strs[key - conviction]
        if index % breaks == 0: res += " "
    return res

def insert_space(strs , breaks =4):
    new_res =""
    for i in range(0,len(strs),breaks):
        new_res += strs[i:i+breaks]
        if i % (breaks ) == 0: new_res += " "
    return new_res


def shiftLbyn(arr, n=0):
    return arr[n::] + arr[:n:]

def shiftRbyn(arr, n=0):
    return arr[n:len(arr):] + arr[0:n:]

def binary_xor(a,b):
    a = a.replace(" ","")
    b = b.replace(" ","")
    print(a, b)
    y = int(a,2) ^ int(b,2)

    return '{:b}'.format(y)

#Initial permut matrix for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#SBOX
S_BOX = [

[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],

[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]


def binvalue(val, bitsize): #Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def substitute(strings ):#Substitute bytes using SBOX
    subblocks = strings.split(" ")
    result = []
    for i in range(len(subblocks)): #For all the sublists
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]),2)#Get the row with the first and last bit
        column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
        val = S_BOX[i][row][column] #Take the value in the SBOX appropriated for the round (i)

        bin = binvalue(val, 4)#Convert the value to binary
        print(bin)
        result += [str(x) for x in bin]#And append it to the resulting list
    return result

def permut(block, table):#Permut the given block using the given table (so generic method)
    return [block[x-1] for x in table]


def generate_roundK(key):
    K_56 = join_name(CP_1,key,57,1)
    print("K_56  is "+join_name(CP_1,key,4,1))
    print("Left halve is %s" %(insert_space(K_56[:len(K_56)//2])))
    print("Right halve is %s" %(insert_space(K_56[len(K_56)//2:])))

    K_56_l = shiftLbyn(list(K_56[:len(K_56)//2]),1)
    K_56_r = shiftLbyn(list(K_56[len(K_56)//2:]),1)
    K_56_n = "".join(K_56_l + K_56_r)
    print("\nLeft1 halve is %s" %(insert_space(K_56_n[:len(K_56_l)])))
    print("Right1 halve is %s" %(insert_space(K_56_n[len(K_56_l):])))

    K_48 = join_name(CP_2,K_56_n,56,1)
    print("\nK_48 is %s" %insert_space(K_48))

    plain_text_join = plain_text.replace(" ","")
    Ip_plaint = join_name(PI,plain_text_join,65, 1)
    print("\nPermutated string is "+ insert_space(Ip_plaint))

    print("\nPermutated string L0 is "+ insert_space(Ip_plaint[:len(Ip_plaint)//2] ))
    print("Permutated string R0 is "+ insert_space(Ip_plaint[len(Ip_plaint)//2:]))

    E_R = join_name(E,Ip_plaint[len(Ip_plaint)//2:]).replace(" ","")
    print("\nExpansion of E(R_0)"+insert_space(E_R))

    A = binary_xor(E_R,K_48)
    print("\nXor result "+insert_space(A))
    print("Length of %d"% len(A))

    S = substitute(insert_space(A,6)[:-1])
    print("\nconcated result %s"%(insert_space("".join(S))))

    final_perm = join_name(P,"".join(S))
    print("\nPermuated result %s" %final_perm)

    R1 = binary_xor("1100 1100 0000 0000 1100 1100 1111 1111".replace(" ",""), final_perm)
    print("\n xor final result %s"% R1)