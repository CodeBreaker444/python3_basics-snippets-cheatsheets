import os
import sys
import random
print('lists are like arrays and can be of any data type:')
todo_list = ['Wakeup','breakfast','lunch','snacks','dinner','8:00-12:00',65]
todo_list[0] = 'morning'
print('To Do:',todo_list[0:7])
subjects = ['English','Hindhi','Maths','Computers','Telugu']
final_list=[todo_list,subjects]
print(final_list)
print('append is like concat')
subjects.append('Social')
print(subjects)
print('Insert is going to insert at a specifc posisition')
subjects.insert(0,'Science')
print(subjects)
todo_list.remove(65)
print(todo_list)
del subjects[1]
print(subjects)
subjects.sort()
todo_list.insert(7,'65')
todo_list.sort()
print(subjects)
print(todo_list)
final_list=todo_list+subjects
print(final_list)
print('length of subjects:',len(subjects))
print('Minimum of ToDoList',min(todo_list))
print('Max of ToDoList',max(todo_list))