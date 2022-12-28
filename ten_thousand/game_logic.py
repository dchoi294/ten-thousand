from random import randint
from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        dice_count = Counter(dice_roll).most_common()

        if dice_count[0][1] == 3:
            if dice_count[0][0] == 1:
                score += 1000
            else:
                score += dice_count[0][0] * 100
        if dice_count[0][1] == 4:
            if dice_count[0][0] == 1:
                score += 2000
            else:
                score += dice_count[0][0] * 200
        if dice_count[0][1] == 5:
            if dice_count[0][0] == 1:
                score += 4000
            else:
                score += dice_count[0][0] * 400
        if dice_count[0][1] == 6:
            if dice_count[0][0] == 1:
                score += 8000
            else:
                score += dice_count[0][0] * 800

        if len(dice_count) == 6:
            score += 1500

        if len(dice_count) == 3:
            if dice_count[2][1] == 2:
                score += 1500

        else:
            for dice in dice_count:
                if dice[0] == 5:
                    score += dice[1] * 50
            for dice in dice_count:
                if dice[0] == 1:
                    score += dice[1] * 100

        return score

    @staticmethod
    def roll_dice(dice_numb):
        return tuple(randint(1, 6) for _ in range(dice_numb))

