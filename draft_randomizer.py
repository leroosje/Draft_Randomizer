import string
import random
import hashlib
import time

class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def decide_pick_order(seed):
    sha = hashlib.sha256()
    sha.update(seed.encode("utf-8"))
    order_phrase = str(int(str(sha.hexdigest()), 16)) #IM SORRY
    order_phrase = order_phrase[(len(order_phrase) % 10):] #IM NOT SORRY
    step = int(len(order_phrase)/10)

    managers = [
        "Luke",
        "Steven",
        "Katie",
        "Gabriel",
        "Nicolas",
        "Nicole",
        "Abir",
        "Cory",
        "Ben",
        "Nat",
    ]

    positions = {}
    for i in range(len(managers)):
        curr = i*step
        positions[managers[i]] = int(order_phrase[curr:curr+step])
    
    sorted_positions = sorted(positions.items(), key=lambda item: item[1])
    sorted_managers = list(m[0] for m in sorted_positions)
    
    return {sorted_managers[i]: i+1 for i in range(len(sorted_managers))}
    
def verification():
    aggregate = {
        "Luke": [],
        "Steven": [],
        "Katie": [],
        "Gabriel": [],
        "Nicolas": [],
        "Nicole": [],
        "Abir": [],
        "Cory": [],
        "Ben": [],
        "Nat": []
    }

    iterations = 100000
    for i in range(iterations):
        seed = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(25))
        pick_order = decide_pick_order(seed)
        for m in pick_order:
            aggregate[m].append(pick_order[m])

    print("Draft picks should average to about 5.5:")
    for m in aggregate:
        print(f"{m} average draft pick: {sum(aggregate[m])/iterations}") #Output average draft pick per manager

def generate_final_pick_order(seed):
    sorted_managers = list(decide_pick_order(seed).keys())

    flavor_text = [
        "The pressure is on! Who are you taking first overall?",
        "First is worst, second is best! Am I right?",
        "They say third time's the charm!",
        "Fourth? Let them get the risky picks out of the way!",
        "You won't have to wait long for your next round pick!",
        "Make sure to snipe whoever fifth pick wants in the second round!",
        "Lucky number seven! Let's see how far luck will take you.",
        "Crazy eight, make some crazy picks!",
        "Mighty number nine! I hope your favorite will still be on the board.",
        "Tenth pick! Get some mean round turner combos ready!"
    ]

    print(f"{bcolors.HEADER}WELCOME EVERYONE! LET'S GET THIS PICK ORDER GOING. THE FOLLOWING PHRASE WILL DECIDE YOUR FATE: {bcolors.WARNING}{seed}{bcolors.ENDC}\n")
    for i in range(len(sorted_managers)):
        print(f"DRAFT PICK {i+1} GOES TO...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(4)
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}{sorted_managers[i]}!{bcolors.ENDC}")
        time.sleep(1)
        print(f"{bcolors.OKCYAN}Congratulations {sorted_managers[i]}! {flavor_text[i]}{bcolors.ENDC}\n")
        time.sleep(8)

    print("The draft order has been decided! Congratulations and good luck to everyone!")

verification()
seed_phrase = "I LOVE FANTASY FOOTBALL" #TO BE PROVIDED AT ACTUAL RUNTIME
#generate_final_pick_order(seed_phrase)