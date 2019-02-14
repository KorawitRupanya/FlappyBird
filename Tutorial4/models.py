from coldetect import check_player_pillar_collision
from random import randint

class Player:
    GRAVITY = 1
    STARTING_VELOCITY = 15
    JUMPING_VELOCITY = 15

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vy = Player.STARTING_VELOCITY
    
    def jump(self):
        self.vy = Player.JUMPING_VELOCITY
 
    def update(self, delta):
        self.y += self.vy
        self.vy -= Player.GRAVITY

class PillarPair:
    PILLAR_SPEED = 5
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        self.x -= PillarPair.PILLAR_SPEED
        if self.x < -40 :
                self.x = self.world.width+40
                self.random_position_y()
        pass
        
    

    def hit(self, player):
        return check_player_pillar_collision(player.x, player.y,
                                             self.x, self.y)
 
    def random_position_y(self):
        self.y = randint(100,450)

class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2
    STATE_DEAD = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self, width // 2, height // 2)
        self.state = World.STATE_FROZEN
        self.pillar_pair = PillarPair(self, width - 100, height // 2)
        self.score = 0
 
    def update(self, delta):
        if self.state in [World.STATE_FROZEN, World.STATE_DEAD]:
            return
 
        self.player.update(delta)
        self.pillar_pair.update(delta)
 
        if self.pillar_pair.hit(self.player):
            self.die()
    
    def on_key_press(self, key, key_modifiers):
        self.player.jump()
    
    def start(self):
        self.state = World.STATE_STARTED
 
    def freeze(self):
        self.state = World.STATE_FROZEN     
 
    def is_started(self):
        return self.state == World.STATE_STARTED

    def die(self):
        self.state = World.STATE_DEAD
 
    def is_dead(self):
        return self.state == World.STATE_DEAD
