import sys
#functions

#multiplication function
print('functions:')
def multiply(f,n):
    mul=f*n
    return mul
print('Multiplication of %d×%d=%d'%(10,5,multiply(10,5)))

#use inputs and functions
#print('Enter two values:')
#i,j = map(int,sys.stdin.readline().split())
i,j = [int(x) for x in input("Enter Two Number:").split()]
print('Multiplication of %d×%d=%d'%(i,j,multiply(i,j)))