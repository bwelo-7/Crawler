import pygame
import heapq

from stuff import tile_size

game_map = [
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"x------xxxx---------xxxx-----------xxxx----------x",
"x------xxxx---------xxxx-----------xxxx----------x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x----------------------------------------xxxx----x",
"x----------------------------------------xxxx----x",
"x------xxxx---------xxxx----------------xxxx-----x",
"x------xxxx---------xxxx----------------xxxx-----x",
"x------xxxx---------xxxx-------------------------x",
"xxxxxxxxxxxx--------xxxx-------------------------x",
"x----------x--------xxxx----xxxxxxxxxxxxxxxxx----x",
"x----------x----------------x---------------x----x",
"x----------x----------------x---------------x---x",
"x----------xxxxxxxxxxxxx----x---------------x---x",
"x---------------------------x---------------x---x",
"x---------------------------x---------------x---x",
"x----------xxxxxxxxxxxxx----x---------------x---x",
"x----------x----------------x---------------x---x",
"x----------x----------------x---------------x---x",
"x----------x--------xxxx----xxxxxxxxxxxxxxxxx---x",
"xxxxxxxxxxxx--------xxxx------------------------x",
"x------xxxx---------xxxx------------------------x",
"x------xxxx---------xxxx----------------xxxx----x",
"x------xxxx---------xxxx----------------xxxx----x",
"x----------------------------------------xxxx----x",
"x----------------------------------------xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]

# Convert from strings to lists:
game_map = [list(row) for row in game_map]



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((105, 95, 110))
        self.rect = self.image.get_rect(topleft=(x, y))


class Loadmap:
    def __init__(self, game_map, tile_size):
            self.walls = pygame.sprite.Group()


            for row_index, row in enumerate(game_map):
                for col_index, tile in enumerate(row):
                    if tile == 'x':
                        pixel_y = row_index * tile_size
                        pixel_x = col_index * tile_size
                        wall = Wall(pixel_x, pixel_y, tile_size)
                        self.walls.add(wall)




def wall_collisions(sprite, walls):
    sprite.rect.x += int(round(sprite.dx))
    hits = pygame.sprite.spritecollide(sprite, walls, False)
    for wall in hits:
        if sprite.dx > 0:
            sprite.rect.right = wall.rect.left
        elif sprite.dx < 0:
            sprite.rect.left = wall.rect.right
        sprite.dx = 0


    sprite.rect.y += int(round(sprite.dy))
    hits = pygame.sprite.spritecollide(sprite, walls, False)
    for wall in hits:
        if sprite.dy > 0:
            sprite.rect.bottom = wall.rect.top
        elif sprite.dy < 0:
            sprite.rect.top = wall.rect.bottom
        sprite.dy = 0




def get_walkable_grid(game_map):
    grid = []
    for row in game_map:
        grid_row = []
        for tile in row:
            if tile == 'x':  # wall
                grid_row.append(1)  # blocked
            else:
                grid_row.append(0)  # walkable
        grid.append(grid_row)
    return grid



def astar(start, goal, grid):
    width = len(grid[0])
    height = len(grid)

    def h(a, b):
        # Manhattan distance heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0 + h(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        neighbors = [
            (current[0] + dx, current[1] + dy)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]
        ]
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 0:
                tentative_g = g_score[current] + 1
                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = tentative_g
                    priority = tentative_g + h((nx, ny), goal)
                    heapq.heappush(open_set, (priority, tentative_g, (nx, ny)))
                    came_from[(nx, ny)] = current
    return []  # no path found


def pixel_to_grid(pos):
    x, y = pos
    return x // tile_size, y // tile_size

def grid_to_pixel(grid_pos):
    x, y = grid_pos
    return x * tile_size + tile_size//2, y * tile_size + tile_size//2
