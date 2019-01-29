# Define all nodes
node0 = {'val': 0, 'nodes': []}
node1 = {'val': 1, 'nodes': []}
node2 = {'val': 2, 'nodes': []}
node3 = {'val': 3, 'nodes': []}
node4 = {'val': 4, 'nodes': []}
node5 = {'val': 5, 'nodes': []}
node6 = {'val': 6, 'nodes': []}
node7 = {'val': 7, 'nodes': []}
node8 = {'val': 8, 'nodes': []}
node9 = {'val': 9, 'nodes': []}
node10 = {'val': 10, 'nodes': []}
node11 = {'val': 11, 'nodes': []}
node12 = {'val': 12, 'nodes': []}

# Assign nodes
node0['nodes'] = [node1, node10]
node1['nodes'] = [node0, node2, node11]
node2['nodes'] = [node1, node3]
node3['nodes'] = [node2, node4, node5, node6]
node4['nodes'] = [node3]
node5['nodes'] = [node3, node6, node7, node8]
node6['nodes'] = [node3, node8, node9]
node7['nodes'] = [node5, node9]
node8['nodes'] = [node5, node6, node9]
node9['nodes'] = [node6, node7, node8, node10]
node10['nodes'] = [node0, node12, node9]
node11['nodes'] = [node1]
node12['nodes'] = [node10]

# Helpers
route = []
record = []

# Search recursive and get the route
def run(node, val):
  if node['val'] not in record:
    record.insert(0, node['val'])
    if node['val'] == val:
      return True
    for nextNode in node['nodes']:
      if run(nextNode, val):
        route.insert(0, nextNode['val'])
        return True
    return False

# Solution
run(node0, 6)
route.insert(0, 0) # To insert the root node
print("One route is: {route}".format(route=route))