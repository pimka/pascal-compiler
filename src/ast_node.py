class Node(object):
    def __init__(self, t, *args):
        self.type = t
        self.args = args

    def __str__(self):
        s = f'type: {str(self.type)}\n'
        s += ''.join([f'i: {str(i)}\n' for i in self.args])
        return s
