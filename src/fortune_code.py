import random

def get_fortune():
    fortunes = [
        "You will have a great day today!",
        "A thrilling time is in your near future.",
        "Your hard work will soon pay off.",
        "Happiness is coming your way!",
        "Beware of what you wish for, it might just come true.",
        "An unexpected opportunity will present itself.",
        "A stranger will soon bring joy to your life.",
        "You will achieve your dreams one step at a time.",
        "Keep smiling; it suits you!",
        "Adventure is on your horizon."
    ]
    return random.choice(fortunes)

def main():
    username = input("Please enter your name: ")
    print(f"\nHello, {username}! Welcome to the Python Fortune Cookie!")
    print("Your fortune for today is:")
    print("-" * 40)
    print(get_fortune())
    print("-" * 40)

if __name__ == "__main__":
    main()
