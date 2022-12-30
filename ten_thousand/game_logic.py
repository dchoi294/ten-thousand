from random import randint
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(dice_numb):
        return tuple(randint(1, 6) for _ in range(dice_numb))

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        dice_count = Counter(dice_roll).most_common()

        if not dice_count:
            return score

        # Straight
        if len(dice_count) == 6:
            score += 1500
            return score

        # Three pairs
        if len(dice_count) == 3 and dice_count[2][1] == 2:
            score += 1500
            return score

        # 3 ~ 6 of a kind
        if dice_count[0][1] >= 3:
            if dice_count[0][0] == 1:
                score += 1000 * (dice_count[0][1]-2)
            else:
                score += dice_count[0][0] * 100 * (dice_count[0][1]-2)
            dice_count = dice_count[1:]

            # Triple doubles
            if len(dice_count) == 1 and dice_count[0][1] == 3:
                if dice_count[0][0] == 1:
                    score += 1000
                else:
                    score += dice_count[0][0] * 100
        else:
            for dice in dice_count:
                if dice[0] == 1:
                    score += dice[1] * 100
                if dice[0] == 5:
                    score += dice[1] * 50

        return score

    @staticmethod
    def validate_keepers(numb, keeps):
        numb = list(numb)
        keeps = list(keeps)
        if keeps == []:
            return False
        for dice in keeps:
            is_inside = numb.count(dice)
            if is_inside > 0:
                numb.remove(dice)
            else:
                return False
        return True

        # if dice_count[0][1] == 3:
        #     if dice_count[0][0] == 1:
        #         score += 1000
        #     else:
        #         score += dice_count[0][0] * 100
        # if dice_count[0][1] == 4:
        #     if dice_count[0][0] == 1:
        #         score += 2000
        #     else:
        #         score += dice_count[0][0] * 200
        # if dice_count[0][1] == 5:
        #     if dice_count[0][0] == 1:
        #         score += 4000
        #     else:
        #         score += dice_count[0][0] * 400
        # if dice_count[0][1] == 6:
        #     if dice_count[0][0] == 1:
        #         score += 4000
        #     else:
        #         score += dice_count[0][0] * 800
        #
        # if len(dice_count) == 6:
        #     score += 1500
        #
        # if len(dice_count) == 3:
        #     if dice_count[2][1] == 2:
        #         score += 1500
        #
        # else:
        #     for dice in dice_count:
        #         if dice[0] == 5:
        #             score += dice[1] * 50
        #     for dice in dice_count:
        #         if dice[0] == 1:
        #             score += dice[1] * 100
        #
        # return score
        #
