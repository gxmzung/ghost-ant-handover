import pygame
from simulation.environment import generate_base_stations
from simulation.uam import UAM

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghost Ant UAM Simulator")

font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

stations = generate_base_stations()
uam = UAM(position=(2, 2, 2), velocity=(1, 1, 0))
path = []

SCALE = 24

def to_screen(x, y):
    return int(x * SCALE + 40), int(HEIGHT - (y * SCALE + 40))

running = True
t = 0
current_cell = "BS-1"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if t < 30:
        pos = uam.move()
        path.append(pos)
        current_cell = f"BS-{min(9, max(1, t // 4 + 1))}"
        t += 1

    screen.fill((10, 15, 25))

    for bs in stations:
        x, y = to_screen(bs.x, bs.y)
        pygame.draw.polygon(screen, (80, 220, 120), [(x, y-12), (x-12, y+12), (x+12, y+12)])
        label = font.render(bs.cell_id, True, (220, 220, 220))
        screen.blit(label, (x + 10, y - 10))

    if len(path) > 1:
        points = [to_screen(p[0], p[1]) for p in path]
        pygame.draw.lines(screen, (80, 140, 255), False, points, 4)

    if path:
        x, y = to_screen(path[-1][0], path[-1][1])
        pygame.draw.circle(screen, (255, 70, 70), (x, y), 12)

    title = font.render("Ghost Ant UAM Simulation", True, (255, 255, 255))
    info = font.render(f"t={t} | Current Cell={current_cell} | Mode=Predictive Ghost Ant", True, (180, 220, 255))

    screen.blit(title, (30, 30))
    screen.blit(info, (30, 65))

    pygame.display.flip()
    clock.tick(2)

pygame.quit()
