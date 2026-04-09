from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        reached = {}
        reached[root.state] = True

        if grid.objective_test(root.state):
            return Solution(root, reached)

        frontier = QueueFrontier()  
        frontier.add(root)

        while not frontier.is_empty():
        # 1. Sacamos el nodo de la frontera
            node = frontier.remove() 

            # 2. Expandimos las acciones posibles desde el estado actual
            for action in grid.actions(node.state): 

                # 3. Obtenemos el estado resultante
                successor = grid.result(node.state, action) 

                # 4. Control de Grafo:
                if successor not in reached:
                    # Marcamos como alcanzado inmediatamente para evitar redundancia 
                    reached[successor] = True 

                    # Creamos el nuevo nodo hijo
                    # El costo es: costo del padre + costo de este paso particular
                    child = Node(
                        value="",
                        state=successor,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action
                    )

                    # 6. Test objetivo
                    if grid.objective_test(successor):
                        return Solution(child, reached) # [cite: 45]

                    # 7. Si no es el objetivo, lo sumamos a la fila para expandirlo luego
                    frontier.add(child) # [cite: 47]

        return NoSolution(reached)
