import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Kecepatan Snake
SNAKE_SPEED = 15

# Inisialisasi Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
change_to = "RIGHT"
direction = change_to
score = 0

# Inisialisasi Food
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Posisi Awal Food
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]

# Fungsi untuk menampilkan pesan saat permainan berakhir
def message(text, color):
    font = pygame.font.Font('freesansbold.ttf', 30)
    mesg = font.render(text, True, color)
    mesg_rect = mesg.get_rect()
    mesg_rect.midtop = (WIDTH/2, HEIGHT/4)
    SCREEN.blit(mesg, mesg_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Validasi arah perubahan tidak boleh 180 derajat
    if change_to == "UP" and not direction == "DOWN":
        direction = "UP"
    if change_to == "DOWN" and not direction == "UP":
        direction = "DOWN"
    if change_to == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"

    # Menggerakkan Snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Tambahkan bagian Snake
    snake_body.insert(0, list(snake_pos))

    # Cek jika Snake makan Food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]

    food_spawn = True
    SCREEN.fill(WHITE)

    for pos in snake_body:
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(SCREEN, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        message("Game Over!", RED)
        pygame.display.update()
        pygame.quit()
        quit()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        message("Game Over!", RED)
        pygame.display.update()
        pygame.quit()
        quit()

    # Aturan permainan agar Snake menabrak dirinya sendiri
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            message("Game Over!", RED)
            pygame.display.update()
            pygame.quit()
            quit()

    # Update Skor
    font = pygame.font.Font('freesansbold.ttf', 20)
    score_font = font.render(f'Score: {score}', True, GREEN)
    score_rect = score_font.get_rect()
    score_rect.midtop = (WIDTH/10, 10)
    SCREEN.blit(score_font, score_rect)
    pygame.display.update()
    pygame.display.flip()

    # Kontrol kecepatan permainan
    pygame.time.Clock().tick(SNAKE_SPEED)

pygame.quit()
