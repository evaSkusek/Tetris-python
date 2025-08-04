from grid import Grid
from blocks import *
import random
import pygame

class Game:
	def __init__(self):
		# Ustvari mrežo in seznam vseh blokov
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		# Naključno izberi trenutni in naslednji blok
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0

		# Naloži zvoke
		self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

		# Predvajaj glasbo v ozadju
		pygame.mixer.music.load("Sounds/music.ogg")
		pygame.mixer.music.play(-1)

	def update_score(self, lines_cleared, move_down_points):
		# Posodobi točke glede na število počistjenih vrstic in premike navzdol
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points

	def get_random_block(self):
		# Če so vsi bloki že bili uporabljeni, jih ponovno dodaj
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		# Izberi naključni blok in ga odstrani iz seznama
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def move_left(self):
		# Premakni trenutni blok levo, če je to dovoljeno
		self.current_block.move(0, -1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		# Premakni trenutni blok desno, če je to dovoljeno
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	def move_down(self):
		# Premakni trenutni blok navzdol
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()

	def lock_block(self):
		# Zakleni trenutni blok v mrežo
		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id
		# Zamenjaj trenutni blok z naslednjim
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		# Počisti polne vrstice in posodobi rezultat
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.clear_sound.play()
			self.update_score(rows_cleared, 0)
		# Preveri, ali se nov blok lahko postavi, če ne, je igre konec
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		# Ponastavi igro
		self.grid.reset()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0

	def block_fits(self):
		# Preveri, ali trenutni blok ustreza v mreži
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True

	def rotate(self):
		# Zavrtite trenutni blok, če je to dovoljeno
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()
		else:
			self.rotate_sound.play()

	def block_inside(self):
		# Preveri, ali je trenutni blok znotraj meja mreže
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True

	def draw(self, screen):
		# Nariši mrežo in trenutni blok
		self.grid.draw(screen)
		self.current_block.draw(screen, 11, 11)

		# Nariši naslednji blok na desni strani (glede na ID bloka poravnaj pozicijo)
		if self.next_block.id == 3:
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 255, 280)
		else:
			self.next_block.draw(screen, 270, 270)
