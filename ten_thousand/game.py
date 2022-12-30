from game_logic import GameLogic

round_score = 0
round_count = 1
count = 1
user_score = 0
dice_left = 6
winning_score = 10000
bank = 0
current_dice = []


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user = input("> ")

    if user == "n":
        global on_off
        on_off = False
        print("OK. Maybe another time")
    else:
        play_dice()


def default_play(numb):
    return GameLogic.roll_dice(numb)


def check_zilch(check):
    check = GameLogic.calculate_score(check)
    if check == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

        global user_score
        global bank
        global round_count
        global current_dice

        bank = 0
        print(f"You banked {bank} in round {round_count}")
        print(f"Total score is {user_score} points")

        round_count += 1
        play_dice(dice_left)


def bank_score():
    global user_score
    global bank
    global dice_left
    global round_count
    global round_score
    global current_dice

    user_score += bank
    print(f"You banked {bank} in round {round_count}")
    print(f"Total score is {user_score} points")

    bank = 0
    round_count += 1
    dice_left = 6
    current_dice = []
    round_score = 0
    play_dice(dice_left)


def play_dice(play=default_play):

    global user_score
    global round_count
    global count
    global round_score
    global dice_left
    global current_dice

    if round == round_count:
        print(f"Starting round {round_count}")
        round_count += 1

    while True:

        print(f"Rolling {dice_left - len(current_dice)} dice...")
        roll = play(6 - len(current_dice))
        playing = GameLogic.roll_dice(roll)
        roll_list = []
        roll_str = ""
        for i in roll:
            roll_list.append(i)
            roll_str += str(i) + " "
        print(f"*** {roll_str} ***")

        check_zilch(tuple(roll_list))

        print(f"Enter dice to keep, or (q)uit:")
        user = input("> ")
        if user == "q":
            print(f"Thanks for playing. you earned {user_score} points")
            quit()
        else:
            while GameLogic.validate_keepers(roll_list, [int(i) for i in user]) is False:
                print("Cheater!!! Or possibly you made a typo. Try again")
                print(f"*** {roll_str}***")
                print("Enter dice to keep, or (q)uit:")
            for numb in user:
                current_dice.append(int(numb))
            round_score += GameLogic.calculate_score(tuple(current_dice))

            if len(current_dice) == 6:
                print("HOT DICE, you get to roll 6 new ones")
                current_dice = []

            print("(r)oll again, (b)ank your points or (q)uit:")
            user = input("> ")

            if user == "b":
                bank_score()

            if user == "q":
                print(f"Thanks for playing. you earned {user_score} points")
                quit()

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
    intro()

