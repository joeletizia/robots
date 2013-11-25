import math
import rg

class Robot:
    game = None
    def act(self, game):
        self.game = game
        if self.space_occupied(self.where_i_should_move()) or self.location == rg.CENTER_POINT:
            enemy_location = self.closest_adjacent_enemy()
            if enemy_location:
                print("Robot {0}:Trying to attack. Location:{1}".format(str(self.location), str(enemy_location)))
                return self.attack(enemy_location)
            else:
                print("Robot {0}:No enemies around; guarding.".format(self.location))
                return self.guard()
        else:
            print("Robot {0}: Not in position; moving to {1}.".format(self.location, self.where_i_should_move()))
            return self.move(self.where_i_should_move())
    def closest_adjacent_enemy(self):
        enemies = []
        if self.enemy_in_space(self.right()):
            enemies.append(self.right())
        if self.enemy_in_space(self.left()):
            enemies.append(self.left())
        if self.enemy_in_space(self.up()):
            enemies.append(self.up())
        if self.enemy_in_space(self.down()):
            enemies.append(self.down())
        enemies.sort(key=lambda x: self.game.robots[x].hp)
        if enemies:
            return enemies[0]
        else:
            return None
    def right(self):
        return (self.location[0]+1, self.location[1])
    def left(self):
        return (self.location[0]-1, self.location[1])
    def up(self):
        return (self.location[0], self.location[1]-1)
    def down(self):
        return (self.location[0], self.location[1]+1)
    def guard(self):
        return ['guard']
    def attack(self, location):
        return ['attack', location]
    def move(self, location):
        return ['move', location]
    def where_i_should_move(self):
        if self.location == rg.CENTER_POINT:
            return rg.CENTER_POINT
        dist_tuple = self.distance_to_center()
        if math.fabs(dist_tuple[0]) >= math.fabs(dist_tuple[1]):
            if dist_tuple[0] > 0:
                return self.right()
            else:
                return self.left()
        else:
            if dist_tuple[1] > 0:
                return self.down()
            else:
                return self.up()
    def distance_to_center(self):
        return (rg.CENTER_POINT[0] - self.location[0],
                rg.CENTER_POINT[1] - self.location[1])
    def space_occupied(self, location):
        if self.game.robots.get(location, False):
            return True
        else:
            False
    def enemy_in_space(self, location):
        if self.space_occupied(location):
            return self.game.robots[location].player_id != self.player_id
        else: 
            False
    def ally_in_space(self, location):
        if self.space_occupied(location):
            return self.game.robots[location].player_id == self.player_id
        else:
            False
