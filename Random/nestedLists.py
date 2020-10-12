# #Accessing Nested Lists
# nested_list = [[1,2,3,],[4,5,6,],[7,8,9]] 

# nested_list[0][1] #2

# nested_list[1][-1] # 6

# #Printing Values in Nested Lists
# nested_list = [[1,2,3,],[4,5,6,],[7,8,9]]

# for l in nested_list:
#     for val in 1:
#         print(val)

# #Nested List Comprehension
# [[print(val) for val in l] for l in nested_list]

# #Another example
# board = [[num for num in range(1,4)] for val in range(1,4)]

# print(board)

# [["x" if num % 2 != 0 else "O" for num in range(1,4) for val in range(1,4)]]