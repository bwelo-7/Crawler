import math
from Bob import Thing  # or your Thing base class
from Walls import *
class Bill(Thing):
    def __init__(self, x, y, target=None):
        super().__init__(x, y, health=3)
        self.image.fill((255,0,0))
        self.target = target
        self.speed = 2
        self.path = []
        self.path_index = 0
        self.grid = get_walkable_grid(game_map)  # use your map

    def update(self, *args):
        if not self.target:
            return

        # Get start & goal on grid
        start = pixel_to_grid(self.rect.center)
        goal = pixel_to_grid(self.target.rect.center)

        # Calculate path
        self.path = astar(start, goal, self.grid)
        if not self.path:
            return

        # Move toward the next cell
        next_cell = self.path[0]
        target_x, target_y = grid_to_pixel(next_cell)

        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
