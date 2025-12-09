class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]
    while len(nodes_to_visit)> 0:
        node = nodes_to_visit.pop(0)
        if node["id"] == id:
            result.append(node)
            return node
        else:
            nodes_to_visit = node["children"] + nodes_to_visit 
    return result or None          
    pass


child_5 = {
  'value': 5,
  'children': []
}
child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': [child_5]
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}

def breadth_first_traversal(node):
    #Initialize an empty output list
    result = []
    #Initialize a list of nodes to visit and add the root node to it
    nodes_to_visit = [node]
    #While there are nodes in the nodes to visit list
    while len(nodes_to_visit)> 0:
        #Remove the first from the nodes to visit list 
        node = nodes_to_visit.pop(0)
        #Add its value to the output list
        result.append(node["value"])
        #Adds its children (if any) to the nodes to visit list
        nodes_to_visit = nodes_to_visit + node["children"]
    #Return the output list
    return result

print(breadth_first_traversal(root))

def depth_first_traversal(node):
    #Initialize an empty output list
    result = []
    #Initialize a list of nodes to visit and add the root node to it
    nodes_to_visit = [node]
    #While there are nodes in the list to nodes to visit
    while len(nodes_to_visit)>0:
        #Remove the first node from the list of nodes to visit
        node = nodes_to_visit.pop(0)
        #Add its value to the output list
        result.append(node["value"])
        #Add its children (if any) to the BEGINNING of the list of nodes to visit
        nodes_to_visit = node["children"] + nodes_to_visit
    #Return the output list
    return result

print(depth_first_traversal(root))

def depth_first_traversal_2(node, result = []):
    result.append(node["value"])
    for child in node["children"]:
        depth_first_traversal(child, result)
    return result    
