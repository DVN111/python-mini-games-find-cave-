import random
welcome_message="Wecome to my games"


print("******************************************")
print(f"*******    {welcome_message}    ********")
print("******************************************")

random_num=random.randint(1,4)

name = input("Hi, whats your name? : ")
print(f'Hello {name}, wellcome to "find your cave"')
print('''now, choose one true cave of this 4 caves to winning the game
        [_] [_] [_] [_]
        1   2   3   4 ''')
chosen_num = int(input("Whats your choise? [1/2/3/4] : "))
print(f"you're choose number {chosen_num}")
confirmation = str(input(f"Are you sure you chose number {chosen_num}? [y/n] : "))

while confirmation == "n":
    print('''now, choose one true cave of this 4 caves to winning the game
        [_] [_] [_] [_]
        1   2   3   4 ''')
    chosen_num = int(input("Whats your choise? [1/2/3/4] : "))
    print(f"you're choose number {chosen_num}")
    confirmation = input(f"Are you sure you chose number {chosen_num}? [y/n] : ").lower
    
if chosen_num == random_num:
    print("You're win")
else:
    print("You're lose")
    