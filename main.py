"""
main.py - Point d'entrée principal
INF-5183 – Fondements de l'Intelligence Artificielle

Exécution : python main.py
             python main.py --seed 42
             python main.py --seed 42 --size 20
"""

import argparse
import random
import sys

from maze  import Maze
from dfs   import dfs
from bfs   import bfs
from astar import astar


# ── Utilitaires d'affichage

def print_section(title: str):
    """Imprime un séparateur de section."""
    print('\n' + '═' * 60)
    print(f'  {title}')
    print('═' * 60)


def print_path_coords(path: list, start: tuple, goal: tuple):
    """Affiche la liste des coordonnées du chemin."""
    if not path:
        print("  Aucun chemin trouvé.")
        return

    coords = []
    for pos in path:
        if pos == start:
            coords.append(f"S {pos}")
        elif pos == goal:
            coords.append(f"G {pos}")
        else:
            coords.append(str(pos))

    print("  Chemin :")
    # Affichage sur plusieurs lignes si long
    line = "  " + " -> ".join(coords)
    if len(line) <= 80:
        print(line)
    else:
        chunk = []
        current = "  "
        for c in coords:
            if len(current) + len(c) + 4 > 78:
                print(current)
                current = "  " + c
            else:
                current += (" -> " if chunk else "") + c
                chunk.append(c)
        print(current)


def print_stats(result: dict):
    """Affiche les statistiques d'un algorithme."""
    print(f"  Nœuds explorés : {result['nodes']}")
    print(f"  Longueur du chemin : {result['length']}")
    print(f"  Temps d'exécution : {result['time_ms']:.3f} ms")


def print_comparison(results: dict):
    """Affiche le tableau comparatif des trois algorithmes."""
    print_section("TABLEAU COMPARATIF")
    header = f"  {'Algorithme':<20} {'Nœuds':>8} {'Longueur':>10} {'Temps (ms)':>12}"
    print(header)
    print("  " + "-" * 54)
    for name, res in results.items():
        print(f"  {name:<20} {res['nodes']:>8} {res['length']:>10} {res['time_ms']:>12.3f}")


def run_algorithm(name: str, algo_func, maze: Maze) -> dict:
    """
    Exécute un algorithme, affiche son exploration, sa solution
    et ses statistiques.
    """
    print_section(f"ALGORITHME : {name}")
    result = algo_func(maze)

    # ── Exploration
    print("\n  [Exploration — cases marquées 'p']")
    print(maze.display(explored=result['explored']))

    # ── Solution
    print("\n  [Solution — chemin marqué '*']")
    if result['path']:
        print(maze.display(path=result['path']))
    else:
        print("  (Aucun chemin trouvé)")

    # ── Coordonnées du chemin
    print()
    print_path_coords(result['path'], maze.start, maze.goal)

    # ── Statistiques
    print()
    print_stats(result)

    return result


# ── Programme principal

def main():
    parser = argparse.ArgumentParser(
        description="INF-5183 – Devoir I : Algorithmes de recherche dans un labyrinthe"
    )
    parser.add_argument('--seed', type=int, default=None,
                        help="Graine aléatoire pour la reproductibilité (ex: --seed 42)")
    parser.add_argument('--size', type=int, default=16,
                        help="Taille du labyrinthe NxN (défaut: 16)")
    args = parser.parse_args()

    # Si il n'y a pas de seed, renseignée
    if args.seed is None:
        args.seed = random.randint(0, 99999)

    # ── Génération du labyrinthe
    print_section(f"LABYRINTHE {args.size}x{args.size}  (seed={args.seed})")
    maze = Maze(size=args.size, seed=args.seed)
    print(maze)
    print(f"\n  Départ : {maze.start}   Arrivée : {maze.goal}")

    # ── Exécution des trois algorithmes
    results = {}
    for name, func in [("DFS", dfs), ("BFS", bfs), ("A* (Manhattan)", astar)]:
        results[name] = run_algorithm(name, func, maze)

    # ── Tableau comparatif
    print_comparison(results)
    print()


if __name__ == "__main__":
    main()

# Affiche la version de python
print(sys.version)