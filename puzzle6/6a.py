file = "input1.txt"


# https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python-are-there-any-built-in-data-structures-in
class Tree(object):
    def __init__(self, name, parent, children=None):
        self.children = []
        self.name = name
        self.parent = parent
        if children is not None:
            for child in children:
                self.children.append(child)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def traverse_tree(tree_node, distances, current_distance=0):
    distances[tree_node.name] = current_distance

    for child in tree_node.children:
        traverse_tree(child, distances, current_distance + 1)


# create tree structure
obj_to_tree = {}
with open(file) as f:
    for line in f:
        print(line.strip())
        linesplit = line.strip().split(')')
        if len(obj_to_tree) == 0:
            obj_to_tree[linesplit[0]] = Tree(linesplit[0], None)
            obj_to_tree[linesplit[1]] = Tree(linesplit[1], obj_to_tree[linesplit[0]])
            obj_to_tree[linesplit[0]].add_child(obj_to_tree[linesplit[1]])
        else:
            if linesplit[0] not in obj_to_tree.keys():
                obj_to_tree[linesplit[0]] = Tree(linesplit[0], None)
            tree = obj_to_tree[linesplit[0]]
            if linesplit[1] in obj_to_tree.keys():
                tree2 = obj_to_tree[linesplit[1]]
                tree2.parent = tree
                tree.add_child(tree2)
            else:
                tree2 = Tree(linesplit[1], tree)
                obj_to_tree[linesplit[1]] = tree2
                tree.add_child(tree2)

# calculate distance from root to every node
orbits = {}
traverse_tree(obj_to_tree['COM'], orbits)

# calculate the sum of orbits
sum_of_orbits = 0
for key in orbits.keys():
    sum_of_orbits += orbits[key]

print('Sum of orbits ' + str(sum_of_orbits))


### 6b

def path_to_node(name):
    # get path from given node to COM
    current_node = obj_to_tree[name]
    path = []
    while current_node.parent is not None:
        path.append(current_node)
        current_node = current_node.parent
    path.append(current_node)
    return path


# get path from YOU to COM
path_from_you = path_to_node('YOU')
path_from_you.reverse()
distance_you = len(path_from_you)

# get path from SAN to COM
path_from_san = path_to_node('SAN')
path_from_san.reverse()
distance_san = len(path_from_san)

# find lca
i = 0
lca = None
while lca is None and i < min(len(path_from_you), len(path_from_san)):
    if path_from_you[i] != path_from_san[i]:
        lca = path_from_you[i-1]
    i += 1

print(lca)

# distance between two nodes in tree:
# distance v to root + distance w to root - 2*distance lca to root
path_from_lca = path_to_node(lca.name)
distance_lca = len(path_from_lca)
print("Distance YOU: " + str(distance_you))
print("Distance SAN: " + str(distance_san))
print("Distance LCA: " + str(distance_lca))
print("Number of orbital transfers: " + str(distance_you + distance_san - 2 * distance_lca - 2))
