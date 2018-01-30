
#String
print('Strings:')
statement="Hi How are you"
print(statement[0:2])
print(statement[3:-7])
print(statement[-7:])
print(statement+" Iam fine")
print(statement.capitalize())
print(statement.find('are'))
print(statement.isalpha())
print(statement.isalnum())
print(statement.isprintable())
print(len(statement))
print(statement.replace("you","you?"))
print(statement.strip())
#split into list
statement_list=statement.split(" ")
print(statement_list)