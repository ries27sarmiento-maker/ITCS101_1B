print("PARROT SIMULATOR - THE ECHO CHAMBER!")

parrot = input("What do you want your parrot say? -->")

times = int(input("How many times should the parrot say squackk?-->"))

print("🗣️LISTEN TO YOUR PARROT ")
for times in range(times):
	print(f"🦜SQUACKKK! {parrot}")