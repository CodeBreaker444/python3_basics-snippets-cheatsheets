def table(self):
  n= int(input("Enter a Number:"))
  for i in range(1,20):
    print("%d×%d=%d"%(n,i,n*i))
def multiplication(self):
    i,j=[int(x) for x in(input("Enter two Numbers:")).split()]
    print('%d×%d=%d'%(i,j,i*j))

def addition(self):
    i, j = [int(x) for x in (input("Enter two Numbers:")).split()]
    print('%d+%d=%d' %(i, j, i+j))
    return 'addd'
def sub(self):
    i, j = [int(x) for x in (input("Enter two Numbers:")).split()]
    print('%d-%d=%d' % (i, j, i-j))
def div(self):
    i, j = [int(x) for x in (input("Enter two Numbers:")).split()]
    print('%d/%d=%d' % (i, j, i // j))
def sqrt(self):
    i, j = [int(x) for x in (input("Enter a Number and Power:")).split()]
    print('%d power of %d=%d' % (j, j, i ** j))

switcher = {
    1: addition,
    2: sub,
    3: multiplication,
    4: div,
    5: sqrt,
    6: table
   }
def main(c):
    if switcher.get(c) == None:
        print(switcher.get(c,"Invalid Choice"))
        scan()
    else:
        switcher[c]("Done")
def scan():
    c=int(input('\n1:Addition\n2:Substraction\n3:Multiplication\n4:Division\n5:Power Of a Number\n6.Table\nEnter Your Choice:'))
    main(c)
scan()
