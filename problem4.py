list1 = [2,'hi', 47, 'zomg', 'markimoo']
list2 = [3, 'hi', 47, 'gojo satoru', 'markimoo']
list3 = []
intersect = list(filter(lambda x: x in list1, list2))
print(intersect)
