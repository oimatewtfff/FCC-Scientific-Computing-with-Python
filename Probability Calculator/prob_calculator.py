import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            for i in range(count):
                self.contents.append(str(color))

    def draw(self, count):
        remove = []
        if count > len(self.contents):
            return self.contents
        for i in range(count):
            remove.append(self.contents.pop(self.contents.index(random.choice(self.contents))))
        return remove


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        actual = copy.deepcopy(hat).draw(num_balls_drawn)
        for key in expected_balls.keys():
            if actual.count(key) < expected_balls[key]:
                count -= 1
                break
    return count / num_experiments + 1
