dictionary = {}

dictionary['superman'] = 'he is very strong'
dictionary['flash'] = 'he is the fastest man in the world'

dictionary.pop('superman')

dictionary = {'superman' : {'power1':'he is very strong', 'power2':'he can fly'},'flash' : 'he is the fastest man in the world', 'green lantern': 'he is the choosen one'}

for key in dictionary:
    print(key)
    print(dictionary[key])