import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, amount in kwargs.items():
            for _ in range(amount):
                self.contents.append(color)

    def draw(self, amount=1):
        ball_chosen_list = []
        if amount > len(self.contents):
            ball_chosen_list = self.contents.copy()
            self.contents.clear()
            return ball_chosen_list
        else:
            for ball in range(0,amount):
                chosen_ball_random = random.randint(0,(len(self.contents)-1))
                ball_chosen = self.contents.pop(chosen_ball_random)
                ball_chosen_list.append(ball_chosen)
        return ball_chosen_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0

    expected_balls_list = []

    for color, amount in expected_balls.items() :
        for _ in range(amount):
            expected_balls_list.append(color)
        
    for x in range(num_experiments):
        expected_balls = expected_balls_list.copy()
        hat_copy = hat.contents.copy()
        balls_chosen = hat.draw(num_balls_drawn)

        for ball in balls_chosen:
            for expected_ball in expected_balls:
                if ball == expected_ball:
                    expected_ball_chosen = expected_balls.index(expected_ball)
                    del expected_balls[expected_ball_chosen]
                    break
        if not expected_balls:
            M += 1

        hat.contents = hat_copy.copy()

    prabability = M / num_experiments

    return round(prabability,3)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
