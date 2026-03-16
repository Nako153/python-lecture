import random
def main():
   print(sample())

moisture = random.randint(25, 40)

def sample():
    global moisture
    moisture = moisture - random.randint(1, 5)
    return moisture


if __name__ == "__main__":
    main()