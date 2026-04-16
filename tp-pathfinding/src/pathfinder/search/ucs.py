from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)
        while not frontier.is_empty():
            # Sacamos el nodo de la frontera
            node = frontier.pop()
            # Test de objetivo:
            if grid.objective_test(node.state):
                return Solution(node, reached)
            # Expandimos las acciones posibles desde el estado actual
            for a in grid.actions(node.state):
                s = grid.result(node.state, a)
                c = node.cost + grid.individual_cost(node.state, a)
                if s not in reached or c < reached[s]:
                    hijo = Node("" ,state=s, cost=c, parent=node, action=a)
                    reached[s] = c
                    frontier.add(hijo, c)

        return NoSolution(reached)

"""
1 function GRAPH-UCS(problema) return solución o no-solución
     n₀ ← NODO(problema.estado-inicial, None, None, 0)
     frontera ← ColaPrioridad()
     frontera.encolar(n₀,n₀.costo)
     alcanzados ← {n₀.estado: n₀.costo}
     do
         if frontera.vacía() then return no-solución
            n ← frontera.desencolar()
         if problema.test-objetivo(n.estado) then return solución(n)
                forall a in problema.acciones(n.estado) do
                s’ ← problema.resultado(n.estado, a)
                c’ ← n.costo + problema.costo-individual(n.estado,a)
                if s’ is not in alcanzados or c’ < alcanzados[s’] then
                    n’ ← Nodo(s’, n, a, c’)
                    alcanzados[s’] ← c’
                    frontera.encolar(n’,c’)
                    """