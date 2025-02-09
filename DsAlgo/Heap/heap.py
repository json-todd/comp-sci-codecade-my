class MaxHeap:
  def __init__(self, input_list: list = []):
    self.heap_list: list[int|None] = [None]
    self.count: int = 0
    
    if input_list:
      for _elem in input_list:
        self.add(_elem)
    
    
  def heapsort(input_list: list) -> list:
    if not input_list: return []
    
    sort_list = []
    max_heap = MaxHeap()
    for _elem in input_list:
      max_heap.add(_elem)  
    
    while max_heap.has_valid_elem_in_storage():  
      _max_elem = max_heap.retrieve_max()
      
      sort_list.append(_max_elem)
    
    sort_list.reverse()
    # sort_list_ascending = sort_list[0:-1:-1]
    return sort_list
  
  def retrieve_max(self) -> int|None:
    if self.count == 0: return None
    
    self.heap_list[1], self.heap_list[self.count] = \
       self.heap_list[self.count], self.heap_list[1]
    self.count -= 1
    _max_elem = self.heap_list.pop()
    self.heapify_down()
    
    return _max_elem
  
  def add(self, element: int):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()
  
  def heapify_down(self) -> None:
    idx = 1 
    
    def this_element_is_less_than_its_larger_child(heap: MaxHeap, idx: int) -> bool:
      return heap.heap_list[idx] < heap.heap_list[larger_child_idx]   
    
    def swap_position_this_element_with_its_larger_child(heap: MaxHeap, idx: int) -> None:
      heap.heap_list[larger_child_idx], heap.heap_list[idx] = \
          heap.heap_list[idx], heap.heap_list[larger_child_idx]
    
    while self.child_present(idx):
      larger_child_idx = self.get_larger_child_idx(idx)
      if this_element_is_less_than_its_larger_child(self, idx):
        swap_position_this_element_with_its_larger_child(self, idx)
        
      idx = larger_child_idx
  
  def heapify_up(self) -> None:
    idx = self.count
    
    def this_element_is_greater_or_equal_to_its_parent (heap: MaxHeap, idx: int) -> bool: 
      return  heap.heap_list[idx] >= heap.heap_list[heap.parent_idx(idx)]   
    
    def swap_position_this_element_with_its_parent (heap: MaxHeap, idx: int) -> None: 
      heap.heap_list[heap.parent_idx(idx)], heap.heap_list[idx] = \
        heap.heap_list[idx], heap.heap_list[heap.parent_idx(idx)]
    
    while self.parent_present(idx):
      if this_element_is_greater_or_equal_to_its_parent(self, idx):
        swap_position_this_element_with_its_parent(self, idx)
      
      idx = self.parent_idx(idx)
  
  def get_larger_child_idx(self, idx: int) -> int:
    if self.right_child_idx(idx) > self.count:
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      
      if left_child > right_child:
        return self.left_child_idx(idx)
      else:
        return self.right_child_idx(idx)
  
  def parent_idx(self, idx: int) -> int:
    return idx // 2
  
  def left_child_idx(self, idx: int) -> int:
    return idx * 2
  
  def right_child_idx(self, idx: int) -> int:
    return idx * 2 + 1
  
  def child_present(self, idx) -> bool:
    return self.left_child_idx(idx) <= self.count
  
  def parent_present(self, idx) -> bool:
    return self.parent_idx(idx) > 0
  
  def has_valid_elem_in_storage(self) -> bool:
    return self.count > 0
  
  def __str__(self) -> str:
    return str([_elem for _elem in self.heap_list])
  
  
if __name__ == "__main__":
  my_list = [42, 70, 38, 12, 94, 28]
  
  heap_list: MaxHeap = MaxHeap()
  # _ = (heap_list.add(_elem) for _elem in my_list)
  for _elem in my_list:
    heap_list.add(_elem)
  
  print(f"The heap after add look like this: {str(heap_list)}")
  
  my_list_heap_max = heap_list.retrieve_max()
  print(f"Got max element: {my_list_heap_max}")
  print(f"The heap after retrieve_max look like this: {heap_list}")
  assert my_list_heap_max == max(my_list), "heap max fails"
  
  
  #sorted_list = MaxHeap.heapsort(my_list)
  #assert sorted_list == sorted(my_list), "heap sort fails"
