from game_logic import GameLogic


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user = input("> ")

    if user == "n":
        print("OK. Maybe another time")
        quit()
    if user == "y":
        play_dice()


def start():
    score = 0
    round_number = 1
    while True:
        round_score = play_dice(round_number)
        if round_score == -1:
            break

        score += round_score
        print(f"You banked {round_score} points in round {round_number}")
        print(f"Total score is {score} points")
        round_number += 1

    print(f"Thanks for playing. You earned {score} points")


def default_play(numb):
    return GameLogic.roll_dice(numb)


def confirm_keepers(roll, roll_string):

    while True:
        print("Enter dice to keep, or (q)uit:")
        user = input("> ")

        if user == "q":
            return -1

        keep = [int(value) for value in user if value.isdigit()]

        if GameLogic.validate_keepers(roll, keep):
            return keep
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {roll_string} ***")


def play_dice(round_number, roller=default_play):
    dice_numb = 6
    round_score = 0
    print(f"Starting round {round_number}")
    while True:
        roll_string = ""
        roll = roller(dice_numb)
        for x in roll:
            roll_string += str(x) + " "
        print(f"Rolling {dice_numb} dice...")
        print(f"*** {roll_string} ***")

        if GameLogic.calculate_score(roll) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            round_score = 0
            return round_score

        keepers = confirm_keepers(roll, roll_string)
        if keepers == -1:
            return -1
        dice_numb -= len(keepers)
        if dice_numb == 0:
            dice_numb = 6
        round_score += GameLogic.calculate_score(tuple(keepers))

        print(f"You have {round_score} unbanked points and {dice_numb} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user = input("> ")
        if user == "b":
            return round_score
        if user == "q":
            return -1

        # if user == "r":
        #     roll = GameLogic.roll_dice(dice_left)
        #     score = GameLogic.calculate_score(roll)
        #     print(f"Rolling {dice_left-len(current_dice)} dice...")
        #     print(f"*** {current_dice} ***")
        #
        # else:
        #     print("Enter dice to keep, or (q)uit:")
        #
        #     user = input("> ")
        #     if user == "q":
        #         print(f"Thanks for playing. You earned {score} points")
        #         break
        #     for dice in user:
        #         current_dice.append(int(dice))
        #
        #     round_score += roll
        #     print(f"You have {round_score} unbanked points and {6 - len(current_dice)} dice remaining")
        #     print(f"(r)oll again, (b)ank your points or (q)uit:")
        #     user = input("> ")
        #     if user == "b":
        #         print(f"You banked {round_score} points in round {round_count}")
        #         score += round_score
        #         print(f"Total score is {score} points")
        #         round_score = 0
        #         current_dice = []
        #         print(f"Starting round {round_count}")


if __name__ == "__main__":
    rolls = []

    def mock_roller(num):
        return rolls.pop(0) if rolls else default_play(num)

    intro()
    play_dice()
