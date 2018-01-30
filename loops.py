import random

#forloop
print('For LOOP:')
for x in range(0,10):
    print(x,'',end="")
    subjects = ['English', 'Hindhi', 'Maths', 'Computers', 'Telugu']

for y in subjects:
    print('\t',y,end="")
print('\n')
for x in [24,68,78,10]:
        print(x)

#two-d_Array
num=[[1,2,3],[4,5,6],[7,8,9]]

for x in range(0,3):
    for y in range(0,3):
        print(num[x][y],end="")

#two-table
print('\nTwo Table:')
input=2
for x in range(0,20):
    print('%d * %d =%d'%(input,x,input*x))
    #print(input,'*',x,'=',input*x)

#While Loop
random_num=random.randrange(0,99)
while(random_num!=75):
    print(random_num,end="")
    random_num=random.randrange(0,99)
#even or not
print('\nEvennumbers:\n')
i=0;
while(i<=20):
    if(i%2==0):
        if i==0:
            i+=1
            continue
        else:
            print('Even Number:',i,'\t',end="")
            i+=1
            continue
    elif i==11:
        break
    else:
        i+=1
        continue
