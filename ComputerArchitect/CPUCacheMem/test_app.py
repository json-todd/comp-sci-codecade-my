from cache import Cache
import pytest

@pytest.fixture
def instructions_to_read_these_locations_from_main_memory() -> dict[int]:
    input_from_codecademy_exercises = [8,3,4,12,10,7,3,2,6,3,1,7,8,6]
    return input_from_codecademy_exercises

class TestCacheEmpty:
    def test_read_1_elem(self, instructions_to_read_these_locations_from_main_memory):
        test_index = 0
        location_to_read_from_main_memory = instructions_to_read_these_locations_from_main_memory[test_index]
        expected_content = f"hello world #{location_to_read_from_main_memory}"

        cache = Cache()

        # act
        content_from_reading_mem = cache.read(location_to_read_from_main_memory)
        
        # assert
        assert content_from_reading_mem == expected_content

        cache_snapshot: list[dict] = cache.get_current_cache()
        assert cache_snapshot[0]["tag"] == 8
        assert cache_snapshot[0]["data"] == expected_content
    
    def test_read_up_to_cache_size(self,instructions_to_read_these_locations_from_main_memory):
        cache = Cache()
        number_of_reads = cache.size
        
        for read_number in range(number_of_reads):
            location_to_read_from_main_mem = instructions_to_read_these_locations_from_main_memory[read_number]
            expected_content = f"hello world #{location_to_read_from_main_mem}"
            
            # act
            content_from_reading_main_mem = cache.read(location_to_read_from_main_mem)
            
            # assert
            cache_snapshot: list[dict] = cache.get_current_cache()
            assert cache_snapshot[read_number]["tag"] == location_to_read_from_main_mem
            assert cache_snapshot[read_number]["data"] == expected_content
    
    def test_read_1_more_than_cache_size(self, instructions_to_read_these_locations_from_main_memory):
        number_