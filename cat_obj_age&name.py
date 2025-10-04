class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(cat1, cat2, cat3):
        ages = [cat1.age, cat2.age, cat3.age]
        return print(f"The oldest cat is {max(ages)} years old.")


Ruby = Cat('Ruby', 4)
Silvie = Cat('Bobbiek', 6)
Booord = Cat('Coal', 3)

Cat.oldest_cat(Ruby, Silvie, Booord)
# 1 Instantiate the Cat object with 3 cats


# 2 Create a function that finds the oldest cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
