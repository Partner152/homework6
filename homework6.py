my_dict={'Егор':1985, 'Мария':2015, 'Михаил':2020}
print(my_dict)
print((my_dict)['Мария'])
print(my_dict.get('Виктория'))
my_dict.update({'Виктор':1956,'Светлана':1958})
del my_dict['Мария']
print(my_dict)
my_set = {12,21,56,"caps",'false', 21,12}
print(my_set)
my_set.add(14)
my_set.add(13)
my_set.discard('false')
print(my_set)