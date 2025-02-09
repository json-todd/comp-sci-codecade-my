def dfs(graph, current_vertex, target_val, visited_vertices=None) -> dict|None:
  if visited_vertices is None:
    visited_vertices = []
  
  visited_vertices.append(current_vertex)
  
  if current_vertex == target_val:
    return visited_vertices
  
  for neighbor in graph.get(current_vertex, []):
    if neighbor in visited_vertices: continue
    
    path_found = dfs(
      graph,
      neighbor, target_val,
      visited_vertices
    )
    
    if path_found is not None:
      return path_found
  
  return None


def bfs(graph, start_vert, target_val) -> list|None:
  path = [start_vert]  
  vertex_and_path = [start_vert, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:    
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph.get(current_vertex, []):
      if neighbor not in visited:
        if neighbor == target_val:
          return path + [neighbor]
        
        bfs_queue.append([neighbor, path + [neighbor]])
  
  return None