"""
maze.py - Génération et gestion du labyrinthe
INF-5183 – Fondements de l'Intelligence Artificielle
"""

import random
from collections import deque


class Maze:
    """
    Représente un labyrinthe 2D de taille NxN.

    Symboles :
        '#' → mur
        '.' → case libre
        'S' → départ (1,1)
        'G' → arrivée (N-2, N-2)
    """

    def __init__(self, size: int = 16, seed: int = None):
        self.size = size
        self.seed = seed
        self.start = (1, 1)
        self.goal = (size - 2, size - 2)
        self.grid = []
        self._generate()

    # ── Génération

    def _generate(self):
        """
        Génère un labyrinthe aléatoire valide.
        Répète la construction jusqu'à obtenir un chemin S→G.
        """
        if self.seed is not None:
            random.seed(self.seed)

        attempt = 0
        while True:
            attempt += 1
            grid = self._build_grid()
            if self._has_path(grid):
                self.grid = grid
                break
            if self.seed is not None:
                random.seed(self.seed + attempt)

    def _build_grid(self) -> list:
        """Construit une grille candidate avec murs aléatoires (~35%)."""
        n = self.size
        grid = []
        for row in range(n):
            line = []
            for col in range(n):
                if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                    line.append('#') # Bord extérieur → toujours mur
                else:
                    line.append('#' if random.random() < 0.35 else '.')
            grid.append(line)

        # Départ et arrivée toujours libres
        sr, sc = self.start
        gr, gc = self.goal
        grid[sr][sc] = 'S'
        grid[gr][gc] = 'G'
        return grid

    # ── Vérification de connexité

    def _has_path(self, grid: list) -> bool:
        """BFS interne : vérifie qu'un chemin S→G existe."""
        visited = set()
        queue = deque([self.start])
        visited.add(self.start)

        while queue:
            r, c = queue.popleft()
            if (r, c) == self.goal:
                return True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and self._is_walkable(grid, nr, nc):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # ── Utilitaires

    def _is_walkable(self, grid: list, r: int, c: int) -> bool:
        """Vérifie qu'une case est dans les limites et non un mur."""
        n = self.size
        return 0 <= r < n and 0 <= c < n and grid[r][c] != '#'

    def is_walkable(self, r: int, c: int) -> bool:
        """Version publique utilisant self.grid."""
        return self._is_walkable(self.grid, r, c)

    def get_neighbors(self, r: int, c: int) -> list:
        """
        Retourne les voisins franchissables dans l'ordre :
        droite, bas, gauche, haut  (cohérent avec DFS demandé).
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [(r + dr, c + dc) for dr, dc in directions
                if self.is_walkable(r + dr, c + dc)]

    # ── Affichage

    def display(self, explored: set = None, path: list = None) -> str:
        """
        Affiche le labyrinthe avec :
            '*' → chemin solution
            'p' → cases explorées (hors chemin)
        Priorité : S/G > * > p > contenu original
        """
        explored = explored or set()
        path_set = set(path) if path else set()

        lines = []
        for r, row in enumerate(self.grid):
            line = []
            for c, cell in enumerate(row):
                pos = (r, c)
                if cell in ('S', 'G'):
                    line.append(cell)
                elif pos in path_set:
                    line.append('*')
                elif pos in explored:
                    line.append('p')
                else:
                    line.append(cell)
            lines.append(' '.join(line))
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.display()