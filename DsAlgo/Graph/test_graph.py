from graph import dfs, bfs
import pytest

@pytest.fixture
def my_graph() -> dict:
  the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }
  
  return the_most_dangerous_graph

@pytest.mark.parametrize(
  "graph_search_style",
  [dfs, bfs]
)
class TestGraphSearch:
  def test_found_the_happy_path(self, graph_search_style, my_graph):
    # given
    starting_point="crocodiles"
    target_point="bees"
    assert starting_point in my_graph and target_point in my_graph, "setup failed"
    
    # when
    got_result = graph_search_style(my_graph,
                     starting_point, target_point)
    print(got_result)
    
    # then
    assert isinstance(got_result, list), "path should be a list"
    assert len(got_result) > 0, "there should be a found valid path from start to target"
    assert str(got_result[0]) == str(starting_point), "path should begin with the starting point"
    assert str(got_result[-1]) == str(target_point), "path should end with the target"
    
    
  def test_target_not_in_graph(self, graph_search_style, my_graph):
    # given
    starting_point="crocodiles"
    target_point="donkey_bridge"
    assert target_point not in my_graph and starting_point in my_graph, "setup failed"
    
    # when
    got_result = graph_search_style(my_graph,
                     starting_point, target_point)
    
    # then
    assert got_result is None
    
  def test_start_point_not_in_graph(self, graph_search_style, my_graph):
    # given
    starting_point="donkey_bridge"
    target_point="crocodiles"
    assert starting_point not in my_graph and target_point in my_graph, "setup failed"
    
    # when
    got_result = graph_search_style(my_graph,
                     starting_point, target_point)
    
    # then
    assert got_result is None
    
    
class TestGraphBreadthFirstSearch:
  def test_found_a_happy_path(self, my_graph):
    # given
    starting_point="crocodiles"
    target_point="bees"
    assert starting_point in my_graph and target_point in my_graph, "setup failed"
    
    # when
    got_result = dfs(my_graph,
                     starting_point, target_point)
    print(got_result)
    
    # then
    assert isinstance(got_result, list), "path should be a list"
    assert len(got_result) > 0, "there should be a found valid path from start to target"