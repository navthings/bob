import math
import torch
import pygame

S = 800
P = 4000

# particles
pos = torch.rand(P, 3) * torch.tensor([0.5, 0.5, 0.8])


def project(pts, yaw, pitch):
    c = pts - 0.5
    x1 = c[:, 0] * math.cos(yaw) - c[:, 1] * math.sin(yaw)
    y1 = c[:, 0] * math.sin(yaw) + c[:, 1] * math.cos(yaw)
    z2 = y1 * math.sin(pitch) + c[:, 2] * math.cos(pitch)
    return S / 2 + x1 * S * 0.55, S / 2 - z2 * S * 0.55


pygame.init()
screen = pygame.display.set_mode((S, S))
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit

    screen.fill((6, 8, 12))
    sx, sy = project(pos, 0.7, 0.35)
    for x, y in zip(sx.tolist(), sy.tolist()):
        pygame.draw.circle(screen, (120, 190, 255), (int(x), int(y)), 2)

    pygame.display.flip()
    clock.tick(60)