from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search
        Args:
            grid (Grid): Grid of points
        Returns:
            Solution: Solution found
        """
        # nodo raiz
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        # En A*, guardamos el costo (g) para llegar a ese estado.
        reached = {}
        reached[root.state] = root.cost
        
        frontier = PriorityQueueFrontier()
        
        # agregamos la raíz a la frontera
        # la prioridad f(n) = g(n) + h(n)
        f_cost_root = root.cost + grid.heuristic(root.state)
        frontier.add(root, priority=f_cost_root) 

        while not frontier.is_empty():
            # sacamos el nodo con el menor f(n) de la frontera
            node = frontier.pop()
            
            # TEST OBJETIVO: En A*, se hace al EXPANDIR el nodo, no al generarlo.

            if grid.objective_test(node.state):
                return Solution(node, reached)
                
            # Expandimos las acciones posibles desde el estado actual
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                
                # g(n): Costo acumulado del padre + costo del paso actual
                new_cost = node.cost + grid.individual_cost(node.state, action)
                
                # Control de Grafo:
                # Agregamos si el estado no ha sido alcanzado antes, 
                # O si encontramos un camino más barato hacia un estado ya alcanzado
                if successor not in reached or new_cost < reached[successor]:
                    reached[successor] = new_cost
                    
                    child = Node(
                        value="",
                        state=successor,
                        cost=new_cost,
                        parent=node,
                        action=action
                    )
                    
                    # f(n) = g(n) + h(n)
                    f_cost = new_cost + grid.heuristic(successor)
                    
                    # Añadimos el hijo a la frontera con su nueva prioridad
                    frontier.add(child, priority=f_cost)
                    
        return NoSolution(reached)


