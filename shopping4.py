Final_cart = {}

while True:
    user = input("enter item name (or 'done' to finish ) : ")

    if user.lower() == "done":
        break
    price = int(input("enter the price : "))
    Final_cart[user] = price

print("--Recipt--")
for key, value in Final_cart.items():
    print(f"{key} : {value}")


# ------------Old MISTAKES------------#
# subtotal = 0

# for amount in Final_cart.values():
#     subtotal += amount

# print("SubTotal : " ,subtotal)

# discounted_amount = subtotal * (10 / 100)
# final_total = subtotal * (1 - 10 / 100)
# print("10% Discount : ", discounted_amount )
# print("Final price is : ", final_total)


# -------------NEW VERSION---------------#
subtotal = sum(Final_cart.values())

if subtotal > 50:
    discount = subtotal * 0.10
else:
    discount = 0.0

final_total = subtotal - discount

print(f"subtotal: ${subtotal:.2f}")
print(f"discount: ${discount:.2f}")
print(f"final_total: ${final_total:.2f}")

