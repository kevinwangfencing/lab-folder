# labs/chapter_04.py
# Camel game

# Distance traveled in miles
miles_traveled = 0

# Thirsty level
thirst = 0

# Tiredness level of camel
camel_tiredness = 0

# Distance of native in miles
native_distance = -20

# Initial number of drinks in the canteen
i_drink_canteen = 10
import random
oasis = random.randint(1,20)

# 1, printing statements
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")

# Options
done = False
while done == False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    choice = input("What is your choice? A/B/C/D/E/Q: ").upper()

    # When user choose Q
    if choice == "Q":
        done == True
        print("----You quit the game----")
        break

    # When user choose E
    elif choice == "E":
        print("Miles traveled: " , miles_traveled, "miles")
        print("Thirst level: " , thirst)
        print("Camel tirdness: " , camel_tiredness)
        print("Native distance: " , native_distance, "miles")
        print("Drinks in canteen: " , i_drink_canteen)

    # When user choose D
    elif choice == "D":
        camel_tiredness = 0
        print("Camel is happy! ")

        import random
        native_d_random = random.randint(7,14)

        native_distance = (native_distance + native_d_random)
        distance_behind = (miles_traveled - native_distance)
        print("The native are" , distance_behind, "miles behind you.")

    # When user choose C
    elif choice == "C":
        import random
        full_s_random = random.randint(10,20)
        miles_traveled = miles_traveled + full_s_random
        print("You have travelled" , miles_traveled, "miles.")
        
        # Add one to thirst
        thirst = thirst + 1

        # Add random to tiredness from 1 to 3
        camel_t_random = random.randint(1,3)
        camel_tiredness = (camel_tiredness + camel_t_random)

        # Move natives 7 to 14 miles
        native_d_random = random.randint(7,14)
        native_distance = (native_distance + native_d_random)
        distance_behind = (miles_traveled - native_distance)
        print("The native are" , distance_behind, "miles behind you.")

    # When user choose B
    elif choice == "B":
        import random
        moederate_s_random = random.randint(5,12)
        miles_traveled = miles_traveled + moederate_s_random
        print("You have travelled" , miles_traveled, "miles.")
        
        # Add one to thirst
        thirst = thirst + 1

        # Add one to camel tiredness 
        camel_tiredness = camel_tiredness + 1

        # Move natives 7 to 14 miles
        native_d_random = random.randint(7,14)
        native_distance = (native_distance + native_d_random)
        distance_behind = (miles_traveled - native_distance)
        print("The native are" , distance_behind, "miles behind you.")

    # When user choose A
    elif choice == "A":
        print("**Your have", i_drink_canteen, "drinks before drinking**")
        if i_drink_canteen > 0:
            i_drink_canteen = i_drink_canteen - 1
            print("**You now have", i_drink_canteen, "drinks left**")
            thirst = 0
        else:
            print("Error")

    # Thirst level greater than six
    if thirst > 6:
            print("You died of thirst! ")
            done = True
    # Thirst level greater than four
    elif thirst > 4:
        print("You are very thirsty! ")


    # Camel tiredness greater than eight
    if camel_tiredness > 8:
        print("Your camel is dead ")
        done = True
    # Camel tiredness greater than five
    elif camel_tiredness > 5:
        print("Your camel is getting tired ")


    # Native caught up
    if native_distance >= miles_traveled:
        print("You have been caught ")
        print("***Game over***")
        done = True
    
    # Native is getting closed
    elif native_distance + 15 >= miles_traveled:
        print("The natives are getting close! ")
    
    # Distance travelled
    if miles_traveled >= 200:
        print("You have travelled 200 miles across the desert ")
        print("***You won the game!!***")
        done = True

    # Oasis is found
    if oasis == 1:
        oasis = True
        print("*****You found an oasis*****")
        i_drink_canteen = 10
        thirst = 0
        camel_tiredness = 0
