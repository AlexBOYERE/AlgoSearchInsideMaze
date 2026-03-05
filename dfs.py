"""
dfs.py - Implémentation de DFS (Depth-First Search)
INF-5183 – Fondements de l'Intelligence Artificielle

Principe :
    - Utilise une pile (LIFO) pour explorer en profondeur.
    - Explore les voisins dans l'ordre : droite, bas, gauche, haut.
    - Ne garantit PAS le chemin le plus court.
"""

import time
from maze import Maze


def dfs(maze: Maze) -> dict:
    """
    Applique DFS pour trouver un chemin de S à G.

    Args:
        maze (Maze): Le labyrinthe à résoudre.

    Returns:
        dict avec les clés :
            'explored' : set  – toutes les positions visitées
            'path'     : list – chemin solution (vide si non trouvé)
            'nodes'    : int  – nombre de nœuds explorés
            'length'   : int  – longueur du chemin (0 si non trouvé)
            'time_ms'  : float – temps d'exécution en millisecondes
    """
    start_time = time.perf_counter()

    start = maze.start
    goal  = maze.goal

    # La pile stocke des couples (position, chemin_parcouru_jusqu'ici)
    stack = [(start, [start])]

    # Ensemble des nœuds déjà visités (évite les boucles infinies)
    visited = set()
    visited.add(start)

    explored = set()   # Toutes les cases parcourues (pour la visualisation)

    while stack:
        (r, c), path = stack.pop()   # LIFO : on dépile le dernier ajouté
        explored.add((r, c))

        # Cas de succès : on a atteint le but
        if (r, c) == goal:
            elapsed = (time.perf_counter() - start_time) * 1000
            return {
                'explored': explored,
                'path':     path,
                'nodes':    len(explored),
                'length':   len(path),
                'time_ms':  elapsed,
            }

        # Ajout des voisins non visités dans la pile
        # get_neighbors retourne déjà les voisins dans l'ordre voulu
        for neighbor in maze.get_neighbors(r, c):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    # Aucun chemin trouvé
    elapsed = (time.perf_counter() - start_time) * 1000
    return {
        'explored': explored,
        'path':     [],
        'nodes':    len(explored),
        'length':   0,
        'time_ms':  elapsed,
    }