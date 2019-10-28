import networkx as nx
from . import Device
from ._specs import Specs, specs_from_graph
from ._isa import ISA, isa_from_graph, isa_from_digraph


def ibmq_ourense():
    graph = nx.from_edgelist([
        (0, 1), (1, 0),
        (1, 2), (2, 1),
        (1, 3), (3, 1),
        (3, 4), (4, 3)
    ])

    return Device(name="ibmq_ourense",
                  raw={"isa": isa_from_digraph(graph, twoq_type='CNOT').to_dict(),
                       "specs": specs_from_graph(graph).to_dict()})


def ibmq_yorktown():
    graph = nx.from_edgelist([
        (0, 1), (0, 2),
        (1, 2), (3, 2),
        (3, 4), (4, 2)
    ])
    return Device(name="ibmq_yorktown",
                  raw={"isa": isa_from_digraph(graph, twoq_type='CNOT').to_dict(),
                       "specs": specs_from_graph(graph).to_dict()})
