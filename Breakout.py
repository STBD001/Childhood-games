import pygame

def start_breakout(screen=None, font=None):
    if screen is None:
        pygame.init()
        window_width = 800
        window_height = 600
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Breakout Game")

    if font is None:
        font = pygame.font.Font(None, 25)

    window_width, window_height = screen.get_size()

    platform_width = 100
    platform_height = 10
    platform_speed = 2
    ball_speedX = 0.5
    ball_speedY = 0.5
    radius = 10
    ball_x = 300
    ball_y = 500
    obstacle_width = 50
    obstacle_height = 20
    bricks = []
    score = 0

    White = (255, 255, 255)
    Blue = (0, 84, 252)
    Red = (245, 0, 0)
    Green = (0, 255, 0)

    Win_text = font.render("You win!", True, Red)
    Lose_text = font.render("You Lose!", True, Red)

    platform_x = (window_width - platform_width) // 2
    platform_y = window_height - platform_height - 10

    def draw_platform(x, y):
        position = (x, y, platform_width, platform_height)
        pygame.draw.rect(screen, Green, position)

    def draw_ball(x, y):
        pygame.draw.circle(screen, Red, (x, y), radius)

    def create_obstacles():
        nonlocal bricks
        num_columns = 14
        num_rows = 5
        x_start = 10
        y_start = 50
        gap = 5

        for row in range(num_rows):
            for col in range(num_columns):
                x_position = x_start + col * (obstacle_width + gap)
                y_position = y_start + row * (obstacle_height + gap)
                brick_rect = pygame.Rect(x_position, y_position, obstacle_width, obstacle_height)
                bricks.append(brick_rect)

    def draw_obstacles():
        for brick in bricks:
            pygame.draw.rect(screen, Blue, brick)

    create_obstacles()

    running = True
    win = False
    lose = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform_x -= platform_speed
        if keys[pygame.K_RIGHT]:
            platform_x += platform_speed

        if platform_x < 0:
            platform_x = 0
        if platform_x > window_width - platform_width:
            platform_x = window_width - platform_width

        ball_x += ball_speedX
        ball_y += ball_speedY

        if ball_x - radius < 0 or ball_x + radius > window_width:
            ball_speedX = -ball_speedX
        if ball_y - radius < 0:
            ball_speedY = -ball_speedY
        if ball_y + radius > window_height:
            lose = True
            running = False

        ball_rect = pygame.Rect(ball_x - radius, ball_y - radius, radius * 2, radius * 2)
        platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)

        if ball_rect.colliderect(platform_rect):
            ball_speedY = -ball_speedY
            ball_y = platform_y - radius

        for brick in bricks[:]:
            if ball_rect.colliderect(brick):
                ball_speedY = -ball_speedY
                bricks.remove(brick)
                score += 1
                break

        if len(bricks) == 0:
            win = True
            running = False

        screen.fill(White)
        draw_platform(platform_x, platform_y)
        draw_ball(ball_x, ball_y)
        draw_obstacles()

        pygame.display.update()

    if win:
        screen.fill(White)
        screen.blit(Win_text, (window_width//2 - Win_text.get_width()//2, window_height//2 - Win_text.get_height()//2))
    elif lose:
        screen.fill(White)
        screen.blit(Lose_text, (window_width//2 - Lose_text.get_width()//2, window_height//2 - Lose_text.get_height()//2))

    pygame.display.update()
    pygame.time.wait(900)

    if screen.get_init():
        pygame.quit()

    return win

if __name__ == "__main__":
    start_breakout()
