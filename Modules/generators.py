__description__ = """Examples of generators - list generator, Dictionary generator, 
and a sum of a list (discards the array)."""


sampledata = ['shrimp', 'shrimp cocktail', 'chicken', 'beef', 'pork', 'shrimp sandwhich', 'fried shrimp',
              'bubba gump shrimp', 'tomatoes', 'lemons', 'peaches']

a = [x for x in range(1, 10)]
print(a)

d = {x: 0 for x in ('Yellow', 'Red', 'Green', 'Blue')}
print(d)

s = sum([x for x in range(0, 11)])
print(s)

shrimp_dishes = [x for x in sampledata if 'shrimp' in x]
print("shrimp Dishes:")
for i in shrimp_dishes:
    print(i)

