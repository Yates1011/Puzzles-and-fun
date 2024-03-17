# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:26:21 2022

@author: yates
"""

import timeit

def norm_list(n=100_000_000):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst
        
def list_comp(n=100_000_000):
    return [i for i in range(n)]      

def list_range(n=100_000_000):
    return list(range(n))
  
def main():
    print('norm\t\t', timeit.timeit(norm_list,number=1))
    print('list comp\t\t', timeit.timeit(list_comp,number=1))
    print('range\t\t', timeit.timeit(list_range,number=1))
    
if __name__ == '__main__':
    main()