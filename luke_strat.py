import math
import rg

class Robot:
    game = None
    def act(self, game):
        self.game = game
        enemy_location = self.closest_adjacent_enemy()
        if 'spawn' in rg.loc_types(self.location):
            destination = rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))[0]
            print("Robot {0}: In a spawn. Moving to {1}".format(str(self.location), str(destination)))
            return self.move(rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))[0])
        elif enemy_location:
            print("Robot {0}:Trying to attack. Location:{1}".format(str(self.location), str(enemy_location)))
            return self.attack(enemy_location)
        else:
            enemies = []
            for loc, robot in game.robots.items():
                if robot.player_id != self.player_id:
                    enemies.append(loc)
            enemies.sort()
            if rg.toward(self.location, enemies[0]) == self.location:
                print("Robot {0}:Don't want to collide; guarding.".format(self.location))
                return self.guard()
            else:
                destination = rg.toward(self.location, enemies[0])
                print("Robot {0}: Not in position; moving to {1}.".format(self.location, destination))
                return self.move(rg.toward(self.location, enemies[0]))
    def guard(self):
        return ['guard']
    def attack(self, location):
        return ['attack', location]
    def move(self, location):
        return ['move', location]
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
    def enemy_in_space(self, location):
        if self.space_occupied(location):
            return self.game.robots[location].player_id != self.player_id
        else: 
            False
    def right(self):
        return (self.location[0]+1, self.location[1])
    def left(self):
        return (self.location[0]-1, self.location[1])
    def up(self):
        return (self.location[0], self.location[1]-1)
    def down(self):
        return (self.location[0], self.location[1]+1)
    def space_occupied(self, location):
        if self.game.robots.get(location, False):
            return True
        else:
            False
