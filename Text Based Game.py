class instructions():
    print("After getting into a crash out on the town you awake in what seems to be an abandoned warehouse..",end='\n')
    print("You hear a terrifying chainsaw in the distance and need to escape.. you find a torn paper that has a map and some items listed on it..",end='\n')
    print("You need to collect these items and escape this maniac that has taken you! Are you able to escape or will you fall victim to this nightmare?",end='\n')
    print("You start off in an open room and there is doors all around you, throughout this adventure gather these items without getting caught and escape!", end='\n')
    print("For moving you will just need to type the direction you want to go, 'North, South, East, West', and they will walk you into these rooms, also to gather",end='\n')
    print("these items you will need to type the prompt: get 'item name' and this will be added to your inventory.. Good luck on your escape!")
    

new_game = input('Ready to escape this nightmare? We start in the central room. (choose Y or N): ')

if new_game == 'n' or new_game == 'N':
    print('Looks like you have fallen victim! How tragic!')
elif new_game == 'y' or new_game == 'Y':
    instructions()

direction = input('Please choose a direction: (North, South, East, West):')


def room1():
    print('You are here in the Northern Room. There is a flashlight located in this room..\n')
    print('To gather this item type "get flashlight", from here we have a room to the West, East and South. Where to go now?')
#if direction == 'East':
#    print('You are now in the Northeastern Room, here lies a stool!')
#elif direction == 'South':
#    print('You are back in the starting room, get out of here and escape!')
#elif direction == 'West':
#    print('You are now in the Northwestern Room, here lies a Door Key!')
#elif direction == 'North':
#    print('You can not go that way, nothing is there..Choose again.')
def room2():
    print('You are in the :\n')
    print('To the North is the Storage Room.\n')
    print('To the East is the Classroom.\n')
    print('To the South is the Nurses office.\n')
    print('To the West is the Deans office.\n')

#if direction == 'North':
#    print('You are now in the Storage room!')
#elif direction == 'South':
#    print('You are now in the Nurses office!')
#elif direction == 'East':
#    print('You will end up in the Deans office again!')
#elif direction == 'West':
#    print('You are now in the Classroom!')

def room3():
    print('You are in the Nurses office:\n')
    print('To the North is the Gallery.\n')
    print('To the East is the Lunch room....Beware the guards are in there!\n')
    print('To the South is Nothing!\n')
    print('To the West is Nothing!\n')

#if direction == 'North':
#    print('You are in the Gallery again!')
#elif direction == 'South':
#    print('You can not go that way!')
#elif direction == 'East':
#    print('You dont want to enter there! Its the security guards!')
#elif direction == 'West':
#    print('You can not go that way!')

def room4():
    print('You are in the Classroom:\n')
    print('To the North is the Bathroom\n')
    print('To the East is the Nothing!\n')
    print('To the South is Nothing!\n')
    print('To the West is the Gallery\n')

#if direction == 'North':
#    print('You are in the Bathroom!')
#elif direction == 'South':
#    print('You can not go that way!')
#elif direction == 'East':
#    print('You can not go that way!')
#elif direction == 'West':
#    print('You are now back in the Gallery!')

def room5():
    print('You are in the Bathroom:')
    print('To the North is Nothing\n')
    print('To the East is Nothing\n')
    print('To the South is the Classroom\n')
    print('To the West is Nothing\n')

#if direction == 'North':
#    print('You can not go that way!')
#elif direction == 'South':
#    print('You are now in the Classroom!')
#elif direction == 'East':
#    print('You can not go that way!')
#elif direction == 'West':
#    print('You can not go that way!')

def room6():
    print('You are in the Storage Room:')
    print('To the North is Nothing\n')
    print('To the East is the Utility Closet\n')
    print('To the South is the Gallery\n')
    print('To the West is Nothing!\n')

#if direction == 'North':
#    print('You can not go that way!')
#elif direction == 'South':
#    print('You are now in the Gallery again!')
#elif direction == 'East':
#    print('You are now in the Utility closet!')
#elif direction == 'West':
#    print('You can not go that way!')

def room7():
    print('You are in the Utility Closet:\n')
    print('To the North is Nothing\n')
    print('To the East is Nothing\n')
    print('To the South is Nothing\n')
    print('To the West is the Storage room\n')

#if direction == 'North':
#    print('You can not go that way!')
#elif direction == 'South':
#    print('You can not go that way!')
#elif direction == 'East':
#    print('You can not go that way!')
#elif direction == 'West':
#    print('You are back in the Storage room.')

def room8():
    print('You are in the Lunch room:\n')
    print('The security guards have caught you and kicked you out of the school! Better luck next time!')


room1 = input('You are in the Deans Office: What direction do you want to go? (North, East, South, West): ')

while direction == 'East':
    room5()
    print('You are now in the Gallery!')
    if direction == 'South':
        room1()
        print('Wrong Way')
    elif direction == 'North':
        room1()
        print('Wrong way')
    elif direction == 'West':
        room1()
        print('Wrong Way')
        room2 = input('You are in the Gallery: What direction do you want to go? (North, East, South, West): ')
    break

while direction == 'North':
    room6()
    print('You are now in the Storage Room!')
    if direction == 'South':
        room3()
        print('You are now in the Nurses Office!')
    elif direction == 'East':
        room4()
        print('You are now in the Classroom!')
    elif direction == 'West':
        room1()
        print('You are back in the Deans office!')
    break

room3 = input('You are in the Nurses Office: What direction do you want to go? (North, East, South, West): ')

while direction == 'North':
    room2()
    print('You are now back in the Gallery!')
    if direction == 'South':
        print('You can not go that way!')
    elif direction == 'East':
        room8()
        print('Oh No! The guards have gotten you!')
    elif direction == 'West':
        print('You can not go that way!')
    break

room4 = input('You are in the Classroom: What direction do you want to go? (North, East, South, West): ')

while direction == 'North':
    room5()
    print('You are now in the Bathroom!')
    if direction == 'South':
        print('You can not go that way!')
    elif direction == 'East':
        print('You can not go that way!')
    elif direction == 'West':
        room2()
        print('You are back in the Gallery!')
    break

room5 = input('You are in the Bathroom: What direction do you want to go? (North, East, South, West): ')

while direction == 'North':
    print('You can not go that way!')
    if direction == 'South':
        room4()
        print('You are now back in the Classroom!')
    elif direction == 'East':
        print('You can not go that way!')
    elif direction == 'West':
        print('You can not go that way!')
    break

room6 = input('You are in the Storage Room: What direction do you want to go? (North, East, South, West): ')

while direction == 'North':
    print('You can not go that way!')
    if direction == 'South':
        room2()
        print('You are now back in the Gallery!')
    elif direction == 'East':
        room7()
        print('You are now in the Utility Closet!')
    elif direction == 'West':
        print('You can not go that way!')
    break

room7 = input('You are in the Utility Closet: What direction do you want to go? (North, East, South, West): ')

while direction == 'North':
    print('You can not go that way!')
    if direction == 'South':
        print('You can not go that way!')
    elif direction == 'East':
        print('You can not go that way!')
    elif direction == 'West':
        room6()
        print('You are now back in the Storage Room!')
    break

room8 = input('Oh no! Its the security Guards! You have been caught!')
print('End')
