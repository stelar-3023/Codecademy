# def double_index (lst, index):
#     if  index < len(lst):
#         lst[index] = lst[index] * 2
#         return lst
# print(double_index([3, 8, -10, 12], 1))

# def remove_middle(lst, start, end):
#     return lst[:start] + lst[end+1:]
# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 4)) 

# def more_than_n(list, item, n):
#     if list.count(item) > n:
#         return True
#     else:
#         return False
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 3, 1))  

# def more_frequent_item(lst, item1, item2):
#     if lst.count(item1) >= lst.count(item2):
#         return item1
#     else:
#         return item2   
# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# def middle_element(lst):
#   if len(lst) % 2 == 0:
#     sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
#     return sum / 2
#   else:
#     return lst[int(len(lst)/2)]
# print(middle_element([5, 2, -10, -4, 4, 5]))

# def append_sum(lst):
#     i = 0
#     while i < 6:
#         lst.append(lst[-2] + lst[-1])
#         i += 1
#     return lst
# print(append_sum([1, 1, 2]))

# def larger_list(lst1, lst2):
#     if len(lst1) >= len(lst2):
#         return lst1[-1]
#     else:
#         return lst2[-1]    
# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10, 6]))

# def combine_sort (lst1, lst2):
#     unsorted = lst1 + lst2
#     sortedList = sorted(unsorted)
#     return sortedList
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# def append_size (lst):
#     list1 = len(lst)
#     lst.append(list1)
#     return lst
# print(append_size([23, 42, 108]))   

# def every_three_nums(start):
#     list1 = range (start, 101, 3)
#     if start > 100:
#         return []
#     else:
#         return (list(list1))
# print(every_three_nums(5))

#Tuple
my_info = ('Steve', 44, 'Dialer Manager')
print(my_info[0])
name, age, occupation = my_info #unpacking tuple
print(name)