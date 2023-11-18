import random

answers = ["rock", "scissors", "paper"]


def game(x, number):
    userCount = 0
    compCount = 0

    while number > 0:
        random_word = random.choice(x)
        userAnswer = input("rock, scissors, paper? ")

        if userAnswer == random_word:
            print("draw")

        if userAnswer == "rock" and random_word == "scissors":
            print(f"You have win. {userAnswer} beats {random_word}")
            userCount += 1

        if userAnswer == "rock" and random_word == "paper":
            print(f"You have lost. {random_word} beats {userAnswer}")
            compCount += 1

        if userAnswer == "scissors" and random_word == "rock":
            print(f"You have lost. {random_word} beats {userAnswer}")
            compCount += 1

        if userAnswer == "scissors" and random_word == "paper":
            print(f"You have win. {userAnswer} beats {random_word}")
            userCount += 1

        if userAnswer == "paper" and random_word == "rock":
            print(f"You have win. {userAnswer} beats {random_word}")
            userCount += 1

        if userAnswer == "paper" and random_word == "scissors":
            print(f"You have lost. {random_word} beats {userAnswer}")
            compCount += 1

        print("\n")

        number -= 1

    if userCount > compCount:
        print("You have won. You have {} vs {}".format(userCount, compCount))
    elif userCount < compCount:
        print("You have lost. You have {} vs {}".format(userCount, compCount))
    elif userCount == compCount:
        print("Draw. {} vs {}".format(userCount, compCount))


game(answers, 5)
