# # Tip calculator with split the bill function

# bill = float(input("How much was your bill?"))
# rating = input("Would you rate your service as: good, fair, or bad?").strip().lower()
# tip = 0
# people = int(input("How many people are splitting the bill?"))
# if rating == "good":
#     tip = 0.20
# elif rating == "fair":
#     tip = 0.15
# elif rating == "bad":
#     tip = 0.10
# else:
#     print("Please rate your service as good, fair or bad.")
#     rating = input("Would you rate your service as: good, fair, or bad?") 

# total_amount = (bill + (bill * tip))
# div_bill = total_amount/people
# print(f"Your total bill is ${total_amount:.2f}")
# print(f"Each person will pay ${div_bill:.2f}")




# Coin counter 


# counter = 0 
# answer = input("Do you want a coin?").strip().lower()
# while answer == "yes":
#     counter +=1 
#     print(f"You have {counter} coins.")
#     answer = input("Would you like another?").strip().lower()
#     if answer == "no":
#         print("Okay, then. Give me my money back.")






# # Lets build a box 

# print("Let's build a box!")
# height = int(input("How many spaces tall should it be?"))
# width = int(input("How many spaces wide should it be?"))

# box_top = ("*" * width)
# print(box_top)

# for i in range(height - 2):
#     print("*" + " " * (width - 2) + "*")

# box_top = ("*" * width)
# print(box_top)
##try joe's suggestion of using range for row and height (for row = 0 and height -1)

##### Joe's box to compare
# width = int(input("Width? "))
# height = int(input("Height? "))
# for row in range(height):
#     if row == 0 or row == height - 1:
#         print("*" * width)
#     else:
#         print("*", end="")
#         print(" " * (width - 2), end="")
#         print("*")



# print a triangle

# print("Let's build a triangle!")
# num_of_rows = int(input("How many rows tall should the triangle be?"))
# spaces = num_of_rows
# stars = -1

# for i in range(num_of_rows):
#     spaces -= 1
#     stars += 2 
#     print(" " * spaces + "*" * stars)


### CLAUDE'S EXAMPLE IN CLASS TO COMPARE
# width = int(input("Please enter an odd number: "))
# spaces = " "
# numstars = "*"
# i = 1
# while i <= width:
#     sp = int((width - i) / 2)
#     print(f"{spaces * sp}{numstars * i}{spaces * sp}")
#     i += 2
#####

#multiplication table 

# first_int = 1
# second_int = 1
# for j in range(10):
#     for i in range(10): 
#         answer = first_int * second_int
#         print(f"{first_int} X {second_int} = {answer}")
#         second_int += 1
#     second_int = second_int - 10 
#     first_int += 1

#### Layne's example to compare
# Multi-table
# num = 1
# while num <= 10:
#     i = 1
#     while i <= 10:
#         product = num*i
#         print(f"{num} * {i}  =  {product} \n")
#         i += 1
#     num += 1
#     print("\n")




    






