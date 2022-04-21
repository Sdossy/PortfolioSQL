rooms = {
        'Main Hall': {'North': 'Northern Hall', 'South': 'Storage room', 'East': 'Eastern Hall', 'West': 'Western Hall'},
        'Northern Hall': {'South': 'Main Hall', 'East': 'NorthEastern Hall', 'West': 'NorthWestern Hall', 'item': 'Flashlight'},
        'Western Hall': {'East': 'Main Hall', 'North': 'NorthWestern Hall', 'South': 'Kitchen', 'item': 'Car Key'},
        'Eastern Hall': {'North': 'NorthEastern Hall', 'West': 'Main Hall', 'item': 'Gas Can'},
        'Storage room': {'North': 'Main Hall', 'West': 'Kitchen', 'item': 'Hammer'},
        'NorthEastern Hall': {'West': 'Northern Hall', 'South': 'Eastern Hall', 'item': 'Stool'},
        'NorthWestern Hall': {'South': 'Western Hall', 'East': 'Northern Room', 'item': 'Door Key'},
        'Kitchen': {'North': 'Western Hall', 'East': 'Eastern Hall', 'item': 'Maniac'}
        }

inventory = {}


def show_status(player, direction, inventory):

    current_room = player


    if direction in rooms[current_room].keys():
        current_room = rooms[current_room][direction]

    else:
        print("There is no room in that direction!")

 
    return current_room


def displayinstructions():

    print('Welcome to the Text Based Video Game')
    print('You have been taken by a maniac and you are now in an abandoned warehouse!')
    print('To move enter the commands: go North, go South, go East, go West')
    print('Also if you are done playing and want to exit type: Exit or exit to leave')
    print('Walk about and try not to get caught by the maniac!')
    print('Good luck!\n')



def main():
    displayinstructions()
    player = ["Main Hall", []]

    while True:

        current_room = player[0]

 
        print("You are in the", current_room)


        if player[0] == "Kitchen":

            if len(player[1]) == 0:
                print("The Maniac has gotten you!! How unfortunate! GAME OVER!")

          
            print("Thanks for playing!")
            break

        print("-" * 25)
        move = input("Enter your move (if you'd like to quit, type 'Exit'):")

        if move == 'Exit':
            print("Thanks for playing, come back soon!")
            quit() 
      
        if " " not in move:
            print("Invalid input! Try again in a different direction!")
            continue
     
        action, arg = move.split(" ", 1)
    
        if action == "go":
            player[0] = show_status(player[0], arg, inventory)

        else:
            print("Invalid input! Try again in a different direction!")


if __name__ == "__main__":
    main()
