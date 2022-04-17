import random
character = "0123456789abcdefghijklmnopqrstuvwxyz!%§!!*'ABCDEFJHNMLOP3!"
character_list = list(character)
password = input("Enter your password: ")
guess = ""
while (guess != password):
    guess = random.choices(character_list,k=len(password))
    print(guess)
    guess = "".join(guess)
    print ("youre password is " + guess)

