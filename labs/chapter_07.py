# Chapter_07.py

# Adventure Dungeon game

room_list = []
# Room 0
room = ["You are in a drark room, There are doors to East, South, West", None, 3, 5, 1]
room_list.append(room)
# Room 1
room = ["This is a living room, There are doors to East and South", None, 0, 2, None]
room_list.append(room)
# Room 2
room = ["This is a washroom room, There are doors to North and East", 1, 5, None, None]
room_list.append(room)
# Room 3
room = ["This is a kitchen, There are doors to South and West", None, None, 4, 0]
room_list.append(room)
# Room 4
room = ["This is a Bedroom, There are doors to North and West", 3, None, None, 5]
room_list.append(room)
# Room 5
room = ["This is a Bedroom, There are doors to North, East, West", 0, 4, None, 2]
room_list.append(room)

# The current room user is in
current_room = 0
print(current_room)

done = False

# Loop starts here
while done == False:
    if done == False:
        print(((room_list)[current_room][0]))
        print()
        print("==If quit type Q or Quit==")
        user_input = str(input("What do you want to do next: ")).upper()

        # When user enter North
        if user_input == "North" or user_input == "N":
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You can't go that way", end = "\n")
            else:
                current_room = next_room
        
        # When user enter East
        elif user_input == "East" or user_input == "E":
            next_room = room_list[current_room][2]
            if next_room == None:
                print("You can't go that way", end = "\n")
            else:
                current_room = next_room

        # When user enter South
        elif user_input == "South" or user_input == "S":
            next_room = room_list[current_room][3]
            if next_room == None:
                print("You can't go that way", end = "\n")
            else:
                current_room = next_room

        # When user enter West
        elif user_input == "West" or user_input == "W":
            next_room = room_list[current_room][4]
            if next_room == None:
                print("You can't go that way", end = "\n")
            else:
                current_room = next_room

        # When user enter Quit
        elif user_input == "Quit" or user_input == "Q":
            print("==You quit the game==")
            done = True

        # # When user enter an invalid response
        else:
            print("Your input is invalid! ", end = "\n")


    else:
        done = True
