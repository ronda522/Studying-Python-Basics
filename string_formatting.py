# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50)) # Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {1}.".format("Cindy", 50)) # Hello Cindy, your balance is 50.

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50)) # Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50)) # Hello Cindy, your balance is 50.

# 2 How would you write this using f-string? (Scroll down for answer)

new_name = "Zazhymenko"
new_amount = 0.1

print(f"Hello {new_name}, your balance is {new_amount}.") # Hello Zazhymenko, your balance is 0.1.