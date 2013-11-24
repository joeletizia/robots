import math
import rg

class Robot:
    def act(self, game):
        return self.move_to_center()
    def move_up(self):
        return ['move', (self.location[0],self.location[1]-1)]
    def move_down(self):
        return ['move', (self.location[0],self.location[1]+1)]
    def move_left(self):
        return ['move', (self.location[0]-1,self.location[1])]
    def move_right(self):
        return ['move', (self.location[0]+1,self.location[1])]
    def guard(self):
        return ['guard']
    def move_to_center(self):
        if self.location == rg.CENTER_POINT:
            return self.guard()
        dist_tuple = self.distance_to_center()
        if math.fabs(dist_tuple[0]) >= math.fabs(dist_tuple[1]):
            if dist_tuple[0] > 0:
                return self.move_right()
            else:
                return self.move_left()
        else:
            if dist_tuple[1] > 0:
                return self.move_down()
            else:
                return self.move_up()
    def distance_to_center(self):
        return (rg.CENTER_POINT[0] - self.location[0],
                rg.CENTER_POINT[1] - self.location[1])
