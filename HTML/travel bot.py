import re, random
from colorama import Fore,init 
init(autoreset=True)

destinations = {
    "beaches" : ["Bali","Maldives","Phuket"],
    "mountains" : ["Swiss Alps","Rocky mountains","Himalayas"],
    "cities" : ["Tokyo","Paris","New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs"
    "Why did the computer go to the doctor? It had a virus"
    "Why do travellers always fel warm? Because of all their hot spots"
]

def normalize(text):return re.sub(r"\s+","",text.strip().lower())
def recommend():
    pref=normalize(input(f"{Fore.CYAN} Travel Bot: Beaches , Mountains or Cities?\n{Fore.YELLOW} You:"))
    if pref in destinations :
        while True :
            suggestion = random.choice(destinations[pref])
            print(f"{Fore.GREEN}Travel how about {suggestion}?")
            ans = input(f"{Fore.GREEN}Travel Bot: Awesome! Enjoy {suggestion}!")
            if ans == "no":continue
            return
    else:
        print(f"{Fore.RED}Travel Bot: Sorry I don't have that type of destination")

def packing():
    loc = normalize(input(f"{Fore.CYAN}Travel Bot : Where to?\n {Fore.YELLOW}You:"))
    days = input(f"{Fore.CYAN}Travel Bot: How many days?\n{Fore.YELLOW}You: ")
    print(f"{Fore.GREEN}Travel Bot: Packing tips for {days} days in {loc}:")
    print("Pack vercetile cloths\n. Bring Chatgers and Adapters\n. Check the weather forcast")

def tell_joke(): print(f"{Fore.GREEN}TravelBot: {random.choice(jokes)}")
def show_help():
    print(f"""{Fore.MAGENTA}\nI can:
{Fore.GREEN}- Suggest travel spots ('recommendation')
- Offer packing tips ('packing')
- Tell a joke ('joke')
- Show this menu ('help')
- Exit ('exit')\n""")

# Main Chat
def chat():
    print(f"{Fore.CYAN}Hello! I’m TravelBot.")
    name = input(f"{Fore.YELLOW}Your name? ")
    print(f"{Fore.GREEN}Nice to meet you, {name}!")
    show_help()

    while True:
        user = normalize(input(f"{Fore.YELLOW}{name}: "))
        if "recommend" in user or "suggest" in user: recommend()
        elif "pack" in user: packing()
        elif "joke" in user or "funny" in user: tell_joke()
        elif "help" in user: show_help()
        elif "exit" in user or "bye" in user:
            print(f"{Fore.CYAN}TravelBot: Safe travels! Goodbye!")
            break
        else: print(f"{Fore.RED}TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
