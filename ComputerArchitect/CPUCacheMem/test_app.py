from app import CPU
import pytest

@pytest.fixture
def instructions_to_read_these_locations_from_main_memory() -> dict[int]:
    input_from_codecademy_exercises = [8,3,4,12,10,7,3,2,6,3,1,7,8,6]
    return input_from_codecademy_exercises

class TestCacheFullAssociative:
    def test_read_1_elem(self, instructions_to_read_these_locations_from_main_memory):
        test_index = 0
        location_to_read_from_main_memory = instructions_to_read_these_locations_from_main_memory[test_index]
        expected_content = f"hello world #{location_to_read_from_main_memory}"

        cpu = CPU()

        # act
        content_from_reading_mem = cpu.read(location_to_read_from_main_memory)
        
        # assert
        assert content_from_reading_mem == expected_content

        cache_snapshot: list[dict] = cpu.cache.get_current_cache()
        assert cache_snapshot[0]["tag"] == 8
        assert cache_snapshot[0]["data"] == expected_content
    
    def test_read_2_elem(self, instructions_to_read_these_locations_from_main_memory):
        cpu = CPU()
        test_number_of_instructions = 2
        
        for test_number in range(test_number_of_instructions):
            location_to_read_from_main_mem = instructions_to_read_these_locations_from_main_memory[test_number]
            expected_content = f"hello world #{location_to_read_from_main_mem}"
            
            # act
            cpu.read(location_to_read_from_main_mem)
            
            cache_snapshot: list[dict] = cpu.cache.get_current_cache()
            assert cache_snapshot[test_number]["tag"]  == location_to_read_from_main_mem
            assert cache_snapshot[test_number]["data"] == expected_content
    
    def test_read_up_to_cache_size(self,instructions_to_read_these_locations_from_main_memory):
        cpu = CPU()
        number_of_reads = cpu.cache.size
        
        for read_number in range(number_of_reads):
            location_to_read_from_main_mem = instructions_to_read_these_locations_from_main_memory[read_number]
            expected_content = f"hello world #{location_to_read_from_main_mem}"
            
            # act
            content_from_reading_main_mem = cpu.read(location_to_read_from_main_mem)
            
            # assert
            cache_snapshot: list[dict] = cpu.cache.get_current_cache()
            assert cache_snapshot[read_number]["tag"] == location_to_read_from_main_mem
            assert cache_snapshot[read_number]["data"] == expected_content   
    
    
        