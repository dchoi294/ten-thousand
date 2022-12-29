from game_logic import GameLogic


def intro():
    print("10000 GAME, wanna roll some dices?")
    print("Press 'y' to start or 'n' to quit!")
    user = input("> ")

    if user == "y":
        print("Let's begin!")
    else:
        exit()


def play_dice():
    user_score = 0
    round_score = 0
    round_numb = 1
    current_dice = []
    dice_left = 6
    winning_score = 10000
    on_off = True

    while on_off:
        print("Press 'r' to roll the dices, 'b' to bank score and 'q' to quit.")
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
            print(f"Current Round: {round_numb}")
            print(f"Current score: {user_score}")
            print(f"Rolling {dice_left-len(current_dice)} dices...")
            round_numb += 1

        if score == 0:
            round_score = 0
            print("Farkled!")
        else:
            round_score += roll
            print(f"Banking points: {round_score}")
            print("Roll again? (r), Bank score? (b), Quit? (q)")

        if user == "b":
            score += round_score
            round_score = 0


if __name__ == "__main__":
    intro()
    play_dice()
