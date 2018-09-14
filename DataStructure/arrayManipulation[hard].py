#!/bin/python3
from itertools import accumulate
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):    
    for i in range(len(queries)):
        q=queries[i]        
        zero[q[0]-1]+=q[2]
        zero[q[1]]-=q[2]    
    return max(accumulate(zero))        
        
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    q=[]
    queries = []
    zero=[]
    zero = [0]*(n+1)
        
                    

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
