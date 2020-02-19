
import random


print("Welcome to Battle of Jakku")
print("Your squad has crash down and is needed to get across the battle to get into reforcements Tie-class fighters and transports")
print("The rebel soldiers has caught of yours plans, get to your starfighters before they steal them")
print("Since the rebels are riding a stoled Clone Wars Era Republican Juggernaunt (carries up to 60 troops) they are not feeling the heat or exhaustion due to being inside of the transports")
print("However they are missing a couple wheels so the Juggernaunt is slow")
print("They also deploy random squads of rebel soldiers to caputure your squad for interrogation")



# initiate variables
done = False
milesTraveled = 0
rebelsTraveled = -20
squadTiredness = 0
thirst = 0
canteen = 3
downedImperialTransport = -1
rebelreforcements = -1
blasterammo = 12



while not done :
        
    # options
    print("A. squad takes a drink.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print("F. squad fight rebels ambushers reforcements.")
    print("L. squad flees from rebel ambushers reforcements.")
    print()
    
    
    
    # Take user's input
    userInput = input("What will you do? ")
    
    # Check if they want to quit
    if userInput.upper() == "Q" :
        done = True
    # Status update
    elif userInput.upper() == "E" :
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("The rebel are", milesTraveled - rebelsTraveled, "miles behind you.")
        print()
    # stop for the night
    elif userInput.upper() == "D" :
        print("You stop for the night.")
        print("Your squad is happy.")
        print("The rebels don't stop.")
        print()
        squadTiredness = 0
        rebelsTraveled += random.randrange(7, 15)
    # full speed ahead
    elif userInput.upper() == "C" :
        miles = random.randrange(10, 21)
        milesTraveled += miles
        thirst += 1
        squadTiredness += random.randrange(1, 4)
        rebelsTraveled += random.randrange(7, 15)
        downedImperialTransport = random.randrange(20)
        if downedImperialTransport == 10 :
            thirst = 0
            squadTiredness = 0
            canteen = 3
            print("your squad travel you happen upon an down imperial transport!")
            print("Sadly there was no surivors however you and your squad finds a cache full of rations and water ")
            print("Your squad is rested!")
            print("The rebels continue the chase.")
            print()
        else :
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The rebels continue the chase.")
            print()
    # mid-speed ahead
    elif userInput.upper() == "B" :
        miles = random.randrange(5, 13)
        milesTraveled += miles
        thirst += 1
        squadTiredness += 1
        rebelsTraveled += random.randrange(7, 15)
        downedImperialTransport = random.randrange(20)
        if downedImperialTransport == 10 :
            thirst = 0
            squadTiredness = 0
            canteen = 3
            print("As you travel you happen upon an downed transport!")
            print("Your squad takes a break")
            print("Your squad is rested!")
            print("The rebels see your squad resting ")
            print()
        else :
            print("You move forward, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The rebels continue the chase.")
            print()
    # Drink from canteen
    elif userInput.upper() == "A" :
        if canteen > 0 :
            canteen -= 1
            thirst = 0
            print("Your squad take a drink")
        else:
            print("Your canteens is empty. the entire squad is thirsty.")
    
    # using blasters
    if userInput.upper() == "F" :
        if blasterammo > 0 :
            blasterammo -= 1
            print

    
    # Status updates
    # Thirst
    if thirst > 5 :
        print("Your squad died of thirst!")
        print("Game Over.")
        print()
        done = True
    elif thirst > 4 :
        print("You are thirsty!")
    # Distance traveled / win check
    if milesTraveled >= 200 :
        print("Congratulations! You reach the imperial starfighter, time to revenege you rebel scums!")
        print("You win!")
        print()
        done = True
    # squad's tiredness
    if squadTiredness > 8 :
        print("Your squad died of exhaustion!")
        print("With no squad, the rebel catch up to you and captures you")
        print("on the spot.")
        print("Game Over. well atleast i get to talk to princess Leia")
        print()
        done = True
    elif squadTiredness > 5 :
        print("Your squad is tired. it's too hot in this armor")
        print()
    # rebels distance from you
    if milesTraveled - rebelsTraveled <= 0 :
        print("The rebels have caught up with you!")
        print("They capture your squad and interrgate you into telling the location of the star fighters.")
        print("Game Over.")
        print()
        done = True
    elif milesTraveled - rebelsTraveled < 15 :
        print("You see faint shapes on the horizon behind you.")
        print("The rebels are getting close!")
        print()

# Exit message
print("Exiting Game. Goodbye.")
input("")