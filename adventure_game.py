print("Welcome to the adventure game")
door = input("You see a green and red door which do you choose? ")
if door == "green":
    alley = input("You see two alley do you want to go left or right? ")
    if alley == "left":
        dog = input("You see a dog coming do you run or do you stay? ")
        if dog == "run":
            cliff = input("You get to a cliff there water below do you jump or wait? ")
            if cliff == "jump":
                print("You win")
            else:
                print("You were almost there but you lost")
        else:
            print("You lose")
    else:
        print("You lose")
else:
    print("You lose")
