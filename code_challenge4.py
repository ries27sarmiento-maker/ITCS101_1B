#print("Welcome!")
#("what is your name?:")

name = input("Welcome! What is your name sweetie? -->")
print("Hello!",name,  "nice to meet you")
choose_genre = input("What genre of book do you like? (Thriller/Comedy/Romance): ").lower()
choose_duration = input("How long should manga be? (short/medium/long): ").lower()
choose_decade = input("Which decade? (2010s/2020s): ").lower()

if choose_genre == 'thriller':
    if choose_decade == "2010s":
        if choose_duration == "short":
            print("I highly recommend Judge")
        elif choose_duration == "medium":
            print("I highly recommend Fort of Apocalypse")
        elif choose_duration == "long":
            print("I highly recommend Ajin: Demi Human")
    
    if choose_decade == "2020s":
        if choose_duration == "short":
            print("I highly recommend Mujirushi")
        if choose_duration == "medium":
             print("I highly recommend Fort of Fool Night")
        elif choose_duration == "long":
            print("I highly recommend Boy's Abyss")

if choose_genre == 'comedy':
    if choose_decade == "2010s":
        if choose_duration == "short":
            print("I highly recommend Ore no Kouhai ga Konnani Kawaii")
        elif choose_duration == "medium":
            print("I highly recommend Tonari no Seki-kun")
        elif choose_duration == "long":
            print("I highly recommend Gekkan Shoujo Nozaki-kun")
    
    if choose_decade == "2020s":
        if choose_duration == "short":
            print("I highly recommend Everyday Host")
        if choose_duration == "medium":
             print("I highly recommend Fort of Kanakana")
        elif choose_duration == "long":
            print("I highly recommend New Normal")

if choose_genre == 'romance':
    if choose_decade == "2010s":
        if choose_duration == "short":
            print("I highly recommend Ojousama no untenshu")
        elif choose_duration == "medium":
            print("I highly recommend Orange")
        elif choose_duration == "long":
            print("I highly recommend Ao haru Ride")    

    if choose_decade == "2020s":
        if choose_duration == "short":
            print("I highly recommend My Love Mix-Up!")
        if choose_duration == "medium":
             print("I highly recommend In the Clear Moonlit Dusk")
        elif choose_duration == "long":
            print("I highly recommend Ayakashi Triangle")

