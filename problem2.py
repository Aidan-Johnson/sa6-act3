strings = ['Eliza', 'Bob', 'Alice', 'Mika']

sorted_strings = sorted(strings, key = lambda x: (len(x), x)) 
print(sorted_strings)