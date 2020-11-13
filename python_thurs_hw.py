# multiply vectors 

# one = [2, 4, 5]
# two = [2, 3, 6]
# new_list = []
# for num in range(len(one)):
#     new_num = one[num] * two[num]
#     new_list.append(new_num)
# print(new_list)


## Matrix addition

# x = [[2, 3], [4, 5]]
# y = [[1, 4], [2, 6]]

# sum = []

# for i in range(len(x)):
#     row = []
#     for j in range(len(x[0])):
#         sum_x_y = x[i][j] + y[i][j]
#         row.append(sum_x_y)
#     sum.append(row)
# print(sum)


###extend matrix solution for larger matrix

# x = [[2, 3, 2], [4, 5, 6], [7, 9, 1], [4, 4, 3]]
# y = [[1, 4, 4], [2, 6, 8], [1, 2, 5], [6, 2, 3]]

# sum = []

# for i in range(len(x)):
#     row = []
#     for j in range(len(x[0])):
#         sum_x_y = x[i][j] + y[i][j]
#         row.append(sum_x_y)
#     sum.append(row)
# print(sum)

### delete repititions in a string 

# feelings = ["happy", "sad", "happy", "angry", "sad", "sad", "excited", "bored"]
#numbers = [1, 3, 4, 5, 8, 9, 8, 8, 1, 1, 3, 3, 3, 5, 4]

# # looked up online
# # new = list(dict.fromkeys(feelings))
# # print(new)

# ##my version after googling and using set and "if not in"  
# #can use numbers or strings
#could convert to a set which is a list which doesnt allow duplicates 
# new_list = []
# for i in feelings: 
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)




### Leet speak -- makes spaces too wide between words

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# leet_substitutions = "48<}3=6#17}[mn0pO2$tuVW%y>"

# string_input = input("Type a string and I will translate it to leetspeak.")
# input_string = ""
# for i in range(len(string_input)):
#     for j in range(len(alphabet)):
#         if string_input[i] == alphabet[j]:
#             input_string += leet_substitutions[j]
#         elif string_input[i] == " ":
#             input_string += " "

# print(input_string)  





###Given solution to leetspeak
# word = input('The word: ').upper()

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

# word = word.replace('A', '4')
# word = word.replace('E', '3')
# word = word.replace('G', '6')
# word = word.replace('I', '1')
# word = word.replace('O', '0')
# word = word.replace('S', '5')
# word = word.replace('T', '7')

# print(word)





###### long vowels 

