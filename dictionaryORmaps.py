print('Dictionaries are like lists but every value is given a key insted of position')
dict_phone={'Phone1':'9440675365','Phone2':'9441836592','Phone3':'8330990980'}
print(dict_phone['Phone2'])
del dict_phone['Phone3']
print(dict_phone)
dict_phone['Phone2']='8330990980'
print(dict_phone)
print(len(dict_phone))
print(dict_phone.get('Phone2'))
print(dict_phone.keys())
print(dict_phone.values())