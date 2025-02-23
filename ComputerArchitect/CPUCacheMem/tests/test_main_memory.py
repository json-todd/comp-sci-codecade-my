import pytest

class TestMainMemory:
    @pytest.mark.parametrize(
        "cache_size, cache_associative_set_size, main_mem_size",
        [(case_cache_size, case_cache_associative_set_size, case_main_mem_size)
         for case_cache_size in [4]
         for case_cache_associative_set_size in [4,2,1]
         for case_main_mem_size in [16] ]
    )
    def test_reduce_any_index_to_a_base_index(self, cache_size, cache_associative_set_size, main_mem_size):
        # arrange
        number_of_cache_associative_sets = cache_size / cache_associative_set_size
        all_main_mem_index = range(main_mem_size)
        test_results = []
        
        for a_main_mem_index in all_main_mem_index:
            # act
            got_base_index = a_main_mem_index % number_of_cache_associative_sets
            test_results.append({
                "main_mem_index": a_main_mem_index,
                "got_base_index": got_base_index,
                "number_of_cache_associative_sets": number_of_cache_associative_sets,
                "test_result": got_base_index <= number_of_cache_associative_sets-1 # minus 1 becaues index starts at 0
            })
            
        # assert
        for _test_case in test_results:
            assert _test_case['test_result'], f"Not all test case pass. Failed at {_test_case}"
        
        # finally
        # for _test_case in test_results:
        #     print(
        #         f"{_test_case['main_mem_index']} -- {_test_case['number_of_cache_associative_sets']} --> {_test_case['got_base_index']}"
        #     )
        
        
        
if __name__ == '__main__':
    def main():
        for case_main_mem_size in [16]:
            for case_number_of_cache_associative_set in [1,2,4]: 
                all_main_mem_index = range(case_main_mem_size)
                for a_main_mem_index in all_main_mem_index:
                    base_main_mem_index = a_main_mem_index % case_number_of_cache_associative_set
                    print(
                        f'{a_main_mem_index} -- {case_number_of_cache_associative_set} --> {base_main_mem_index}'
                    )
                    
    
    main()
        
        
        