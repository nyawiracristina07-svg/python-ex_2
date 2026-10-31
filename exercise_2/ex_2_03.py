amount = input("give me the amount:")
amount_float = float(amount)
print(amount_float)

if 50 < amount_float < 100:
    total = 0.9 * amount_float
    print(f"To pay: {round(total,2)}")

elif amount_float >= 100 :
    total = 0.8 * amount_float
    print(f"To pay: {round(total,2)}")
else:
    print(f'To pay: {amount_float}')