import random

# Phrases for "loves me" and "loves me not"
data = {
    "loves me": [
        "do you want some food",
        "you're so nice",
        "I got you some food",
        "I like your hair",
        "You looked nice today",
        # Add more phrases here
    ],
    "loves me not": [
        "I didn't have the time",
        "Can you get your own food",
        "You'll have to get your own food",
        "Do it yourself",
        # Add more phrases here
    ]
}

def pick_random_phrase(label):
    return random.choice(data[label])

def main():
    petals = 10  # Number of petals (you can adjust this)
    for i in range(petals):
        if i % 2 == 0:
            print(f"Loves me: {pick_random_phrase('loves me')}")
        else:
            print(f"Loves me not: {pick_random_phrase('loves me not')}")

if __name__ == "__main__":
    main()
