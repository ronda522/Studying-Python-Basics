# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

user_1 = {
    'username' : "Fistaha",
    'age' : 228,
    'weapons' : 'big_battle_axe',
    "is_active" : True,
    'clan' : "clan_UID_12345"
}

user_1.keys()

user_1['weapons'] = "long_battle_sword"

user_1.update({'is_banned' : False})

user_1['is_banned'] = True

user_2 = user_1.copy()

user_2.update({'age' : 84})
user_2.update({'username' : 'reih_master_adolf_1941'})

print(user_2)

print(user_1)

# {'username': 'reih_master_adolf_1941', 'age': 84, 'weapons': 'long_battle_sword', 'is_active': True, 'clan': 'clan_UID_12345', 'is_banned': True}
# {'username': 'Fistaha', 'age': 228, 'weapons': 'long_battle_sword', 'is_active': True, 'clan': 'clan_UID_12345', 'is_banned': True}

