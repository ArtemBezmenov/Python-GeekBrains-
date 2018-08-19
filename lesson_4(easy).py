# Ex.1:
list_1 = [1, 123, 532, 1351]
new_list = [x ** 2 for x in list_1]
print(new_list)

# Ex.2:
fruit_1 = ['яблоко','апельсин','мандарин','вишня']
fruit_2 = ['черешня','манго','апельсин','киви','яблоко']
fruit_3 = [name for name in fruit_1 if name in fruit_2]
print(fruit_3)

# Ex.3:
numbers = [1, 7, 8, 12, 16, 10, 62, 8359, 18358935, 123123, -131239, -321, 6553863568, 12312321, 14231, 3, 9, 12]
numbers_correct = [x for x in numbers if x > 0 and x % 4 != 0 and x % 3 == 0]
print(numbers_correct)