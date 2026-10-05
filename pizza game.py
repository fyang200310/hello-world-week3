# PIZZA SHOP ADVENTURE
# Python 3
# You are the customer. Choose your meal and decide what to do when
# your drink spills. The chef will come over to ask how everything is.


player = {
    "name": "customer",
    "score": 0,
    "gems": 0,
    "order": {},
    "items": [],
    "location": "pizza shop",
}


def printGraphic(name):
    """Print recognizable ASCII art for the game scenes."""
    if name == "pizza":
        print(r"""
                         /\
                        /  \
                       /o  o\
                      /   o  \
                     /  o   o \
                    /__________\
                   /_\/_\/_\/\/_\
""")
        print("                 A SLICE OF PIZZA")

    elif name == "soda":
        print(r"""
                   ___________
                  / _________ \
                 /             \
                |               |
                |————————       |
                |        |      |
                |        |      |
                |        |      |
                |        |      |
                |————————       |
                |_______________|
                  
                 
""")
        print("                    .  .  .  .")

    elif name == "juice":
        print(r"""
                    _________
                   /         \
                  /           \
                 /~ ~~~~~~~~ ~ \
                 \             /
                  '-----------'
                       | |
                       | |
                       | |
                    / -    -\
                   /_________\
                  (___________)
""")
        print("                    STEMMED GLASS")

    elif name == "toy_car":
        print(r"""
                 ____________
            ____/_   _        \__
           /____|_| |_|___________\
           |                      |
           '----(O)-------- (O)---'
                    LITTLE TOY CAR
""")

    elif name == "gem":
        print(r"""
           ____      
          /\__/\     
         /_/  \_\    
         \ \__/ /    
          \/__\/ 
         +1 GEM!
""")

    elif name == "gift":
        print(r"""
                     _  _
                    ( \/ )
                     \  /
              .-----  \/ -----. 
              |       ||      |
              |=======||======|
              |       ||      |
              |       ||      |
              |       ||      |
              '---------------'
""")

    elif name == "mirror":
        print(r"""
                 .-------------.
                / .------------. \
               | |             |  |
               | |             |  |
               | |             |  |
               | '-------------'  |
                \       ||       /
                 '-----||||-----'
                       ||||
                       ||||
""")

    elif name == "spilled_drink":
        print(r"""
       

         _____       _____       _____       _____
        / ___ \     |  __ \     |  __ \     / ____|
       | |   | |    | |__) |    | |__) |   | (___
       | |   | |    |  ___/     |  ___/     \___ \
       | |___| |    | |         | |         ____) |
        \_____/     |_|         |_|        |_____/

             ~~~~~~~  (╥﹏╥)  ~~~~~~~
""")

    elif name == "chef":
        print(r"""
                           _________
                        .-'         '-.
                       /               \
                       |               |
                       |               |
                       '---------------'
                           ( o     o )
                            |   >   |
                         .--|_______|-.
                        /              \
                       /|              |\
                      / |              | \__
                        |______________|          
                           /      \                  
                          /        \
""")
        print("                   THE CHEF WALKS OVER")

