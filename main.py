def main():
    print("""
    You are a Witcher, and you are lost in forest;
    You have two swords, There is also a horse named Carrot.
    Now, what do you want do?
    > 1. Follow the path
    > 2. Deep into the forest
    """);
    chose = int(input("> "))
    if(chose == 1):
        branch_path()
    elif(chose == 2):
        print("You fell from a height of two meters and fell to your death.")
    else:
        print("Try to follow the instructions and enter the numbers, otherwise you will starve to death in place, bro.")

def branch_path():
    print("""
    You encounter a gang of robbers robbing a noble caravan.
    Then the caravan is calling you for help.
    You want:
    > 1. screw you, I am busy.
    > 2. Draw your iron sword and fight the bandits.
    """)
    chose = int(input("> "))
    if(chose == 1):
        print("You just move on as if you didn't see it")
    elif(chose == 2):
        print("You cast magic seals and wield iron swords, and this group of robbers is not your opponent at all.")
    else:
        print("You do nothing, and then you are hacked to death.")




main();