WORDS = {
    "PAIR": 4,
    "HEAR": 4,
    "CHEAR": 5,
    "GRAPHIC": 7,
}
 
 
def main():
    count = 0
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
 
    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")
 
        if guess == "GRAPHIC":
            points = WORDS.pop(guess)
            WORDS.clear()
            print("You've won!")
            print(f"Total point so far: {points}")
        elif guess in WORDS.keys():
            count += points
            print(f"Good job! You scored {points} points.")
            print(f"Total point so far: {count}")
        else:
            print(f"Wrong word {guess}")
 
    print("That's the game!")
 
 
main()