import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    
        
    k = int(input())
    for j in range(0,len(arr)-1):
        for i in range(0,len(arr)-j-1):
            if arr[i][k]>arr[i+1][k]:               
                t=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=t
    for i in arr:
        for j in i:
            print(j,end=" ")
        print(" ")
