class Node:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, neighbor, weight):
        self.edges[neighbor] = weight


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]

    def add_edge(self, from_name, to_name, weight):
        from_node = self.add_node(from_name)
        to_node = self.add_node(to_name)
        from_node.add_edge(to_node, weight)

    def dijkstra(self, start_name, end_name):
        if start_name not in self.nodes or end_name not in self.nodes:
            return None
        start = self.nodes[start_name]
        end = self.nodes[end_name]

        distances = {node: float('inf') for node in self.nodes.values()}
        previous = {node: None for node in self.nodes.values()}
        distances[start] = 0
        unvisited = set(self.nodes.values())

        while unvisited:
            current_node = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current_node)
            if distances[current_node] == float('inf'):
                break
            for neighbor, weight in current_node.edges.items():
                new_dist = distances[current_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
            if current_node == end:
                break

        path = []
        current = end
        while current:
            path.append(current.name)
            current = previous[current]
        path.reverse()
        return path, distances[end]

    def min_edge(self):
        min_weight = float('inf')
        min_edge_info = None
        for node in self.nodes.values():
            for neighbor, weight in node.edges.items():
                if weight < min_weight:
                    min_weight = weight
                    min_edge_info = (node.name, neighbor.name, weight)
        return min_edge_info

    def max_edge(self):
        max_weight = float('-inf')
        max_edge_info = None
        for node in self.nodes.values():
            for neighbor, weight in node.edges.items():
                if weight > max_weight:
                    max_weight = weight
                    max_edge_info = (node.name, neighbor.name, weight)
        return max_edge_info

    def remove_edge(self, from_name, to_name):
        if from_name not in self.nodes or to_name not in self.nodes:
            return False
        from_node = self.nodes[from_name]
        to_node = self.nodes[to_name]
        if to_node in from_node.edges:
            del from_node.edges[to_node]
            return True
        return False

    def remove_node(self, name):
        if name not in self.nodes:
            return False
        node_to_remove = self.nodes[name]
        for node in self.nodes.values():
            if node_to_remove in node.edges:
                del node.edges[node_to_remove]
        del self.nodes[name]
        return True

    def is_connected(self):
        if not self.nodes:
            return True
        
        start = next(iter(self.nodes.values()))
        visited = set()
        stack = [start]
        
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in current.edges.keys():
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return len(visited) == len(self.nodes)

    def display(self):
        for node in self.nodes.values():
            line = f"{node.name} -> "
            edges = [f"{neighbor.name}({weight})" for neighbor, weight in node.edges.items()]
            line += ", ".join(edges)
            print(line)


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)

    g.display()

    path, distance = g.dijkstra("A", "D")
    print("Shortest path:", path)
    print("Distance:", distance)