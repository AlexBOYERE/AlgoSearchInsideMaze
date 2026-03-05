"""
bfs.py - Implémentation de BFS (Breadth-First Search)
INF-5183 – Fondements de l'Intelligence Artificielle

Principe :
    - Utilise une file (FIFO) pour explorer en largeur.
    - Garantit le chemin le plus court (en nombre de cases).
"""

import time
from collections import deque
from maze import Maze


def bfs(maze: Maze) -> dict:
    """
    Applique BFS pour trouver le chemin optimal de S à G.

    Args:
        maze (Maze): Le labyrinthe à résoudre.

    Returns:
        dict avec les mêmes clés que dfs().
    """
    start_time = time.perf_counter()

    start = maze.start
    goal  = maze.goal

    # La file stocke des couples (position, chemin_parcouru)
    queue = deque([(start, [start])])

    visited = set()
    visited.add(start)

    explored = set()

    while queue:
        (r, c), path = queue.popleft()   # FIFO : on défile le premier ajouté
        explored.add((r, c))

        if (r, c) == goal:
            elapsed = (time.perf_counter() - start_time) * 1000
            return {
                'explored': explored,
                'path':     path,
                'nodes':    len(explored),
                'length':   len(path),
                'time_ms':  elapsed,
            }

        for neighbor in maze.get_neighbors(r, c):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    elapsed = (time.perf_counter() - start_time) * 1000
    return {
        'explored': explored,
        'path':     [],
        'nodes':    len(explored),
        'length':   0,
        'time_ms':  elapsed,
    }