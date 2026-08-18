# user = input("Enter Your Password : ")

# def length(user):
#     if len(user) >= 8:
#         return 1

# has_uppercase = any(char.isupper() for char in user)

# def Uppercase(has_uppercase):
#     if has_uppercase == True:
#         print("true")
#     else:
#         print("false")

password = input("Enter Your Password : ")

has_length = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

score = sum([has_digit, has_length, has_lower, has_upper])

print("Your Password Strength is : ", score)