def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in names:
        print(write_letter(names[i], "Princess Peach"))
  
def write_letter(reciver, sender):
    return f"""
    +-----------------------------------------+
    Dear {reciver}

    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM. 

    Sinclearly,
    {sender}
    +-----------------------------------------+
    """
main()
