from graphviz import Digraph

class Graph:
    def __init__(self, ast):
        self.ast = ast
        self.graph = Digraph('gr', filename='test.gv')
        self.__build(self.ast)
        self.graph.view()

    def __build(self, node):
        result = []
        if node is None:
            return None
        self.graph.node(str(hash(node)), node.type)
        for arg in node.args:
            if type(arg) is str:
                self.graph.node(str(hash(node)), f'{node.type} ({arg})')
                result.append(str(hash(node)))
            else:
                ch_nodes = self.__build(arg)
                if ch_nodes != None:
                    for ch_node in set(ch_nodes):
                        self.graph.edge(str(hash(node)), ch_node)
        result.append(str(hash(node)))
        return result