#!/usr/bin/python
import sys
import math

def main():
   a = raw_input().split(",")
   b = raw_input().split(",")
   z = a + b
   for item in z:
        print('%s'%(str(item))) 

if __name__=='__main__':
   main()
