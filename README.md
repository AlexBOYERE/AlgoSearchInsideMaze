# Devoir I – Algorithmes de Recherche dans un Labyrinthe
**INF-5183 – Fondements de l'Intelligence Artificielle**  
**Université du Québec en Outaouais**  
**Session : Hiver 2026**

---

## Description

Ce projet implémente trois algorithmes de recherche pour résoudre un labyrinthe 16x16 :
- **DFS** (Depth-First Search) — recherche en profondeur
- **BFS** (Breadth-First Search) — recherche en largeur, chemin optimal
- **A\*** (A-Star) — recherche informée avec heuristique de Manhattan

---

## Prérequis

- Python 3.11+
- Aucune dépendance externe

---

## Installation
```bash
git clone https://github.com/votre-utilisateur/Devoir_I.git
cd Devoir_I
```

---

## Exécution
```bash
# Labyrinthe aléatoire (16x16)
python main.py

# Avec une graine fixe (reproductible)
python main.py --seed 42

# Taille et graine personnalisées
python main.py --seed 42 --size 20
```

---

## Structure du projet

| Fichier | Rôle |
|---------|------|
| `maze.py` | Génération et gestion du labyrinthe |
| `dfs.py` | Depth-First Search (pile LIFO) |
| `bfs.py` | Breadth-First Search (file FIFO) |
| `astar.py` | A* avec heuristique de Manhattan |
| `main.py` | Point d'entrée, orchestration et affichage |
| `README.md` | Documentation |

---

## Symboles

| Symbole | Signification |
|---------|---------------|
| `#` | Mur |
| `.` | Case libre |
| `S` | Départ (1,1) |
| `G` | Arrivée (N-2, N-2) |
| `p` | Case explorée |
| `*` | Chemin solution |

---

## Exemple de sortie
```
  Algorithme      Nœuds    Longueur   Temps (ms)
  ──────────────────────────────────────────────
  DFS                78          45        0.521
  BFS               112          27        0.634
  A* (Manhattan)     45          27        0.312
```

---

## Sources

- Documentation Python : https://docs.python.org/3/
- BFS : https://en.wikipedia.org/wiki/Breadth-first_search
- DFS : https://en.wikipedia.org/wiki/Depth-first_search
- A* : https://en.wikipedia.org/wiki/A*_search_algorithm
- Distance de Manhattan : https://en.wikipedia.org/wiki/Taxicab_geometry
- Russell & Norvig — *Artificial Intelligence: A Modern Approach*, Chapitres 3 et 4