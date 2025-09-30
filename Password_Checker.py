username = input("Enter your username: ")
password = input("Enter your password: ")

password_leghts = len(password)

password = '*' * password_leghts 

print(f"{username}, your password {password} is {password_leghts} long")