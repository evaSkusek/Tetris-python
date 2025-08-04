import pygame
from colors import Colors

class Grid:
	def __init__(self):
		# Dimenzije mreže (20 vrstic x 10 stolpcev)
		self.num_rows = 20
		self.num_cols = 10
		self.cell_size = 30  # Velikost posamezne celice v pikslih
		# Ustvari mrežo, kjer je vsaka celica na začetku prazna (vrednost 0)
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		# Pridobi barve za risanje celic
		self.colors = Colors.get_cell_colors()

	def print_grid(self):
		# Izpiše trenutno stanje mreže v terminal (debug funkcija)
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ")
			print()

	def is_inside(self, row, column):
		# Preveri, ali je dana vrstica in stolpec znotraj meja mreže
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

	def is_empty(self, row, column):
		# Preveri, ali je določena celica prazna (vrednost 0)
		if self.grid[row][column] == 0:
			return True
		return False

	def is_row_full(self, row):
		# Preveri, ali je celotna vrstica zapolnjena (brez ničel)
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True

	def clear_row(self, row):
		# Počisti (ponastavi) dano vrstico (vse vrednosti postavi na 0)
		for column in range(self.num_cols):
			self.grid[row][column] = 0

	def move_row_down(self, row, num_rows):
		# Premakne vrstico navzdol za podano število vrstic
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

	def clear_full_rows(self):
		# Počisti vse polne vrstice in premakni zgornje vrstice navzdol
		completed = 0  # Število počistenih vrstic
		# Začni od spodnje vrstice proti vrhu
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed  # Vrni število počistenih vrstic

	def reset(self):
		# Ponastavi celotno mrežo (vse celice na 0)
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0

	def draw(self, screen):
		# Nariši mrežo na podani zaslon (screen)
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column]  # ID bloka v tej celici (ali 0)
				cell_rect = pygame.Rect(
					column * self.cell_size + 11,  # vodoravna pozicija
					row * self.cell_size + 11,     # navpična pozicija
					self.cell_size - 1,            # širina celice
					self.cell_size - 1             # višina celice
				)
				# Nariši pravokotnik z ustrezno barvo glede na vrednost celice
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
