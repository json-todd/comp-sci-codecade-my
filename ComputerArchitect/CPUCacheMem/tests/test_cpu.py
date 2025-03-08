import sys, os
import pytest
from typing import List, Dict
print(f"\nPython path when \"{__file__}\" executed: {sys.path}")
from cpu import CPU

@pytest.fixture
def instructions_to_read_these_locations_from_main_memory() -> dict[int]:
    input_from_codecademy_exercises = [8,3,4,12,10,7,3,2,6,3,1,7,8,6]
    return input_from_codecademy_exercises

class TestCacheFullyAssociative:
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
    
    
class TestCache2WayAssociativity:
    @pytest.mark.parametrize(
        "test_case_name,test_input_instruction_to_read_main_mem_locations,expected_cache_results,expect_cache_hit,expect_cache_miss",
        [
            ("read_2_locations_each_start_of_different_associative_block",
             [0,1], [
                {'tag': 0, 'data': 'hello world #0'},
                {'tag': None, 'data': ''},
                {'tag': 1, 'data': 'hello world #1'},
                {'tag': None, 'data': ''}
            ], 0, 2),
            ("read_4_locations_to_cache_max_size",
             [0,1,2,3],[
                {'tag': 0, 'data': 'hello world #0'},
                {'tag': 2, 'data': 'hello world #2'},
                {'tag': 1, 'data': 'hello world #1'},
                {'tag': 3, 'data': 'hello world #3'}
            ], 0, 4),
            ("replace_fifo",
             [0,1,2,3,4,5,6,7],[
                {'tag': 4, 'data': 'hello world #4'},
                {'tag': 6, 'data': 'hello world #6'},
                {'tag': 5, 'data': 'hello world #5'},
                {'tag': 7, 'data': 'hello world #7'}
            ], 0, 8),
            ("having_cache_hit",
             [0,1,2,3,4,2],[
                {'tag': 4, 'data': 'hello world #4'},
                {'tag': 2, 'data': 'hello world #2'},
                {'tag': 1, 'data': 'hello world #1'},
                {'tag': 3, 'data': 'hello world #3'}
             ], 1, 5)
        ]
    )
    def test_cpu_read_and_cache_replace(self,
        test_case_name: str,
        test_input_instruction_to_read_main_mem_locations: List,
        expected_cache_results: List[Dict],
        expect_cache_hit: int,
        expect_cache_miss: int
    ):
        cpu = CPU(cache_associative_set=2)

        # act
        for test_read_location in test_input_instruction_to_read_main_mem_locations:
            cpu.read(test_read_location)    
        
        # assert
        got_cache_snapshot = cpu.cache.get_current_cache()
        assert_error_msg = f"{test_case_name} failed"
        assert str(got_cache_snapshot) == str(expected_cache_results), assert_error_msg 
        assert cpu.cache.cache_hit == expect_cache_hit, assert_error_msg
        assert cpu.cache.cache_miss == expect_cache_miss, assert_error_msg