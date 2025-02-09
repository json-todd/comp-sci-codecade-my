from heap import MaxHeap
import pytest 

@pytest.fixture
def my_list() -> list:
  return [42, 70, 38, 12, 94, 28]

class TestInstantiate:
  def test_without_input_list(self):
    heap_list: MaxHeap = MaxHeap()
    assert str(heap_list.heap_list) == '[None]'
  
  def test_with_input_list(self, my_list):
    heap_list: MaxHeap = MaxHeap(my_list)
    assert len(heap_list.heap_list) > 0, "heap list shouldn't be empty"
  
    
  def test_without_input_list_manual_adding(self, my_list):
    # my_list = [42, 70, 38, 12, 94, 28]
    
    heap_list: MaxHeap = MaxHeap()
    # _ = (heap_list.add(_elem) for _elem in my_list)
    for _elem in my_list:
      heap_list.add(_elem)
    
    print(f"The heap after add look like this: {str(heap_list)}")
    assert len(heap_list.heap_list) > 0, "heap list shouldn't be empty"


  
def test_sort(my_list):
  sorted_list = MaxHeap.heapsort(my_list)
  assert isinstance(sorted_list, list), "heap sort should return a list"
  assert len(sorted_list) > 0 , "heap sort shouldn't return empty"
  assert str(sorted_list) ==  str(sorted(my_list)), "heap sort fails"
  

class TestMax:
  def test_normal_list(self, my_list):
    heap_list: MaxHeap = MaxHeap(my_list)
    print(f"Instantiate heap: {heap_list}")
      
    got_heap_max = heap_list.retrieve_max()
    expect_max = max(my_list)
    print(f"Got max element: {got_heap_max}")
    print(f"The heap after retrieve_max look like this: {heap_list}")
    assert got_heap_max == expect_max, "heap max fails"


class TestValidElemInStorage:
  def test_normal_list(self, my_list):
    heap_list: MaxHeap = MaxHeap(my_list)
      
    assert heap_list.has_valid_elem_in_storage(), "I thought it has valid element"
    
  def test_heap_w_a_single_element(self):
    my_list = [1]
    heap_list: MaxHeap = MaxHeap()
    for _elem in my_list:
      heap_list.add(_elem)
    
    print(f"{str(heap_list)}")
    assert heap_list.has_valid_elem_in_storage(), f"I thought it has valid element"
    
  
  def test_empty_list(self):
    my_list = []
    heap_list: MaxHeap = MaxHeap()
    for _elem in my_list:
      heap_list.add(_elem)
      
    assert heap_list.has_valid_elem_in_storage() == False, "I thought it doesn't have a valid element"
  
  