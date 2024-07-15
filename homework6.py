my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Egor'))
print(my_dict.get('Suhrob', "doesn't exist"))
my_dict.update({'Pasha': 899944422, 'Ksyusha': 791888343})
a = my_dict.pop('Vasya')
print(a)
del my_dict['Masha']
print(my_dict)

# Множества
my_set = {1, 2, 3, 4, 1, 2, 3}
print(my_set)
my_set.update({5, 6})
my_set.discard(1)
print("Modified set:", my_set)