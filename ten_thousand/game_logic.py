from random import randint
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(dice_numb):
        return tuple(randint(1, 6) for _ in range(dice_numb))

    @staticmethod
    def calculate_score(dice_roll):
        dice_count = Counter(dice_roll)

        score_dict = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

        score = 0

        # calculate straight
        if len(dice_count) == 6:
            return 1500

        # calculate triple doubles
        if len(dice_count) == 3 and all(value == 2 for value in dice_count.values()):
            return 1500

        # score based on face value
        for face_value, count in dice_count.items():
            if face_value == 5 and count <= 2:
                score += 50 * count
            elif face_value == 1 and count <= 2:
                score += 100 * count
            elif face_value == 1 and count == 3:
                score += 1000
            elif count == 3:
                score += score_dict[face_value]
            elif count == 4:
                score += score_dict[face_value] * 2
            elif count == 5:
                score += score_dict[face_value] * 3
            elif count == 6:
                score += score_dict[face_value] * 4

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
