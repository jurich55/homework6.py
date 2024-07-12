   # словарь
my_dict = {'Petya':1985, 'Vasya':1988, 'igor':1992, 'Nina':1998}
print(my_dict)
print(my_dict.get('Nina'))
print(my_dict.get('Oleg'))
my_dict.update({'Alex':2001, 'Masha':1995})
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict)
print(a)
    # множества
my_set_ = {5,2,'p',1,4,5,1}
print(my_set_)
my_set_.remove('p')
print(my_set_)
my_set = {7,9}
my_set_.update(my_set)
print(my_set_)
my_set_.discard(5)
print(my_set_)