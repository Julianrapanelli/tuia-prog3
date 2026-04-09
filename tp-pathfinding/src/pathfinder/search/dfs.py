from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            # Sacamos el nodo (LIFO)
            node = frontier.remove()

            # Test de objetivo:
            if grid.objective_test(node.state):
                return Solution(node, expanded)

            # Si no lo expandimos antes, lo hacemos ahora
            if node.state not in expanded:
                expanded[node.state] = True

                # Expandimos sucesores
                for action in grid.actions(node.state):
                    successor_state = grid.result(node.state, action)

                    # Creamos el nodo hijo
                    child = Node(
                        "",
                        successor_state,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action
                    )

                    # Lo agregamos a la frontera si no fue expandido
                    if child.state not in expanded:
                        frontier.add(child)
        return NoSolution(expanded)
