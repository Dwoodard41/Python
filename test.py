
import wordle_lists
import pygame

pygame.init()

size = screen_width, screen_height = 772, 1258
screen = pygame.display.set_mode(size)

# ########################## COLORS
neutral = r, g, b = 211, 211, 211
darkgrey = r, g, b = 105, 105, 105
green = r, g, b = 114, 245, 105
yellow = r, g, b = 226, 245, 105
black = r, g, b = 0, 0, 0

# ########################## TITLE DIMENSIONS
title_left_border = 50
title_right_border = title_left_border
title_rect_h = 100
title_rect_w = screen_width - title_left_border - title_right_border
title_rect_x = title_left_border
title_rect_y = 25
title_coords = title_rect_x, title_rect_y, title_rect_w, title_rect_h
title_rect_text_dest = title_rect_x + 50, title_rect_y + 25
title_rect_text = "WORDLE"

# ########################## PLAY AREA DIMENSIONS
rect_left_border = 136
initial_rect_x = 136
initial_rect_y = 150
initial_rect_w = 90
initial_rect_h = 90
space_between_rect_x = 10
space_between_rect_y = 20
initial_rect = initial_rect_x, initial_rect_y, initial_rect_w, initial_rect_h

# ########################### ALPHABET KEY DIMENSIONS
alpha_left_border = 54
initial_alpha_x = alpha_left_border
initial_alpha_y = screen_height - 200
initial_alpha_w = 39
initial_alpha_h = 39
space_between_alpha_x = 13
space_between_alpha_y = 13


class PlayerCell:
    # x and y represent two integers used to index the array of player cells in the wordle game
    def __init__(self, x, y):
        self.name = "cell" + str(x) + str(y)




def build_screen():
    pygame.init()

    background = pygame.transform.rotate(pygame.image.load("images/background.jpg"), 90).convert_alpha()
    screen.blit(background, (0, 0))

    # This displays the title
    title = pygame.draw.rect(screen, neutral, title_coords, width=0, border_radius=10)
    title = pygame.draw.rect(screen, black, title_coords, width=2, border_radius=10)
    title_center = title.center
    title_text = pygame.font.SysFont('arial', 50).render(title_rect_text, True, black)

    title_text = screen.blit(title_text, (title.centerx - 100, title.centery - 25))


    # This displays the playing area
    for a in range(0, 6):
        for b in range(0, 5):
            x = initial_rect_x + (b * (space_between_rect_x + initial_rect_w))
            y = initial_rect_y + (a * (space_between_rect_y + initial_rect_h))
            w = initial_rect_w
            h = initial_rect_h
            loc = x, y



            rect = pygame.draw.rect(screen, neutral, (x, y, w, h), width=0, border_radius=10)
            rect = pygame.draw.rect(screen, black, (x, y, w, h), width=2, border_radius=10)

            rect = PlayerCell(a, b)
            print(rect.name)

            player_cells = {"cell": name, "loc": loc}

    # This displays the available letter spaces
    letter_index = 0
    characters = wordle_lists.LEGAL_CHARACTERS

    while letter_index < len(characters):
        for a2 in range(0, 2):
            for b2 in range(0, 13):
                x2 = initial_alpha_x + (b2 * (space_between_alpha_x + initial_alpha_w))
                y2 = initial_alpha_y + (a2 * (space_between_alpha_y + initial_alpha_h))
                w2 = initial_alpha_w
                h2 = initial_alpha_h

                rect = pygame.draw.rect(screen, neutral, (x2, y2, w2, h2), width=0, border_radius=4)
                rect = pygame.draw.rect(screen, black, (x2, y2, w2, h2), width=2, border_radius=4)

                rect_font = pygame.font.SysFont('arial', 30).render(characters[letter_index].upper(),
                                                                    True,
                                                                    black)

                font_dest_left = rect.left + 10
                font_dest_top = rect.top
                font_dest = font_dest_left, font_dest_top

                screen.blit(rect_font, font_dest)

                letter_index = letter_index + 1

    pygame.display.flip()


def update_play_box(key_pressed):

    print(f"The '{key_pressed}' key was just pressed.")

def play_wordle():
    running = True
    screen_built = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keystroke = pygame.key.name(event.key)
                update_play_box(keystroke)

        if screen_built is False:
            build_screen()

        pygame.display.flip()

play_wordle()

print(player_cells)