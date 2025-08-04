from block import Block
from position import Position

# L-oblikovan blok
class LBlock(Block):
	def __init__(self):
		super().__init__(id = 1)  # ID 1 za L blok
		# Definicija celic za vse 4 rotacijske pozicije
		self.cells = {
			0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
			3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}
		self.move(0, 3)  # Začetni premik bloka na sredino vrstice

# J-oblikovan blok (obrnjeni L)
class JBlock(Block):
	def __init__(self):
		super().__init__(id = 2)  # ID 2 za J blok
		self.cells = {
			0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
			3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
		}
		self.move(0, 3)

# I-oblikovan blok (ravna črta)
class IBlock(Block):
	def __init__(self):
		super().__init__(id = 3)  # ID 3 za I blok
		self.cells = {
			0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
			1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
			2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
			3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
		}
		self.move(-1, 3)  # Dvig bloka za eno vrstico zaradi višine

# O-oblikovan blok (kvadrat)
class OBlock(Block):
	def __init__(self):
		super().__init__(id = 4)  # ID 4 za O blok
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
		}
		self.move(0, 4)  # Postavi bolj v sredino

# S-oblikovan blok
class SBlock(Block):
	def __init__(self):
		super().__init__(id = 5)  # ID 5 za S blok
		self.cells = {
			0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
			1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
			2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
			3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
		}
		self.move(0, 3)

# T-oblikovan blok
class TBlock(Block):
	def __init__(self):
		super().__init__(id = 6)  # ID 6 za T blok
		self.cells = {
			0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
			3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
		}
		self.move(0, 3)

# Z-oblikovan blok
class ZBlock(Block):
	def __init__(self):
		super().__init__(id = 7)  # ID 7 za Z blok
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
			1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
			3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
		}
		self.move(0, 3)
