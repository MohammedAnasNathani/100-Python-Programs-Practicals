list1 = [x for x in range(1, 11)]
list2 = [x**2 for x in range(1, 11)]
list3 = [x for x in range(1, 11) if x % 2 == 0]
list4 = [x + 5 for x in range(1, 11)]
list5 = [chr(65 + x) for x in range(10)]

print(list1, list2, list3, list4, list5)
