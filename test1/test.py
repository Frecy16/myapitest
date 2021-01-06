# 过滤掉长度小于或等于3的人名
# name_list = ['Tom', 'Lily', 'Lucy', 'Jack', 'Steven', 'Bob', 'Jone', 'Ha']
#
# result = [name for name in name_list if len(name) > 3]
# print(result)

# capitalize() 首字母大写
# casefold() 首字母小写
# result1 = [name.casefold() for name in name_list if len(name) > 3]
# print(result1)

# 将1-100之间能被3整除，组成一个新的列表
# num_list = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
# print(num_list)

# g = (n for n in range(1, 11))
# for i in g:
#     print(i)

# list1 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
# print(list1)

list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 3, 5)]
new_list2 = [i[-1] for i in list2]
print(new_list2)
