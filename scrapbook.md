# 2025-03-01
**aims:** how do i know the code copy-pasted from codecademy work as expected, and when running with exercise' inputs the code results in the right answer?
i first seek understanding of the cache n-way set associative. i had one focus session about this last week.
then, i design test cases to prove that my understanding matches the code copy-pasted from codecademy.
after test pass, i can further run the code step-by-step in debug mode.
as a results, i confidently submit the answer.

## end-to-end test cases:
* empty cache, write an entry
* full cache, read an entry that will result in cache miss 
  * for example, cache saves the main mem's index as \[0,2,1,3\], when cpu is supposed to read from main mem index 4, then cache should replace cache's index 0 and becomes \[4,2,1,3\]. when cpu is supposed to read from main mem index 5, thn cache should replace cache's index 1 \[4,2,5,3\]
* test fifo replace policy in 2-way set associativity
  * i cannot simply instantiate a cpu with cache \[4,2,5,3]\ from scratch and test the fifo policy. because it will probably replace cache's index 0 and 2 first, as they will be recognized as the first-in. i have to set the internal's attribute of cache.fifo_policy, so the cache knows that cache's index 1 or 3 are actually the first-in, so next time when the cache misses it replaces index's 1 or 3
* Or, i will make 1 long scenarios that cover bth replace cache and test

# 2025-03-08
## end-to-end test cases:
* decide to cover fifo policy e2e by inputing 1 long sequence
```py
"test_input,expect_results,test_case_name",
([0,1,2,3,4,5,6],[
    {'tag': 4, 'data': 'hello world #4'},
    {'tag': 6, 'data': 'hello world #6'},
    {'tag': 5, 'data': 'hello world #5'},
    {'tag': 3, 'data': 'hello world #3'}
], "replace_fifo")
```
* \[ \] to add assert for cache hit

## configure for pytest
* add visibility on `sys.path` to debug the ImportModule error
* add `conftest.py` at the project's root and manually insert to path the project's directory
  