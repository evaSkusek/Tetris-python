from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		# ID določa vrsto bloka (npr. I, J, L, itd.)
		self.id = id
		# Slovar, ki vsebuje pozicije celic za vsak rotacijski položaj
		self.cells = {}
		# Velikost posamezne celice v pikslih
		self.cell_size = 30
		# Premik bloka po vrsticah in stolpcih
		self.row_offset = 0
		self.column_offset = 0
		# Trenutno stanje rotacije (0 = začetna pozicija)
		self.rotation_state = 0
		# Barve za risanje blokov
		self.colors = Colors.get_cell_colors()

	def move(self, rows, columns):
		# Premakni blok za določeno število vrstic in stolpcev
		self.row_offset += rows
		self.column_offset += columns

	def get_cell_positions(self):
		# Pridobi pozicije celic bloka glede na trenutno rotacijo in zamik
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			# Ustvari novo pozicijo glede na zamike
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		# Zavrti blok v naslednjo rotacijsko pozicijo
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0  # Če je konec seznama, se vrni na začetek

	def undo_rotation(self):
		# Razveljavi rotacijo (nazaj za eno stanje)
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1  # Če je začetek, pojdi na konec

	def draw(self, screen, offset_x, offset_y):
		# Nariši blok na zaslon z določenim zamikom
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(
				offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, 
				self.cell_size - 1, self.cell_size - 1  # -1 zaradi robov med kvadratki
			)
			# Nariši kvadratek z ustrezno barvo
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)
