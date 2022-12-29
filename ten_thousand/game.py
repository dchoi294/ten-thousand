from game_logic import GameLogic

on_off = True


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user = input("> ")

    if user == "n":
        global on_off
        on_off = False
        print("OK. Maybe another time")
    else:
        exit()


def play_dice():
    user_score = 0
    round_score = 0
    round_numb = 1
    current_dice = []
    dice_left = 6
    winning_score = 10000

    while on_off:

        user = input("> ")
        if user_score >= winning_score:
            print("You won!!")
            break

        if user == "q":
            print("Aww")
            exit()

        if user == "r":
            roll = GameLogic.roll_dice(dice_left)
            score = GameLogic.calculate_score(roll)
            print(f"Starting round {round_numb}")
            print(f"Rolling {dice_left-len(current_dice)} dice...")
            print(f"*** {current_dice} ***")

        if score == 0:
            round_score = 0
            print("Farkled!")
        else:
            print("Enter dice to keep, or (q)uit:")

            user = input("> ")
            if user == "q":
                print(f"Thanks for playing. You earned {score} points")
                break
            for dice in user:
                current_dice.append(int(dice))

            round_score += roll
            print(f"You have {round_score} unbanked points and {6 - len(current_dice)} dice remaining")
            print(f"(r)oll again, (b)ank your points or (q)uit:")
            user = input("> ")
            if user == "b":
                print(f"You banked {round_score} points in round {round_numb}")
                score += round_score
                print(f"Total score is {score} points")
                round_score = 0
                current_dice = []
                round_numb += 1


if __name__ == "__main__":
    intro()
    play_dice()
