import os

anonymous_name = "???"

print(f"{anonymous_name}: Thank you for meeting me here.")
anonymous_name = "Derek"

player_name = input(f"{anonymous_name}: My name is {anonymous_name}, what's yours? ").strip()
while len(player_name) < 1 or any(character.isdigit() for character in player_name):
	print(f"{anonymous_name}: There's no way you have no name or numbers in it, what's your real name?")
	player_name = input("What's your name? ").strip()


if "febit" in player_name.lower():
	print(f"{anonymous_name}: {player_name}.. Have we met before?")
elif "noah" in player_name.lower():
	print(f"{anonymous_name}: {player_name}?? You have the same name as my creator!")
else:
	print(f"{anonymous_name}: Thank you for joining me on this misson {player_name}, I'm so glad to have you here.")

player_age = input(f"{anonymous_name}: How old are you {player_name}? ")

while not player_age.isdigit():
	print(f"{anonymous_name}: That isn't an age {player_name}, please tell me your age.")
	player_age = input(f"{anonymous_name}: How old are you {player_name}? ")

player_age = int(player_age)

if player_age < 18:
	print(f"{anonymous_name}: You're too young to be a detective, get out of here!")
elif player_age > 85:
	print(f"{anonymous_name}: You're WAY to fucking old for this job, get out of here!")
else:
	input(f"{anonymous_name}: You're {player_age}? Great, let's get back into buisness. Press enter to continue. ")

os.system("cls")
print("Creator: I got bored, I don't wanna finish this game for now.")

# Made by LarvaMomkey.