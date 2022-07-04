print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose = input("You will choose left or right:").lower()

if choose == "right":
    print("You fall into a hole. GAME OVER.")
else:
    choose = input("You arrive in a river, with strong waves. You will try to swin or wait? ").lower()
    if choose == "swin":
        print("You goes away by the waves. GAME OVER.")
    else:
        print("After you waited, you see a small boat. You through the river with it and arriver in a village.")
        choose = input("In the village you found three houses, the red, blue and yellow one, how house you choose? ").lower()
        if choose == "red":
            print("When you open the door a wave of flames cross you and you fall burned down. GAME OVER.")
        elif choose == "blue":
            print("When you open the door, you free a angry bear that attacked you and you fall down. GAME OVER.")
        elif choose == "yellow":
            print("When you open the door, you see a box, and when you open it inside have a lot of brights coins.")
            print("CONGRATULATIONS, YOU WON THE GAME!!")
        else:
            print("You took a long time to decide and you have not saw the storm approaching that blow you away. GAME OVER.")