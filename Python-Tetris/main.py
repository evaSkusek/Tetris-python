import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# Nastavi pisavo
title_font = pygame.font.Font(None, 40)

# Pripravi tekst za izpis
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Okvirji za prikaz točk in naslednjega bloka
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Ustvari glavno okno
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Ura za nadzor hitrosti igre
clock = pygame.time.Clock()

# Ustvari novo igro
game = Game()

# Ustvari dogodek, ki se bo sprožil vsakih 200 ms (za premik bloka navzdol)
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Glavna zanka igre
while True:
	for event in pygame.event.get():
		# Če uporabnik zapre okno
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# Če je pritisnjena tipka
		if event.type == pygame.KEYDOWN:
			# Če je konec igre, jo ponastavi ob naslednjem pritisku tipke
			if game.game_over == True:
				game.game_over = False
				game.reset()

			# Premiki in rotacije samo, če igra še ni končana
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)  # Dodatna točka za ročni spust
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()

		# Premik bloka navzdol vsakih 200 ms (glede na časovnik)
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	# --- RISANJE NA ZASLON ---
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.dark_blue)  # Ozadje

	# Naslova
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))

	# Če je igre konec, izpiši obvestilo
	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	# Okvir in vrednost za točke
	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, 
		centery=score_rect.centery))

	# Okvir za naslednji blok
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

	# Nariši mrežo in trenutni blok
	game.draw(screen)

	# Posodobi zaslon
	pygame.display.update()
	clock.tick(60)  # Omeji na 60 FPS
