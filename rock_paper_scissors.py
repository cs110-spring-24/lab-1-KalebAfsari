import random

cpu = random.randint(1,3)

user = input("Enter rock, paper, or scissors: ")


if user == "rock":
	if cpu == 1:
		print("Tie")
	elif cpu == 2:
		print("You lose, rock loses to paper")
	else:
		print("You win, rock beats scissors")

elif user == "paper":
	if cpu == 1:
		print("You win, paper beats rock")
	elif cpu == 2:
		print("Tie")
	else:
		print("You lose, paper loses to scissors")

elif user == "scissors":
	if cpu == 1:
		print("You lose, scissors loses to rock")
	elif cpu == 2:
		print("You win, scissors beats paper")
	else:
		print("Tie")

else:
	print("Run the code again and use all lowercase letters. ")
