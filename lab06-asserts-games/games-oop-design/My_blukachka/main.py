import game

###############################################################
church = game.Building("Church")
sheptytsky = game.Building("Sheptytsky Center")
academic = game.Building("Academic Building")
space = game.Building("IT-space")
collegium = game.Building("Collegium")

church.link_building(sheptytsky)
sheptytsky.link_building(church)
sheptytsky.link_building(collegium)
sheptytsky.link_building(academic)
academic.link_building(space)
academic.link_building(sheptytsky)
academic.link_building(collegium)
space.link_building(academic)
collegium.link_building(sheptytsky)
collegium.link_building(academic)

###############################################################
librarian = game.Enemy("Angry Librarian")
librarian.set_conversation("WHERE ARE YOUR READER'S TICKET??")
librarian.set_weakness("reader's ticket")
sheptytsky.set_character(librarian)

chef = game.Enemy("Greedy Chef")
chef.set_conversation("You don't have enough money or discount?.. It's your problem, loser))")
chef.set_weakness("local card")
academic.set_character(chef)

teacher = game.Friend("Teacher")
teacher.set_conversation("Don't forget your books.")
space.set_character(teacher)

conscience = game.Friend("Your Conscience")
conscience.set_conversation("I hope you'll not spend so much time playing video games")
collegium.set_character(conscience)

###############################################################
ticket = game.Item("reader's ticket")
ticket.set_description("Without Reader's Ticket you will be in Black List of Library Legion")
academic.set_item(ticket)

local = game.Item("local card")
local.set_description("You'll not be able to get Trapezna's Treasure without Local Card")
sheptytsky.set_item(local)

books = game.Item("books")
books.set_description("Reading books, you understand the wisdom of ancestors")
space.set_item(books)

###############################################################
current_building = church
backpack = []

dead = False

while dead == False:

    print("\n")
    current_building.get_details()

    inhabitant = current_building.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_building.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    builds = [church, sheptytsky, academic, space, collegium]
    buildings = {building.building: building for building in builds}
    if command in buildings:
        if command != 'Collegium':
            current_building = current_building.move(command)
        else:
            if 'books' in backpack and inhabitant.get_defeated() == 2:
                print("Game Complete")
                dead = True
            elif 'books' in backpack and inhabitant.get_defeated() != 2:
                print("You forgot to complete librarian and chef")
            elif 'books' not in backpack and inhabitant.get_defeated() == 2:
                print("Don't forget your book... It's not a good idea")
            else:
                print("WHERE ARE YOUR BOOKS AND COMPLETED ENEMIES??")


    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "interact":
        if inhabitant is not None:
            if inhabitant.agra == 'enemy':
                # Fight with the inhabitant, if there is one
                print("What will you interact with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.interact(fight_with) == True:
                        print("Hooray, you won the fight!")
                        inhabitant.add_defeat()
                        backpack.remove(fight_with)
                        current_building.character = None
                    else:
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("teacher")
        else:
            print("There is no one here to fight with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_building.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == 'stats':
        print(backpack)
        print(game.Enemy('stats').get_defeated())
    else:
        print("I don't know how to " + command)