import networkx as nx

def find_components(G):
    """Find all components of graph G"""
    seen = set()
    for v in G.nodes():
        if v not in seen:
            c = find_component(G, v)
            yield c
            seen.update(c)

def find_component(G, v):
    """Find all nodes in the same component as node v"""
    c = set()
    c.add(v)
    _find_component(G, v, c)
    return c

def _find_component(G, v, c):
    """Helper function for finding all nodes in the same component as node v,
    storing them as we recurse in set c."""
    for n in G.neighbors(v):
         if n not in c:
            c.add(n)
            _find_component(G, n, c)


G = nx.Graph()
G.add_cycle(range(0, 5))
G.add_cycle(range(10, 15))
for c in find_components(G):
    print(c)

# Exercise: look at the NetworkX implementation in nx.algorithm.components