def chooseFrom(prompt, options):
    """Keep asking until the player types one of the listed options."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("Please choose: " + " / ".join(options))


def rewardGem(task):
    print("\n" + task)
    input("Press enter to collect the gem > ")
    player["gems"] += 1
    print("A sparkling gem appears in my inventory!")
    printGraphic("gem")


def orderFood():
    print("\nMAIN QUEST: Choose something to make my long day better.")
    print("A server in a red apron slides a menu across the table.")
    print('Server: "Welcome! Our oven is working overtime today. What sounds good?"')
    print("The menu has two pizzas: cheese / pepperoni")
    pizza = chooseFrom("> ", ["cheese", "pepperoni"])
    player["order"]["pizza"] = pizza
    print("\nI order a " + pizza + " pizza. The server makes a little chef's-kiss gesture.")
    printGraphic("pizza")
    print('Server: "Would you like a drink with that?"')
    add_drink = chooseFrom("Order a drink? yes / no > ", ["yes", "no"])
    if add_drink == "yes":
        print("The drink menu has soda / juice")
        drink = chooseFrom("> ", ["soda", "juice"])
    else:
        drink = "water"
        print("I ask for water. The server brings a cool glass with a lemon slice.")
    player["order"]["drink"] = drink

    if drink != "water":
        print("\nThe server brings me a " + drink + ".")
        printGraphic(drink)
    print("\nThe pizza smells so good that my stomach growls loud enough to make the server laugh.")
    rewardGem("I placed my pizza and drink order")
    eat_now = chooseFrom("Eat while it is hot? yes / no > ", ["yes", "no"])
    if eat_now == "yes":
        print("I take a bite. The cheese stretches all the way to my nose!")
    else:
        print("I wait a moment, then take a careful bite. The crust is still warm and crisp.")


def spilledDrinkSideStory():
    print("\nSIDE QUEST: Clean up the spilled drink.")
    print("\nI take my first bite and enjoy the crispy, cheesy pizza.")
    input("Press enter to continue > ")
    print("I reach for my drink, but my sleeve catches the cup.")
    print("It tips over and spills across the table!")
    printGraphic("spilled_drink")
    print("Should I ask the server for help or clean it myself?")
    print("Options: tell server / clean it")
    choice = chooseFrom("> ", ["tell server", "clean it"])

    if choice == "tell server":
        print("I tell the server. They bring a napkin and help me clean up.")
        player["score"] += 1
    else:
        print("I get a napkin and clean the table myself. A kind customer helps!")
        player["score"] += 2
    rewardGem("I took care of the spilled drink")
    input("Press enter to continue > ")


def lostToySideStory():
    player["location"] = "dining room"
    print("\nAs the server wipes up the spilled drink, I hear a small sob nearby.")
    input("Press enter to look over > ")
    print("A little kid is searching under the next table, looking worried.")
    print('The kid sniffles, "My toy car rolled away. I cannot find it."')
    printGraphic("toy_car")
    choice = chooseFrom("Should I help look? yes / no > ", ["yes", "no"])

    if choice == "no":
        print("I ask the server to stay with the kid while I finish my meal.")
        print("The server kindly helps the kid search. I return to my table.")
        return False

    print("I get down on my knees and look around the dining room.")
    search = chooseFrom("Where should I check first? under booth / by counter > ",
                        ["under booth", "by counter"])
    if search == "under booth":
        print("I spot a little red wheel under a booth and reach for the toy car.")
    else:
        print("I ask the server at the counter. They point to the waiting bench.")
        print("The toy car is tucked beside the bench!")

    print("I return the car. The kid laughs with relief, and their parent thanks me.")
    player["items"].append("toy car")
    player["score"] += 2
    rewardGem("I helped the kid find the toy car")
    input("Press enter to return to my table > ")
    return True


def talkToChefSideStory():
    player["location"] = "table"
    print("\nBack at my table, I take another bite of pizza.")
    print("The kitchen door swings open. The chef walks over, holding a ladle.")
    printGraphic("chef")
    print('Chef: "I am checking on our guests. How is everyone enjoying the food?"')
    print("I can answer: delicious / suggestion")
    answer = chooseFrom("> ", ["delicious", "suggestion"])

    if answer == "delicious":
        print('I say, "It is delicious!" The chef smiles proudly.')
        player["score"] += 2
    else:
        print('I share a kind suggestion. The chef listens carefully and thanks me.')
        player["score"] += 1
    rewardGem("I shared my feedback with the chef")
    input("Press enter to hear what happens next > ")


def jukeboxMysterySideStory():
    print("\nJust as the chef heads back to the kitchen, the jukebox crackles to life by itself.")
    print("The lights flicker. A paper ticket slides out, covered in tiny music notes.")
    print('The ticket says: "I am red, round, and grow on a vine. I become pizza sauce. What am I?"')
    answer = chooseFrom("Choose an answer: tomato / mushroom / olive > ",
                        ["tomato", "mushroom", "olive"])

    if answer == "tomato":
        print("The jukebox flashes green and plays a cheerful victory tune!")
        print("A hidden drawer opens. A mysterious light glows inside!")
        player["items"].append("jukebox ticket")
        player["score"] += 2
        rewardGem("I solved the jukebox riddle")
        return True
    elif answer == "mushroom":
        print("The jukebox plays a spooky little tune. A mushroom-shaped sticker pops out!")
        print("The server laughs: " + '"Good topping, but tomatoes make the sauce."')
        print("The machine clicks shut. I keep the funny sticker, but the riddle remains unsolved.")
        player["items"].append("mushroom sticker")
        return False
    else:
        print("The jukebox starts playing lively Italian music!")
        print("A jar of olives rolls out of its secret slot, and I catch it just in time.")
        print("The server takes the jar back to the kitchen. The jukebox goes quiet again.")
        player["score"] += 1
        return False


def main():
    print("AFTER SCHOOL AT THE LITTLE PIZZA SHOP")
    player["name"] = input("What is your name? ").strip() or "customer"
    print("\nAfter a long day of classes, my backpack feels heavier than a pizza oven.")
    print("My stomach growls. I could go straight home, or treat myself to pizza.")
    treat = chooseFrom("Should I get a pizza treat? yes / no > ", ["yes", "no"])
    if treat == "no":
        print("I decide to head home and save my treat for another day.")
        print("As I walk away, I hear the shop bell ring behind me. Maybe next time!")
        return

    print("\nI spot a cozy pizza shop on the corner. Golden light glows in the window.")
    print("The smell of warm dough and tomato sauce follows me down the sidewalk.")
    enter_shop = chooseFrom("Should I go inside? yes / no > ", ["yes", "no"])
    if enter_shop == "no":
        print("I start walking home, but my stomach gives one enormous growl.")
        enter_shop = chooseFrom("Change my mind and go inside? yes / no > ", ["yes", "no"])
    if enter_shop == "no":
        print("I keep walking home, dreaming about extra cheese.")
        return

    print("\nI push open the door. A tiny bell jingles, and warm air smells like basil.")
    print("A server in a red apron welcomes me and shows me to a booth.")
    print("A sign reads: PIZZA QUEST — collect 3 gems to win a secret gift!")
    print('The server winks: "Finish quests around the shop and the prize is yours."')
    print("I sit down, curious about the strange sign and the glowing jukebox.")

    orderFood()
    spilledDrinkSideStory()
    lostToySideStory()
    talkToChefSideStory()
    jukeboxMysterySideStory()

    print("\nThe server counts my gems and smiles.")
    if player["gems"] >= 3:
        print("I completed the Pizza Quest! I win the shop's mysterious secret gift!")
        printGraphic("gift")
        input("Press enter to open my gift > ")
        print("Inside the box is an old silver mirror.")
        printGraphic("mirror")
        input("Press enter to look into the mirror > ")
        print("I look for my reflection, but the mirror shows only the empty shop behind me.")
        print("My heart pounds. I yelp and throw the mirror away!")
        input("Press enter to continue > ")
        print("The room spins. I suddenly wake up in my bed, still wearing my school clothes.")
        print("The pizza shop, the quests, and the strange mirror were all a dream!")
    else:
        print("I need more gems to win the secret gift. I promise to return and finish the quest.")
    print("\nThanks for playing, " + player["name"] + "!")
    if player["order"]:
        print("My order: " + player["order"]["pizza"] + " pizza and "
              + player["order"]["drink"] + ".")
    print("My kindness points: " + str(player["score"]))
    print("Gems collected: " + str(player["gems"]))
    if player["items"]:
        print("Items in my adventure bag: " + ", ".join(player["items"]))


if __name__ == "__main__":
    main()
