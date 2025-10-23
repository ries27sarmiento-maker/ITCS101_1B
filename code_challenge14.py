anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").lower()
    if anime == 'exit':
        print("You have exited the anime entry program.")
        break
    else:
        anime_list += [anime]
        print(f" '{anime}'has been added to your anime list \n")

print("Your anime list includes:")
for z in anime_list:
    print(f"- {z}")
