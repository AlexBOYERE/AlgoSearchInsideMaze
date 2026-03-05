"""
astar.py - Implémentation de A* (A-Star)
INF-5183 – Fondements de l'Intelligence Artificielle

Principe :
    - File de priorité (min-heap) sur f(n) = g(n) + h(n).
    - g(n) : coût réel depuis S jusqu'au nœud n.
    - h(n) : heuristique de Manhattan = |r - gr| + |c - gc|.
    - Garantit le chemin optimal (heuristique admissible).
"""

import time
import heapq
from maze import Maze


def manhattan(a: tuple, b: tuple) -> int:
    """Distance de Manhattan entre deux points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze: Maze) -> dict:
    """
    Applique A* pour trouver le chemin optimal de S à G.

    Args:
        maze (Maze): Le labyrinthe à résoudre.

    Returns:
        dict avec les mêmes clés que dfs() et bfs().
    """
    start_time = time.perf_counter()

    start = maze.start
    goal  = maze.goal

    # Le heap stocke des tuples : (f, g, position, chemin)
    # f = g + h ; on trie d'abord par f, puis par g pour les égalités
    h0 = manhattan(start, goal)
    heap = [(h0, 0, start, [start])]   # (f, g, pos, path)

    # Dictionnaire des meilleurs coûts g connus pour chaque nœud
    best_g = {start: 0}

    explored = set()

    while heap:
        f, g, (r, c), path = heapq.heappop(heap)

        # Si ce nœud a déjà été traité avec un meilleur coût, on ignore
        if (r, c) in explored:
            continue
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
            new_g = g + 1   # Chaque déplacement coûte 1
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                new_h = manhattan(neighbor, goal)
                new_f = new_g + new_h
                heapq.heappush(heap, (new_f, new_g, neighbor, path + [neighbor]))

    elapsed = (time.perf_counter() - start_time) * 1000
    return {
        'explored': explored,
        'path':     [],
        'nodes':    len(explored),
        'length':   0,
        'time_ms':  elapsed,
    }