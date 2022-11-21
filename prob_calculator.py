import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value      

    def draw(self, number):
        balls = []
        if number > len(self.contents):
            balls = random.sample(self.content, k=len(self.contents))
        else:
            balls = random.sample(self.contents, k=number)
        for b in balls:
            self.contents.remove(b)
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copy = copy.deepcopy(hat)
    exp_balls = []
    for key, value in expected_balls.items():
        exp_balls += value * [key]    
    M = 0
    for N in range(num_experiments):
        if num_balls_drawn > len(hat_copy.contents):
            drawn_balls = random.sample(hat_copy.contents, k=len(hat_copy.contents))
        else:
            drawn_balls = random.sample(hat_copy.contents, k=num_balls_drawn)
        coincidences = 0
        drawn_balls_copy = copy.deepcopy(drawn_balls)
        for color in exp_balls:
            if color in drawn_balls:
                drawn_balls.remove(color)
                coincidences += 1
        if coincidences == len(exp_balls):
            M += 1
    return M / num_experiments    
