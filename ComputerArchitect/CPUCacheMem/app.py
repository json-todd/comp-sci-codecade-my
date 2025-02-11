from cache import Cache
from memory import MainMemory

class CPU:
  def __init__(self, cache_associative_set: int = 1):
    self.cache = Cache(associative_set=cache_associative_set)
    self.main_memo = MainMemory()
  
  def read(self, address) -> str:
    return self.cache.read(address)

def exercise1():
  instructions=[8,3,4,12,10,7,3,2,6,3,1,7,8,6]
  cpu = CPU()
  
  for location_to_read in enumerate(instructions):
    cpu.read(location_to_read)
    
  print()
  print(f"Cache hit count: {cpu.cache.cache_hit}")
  print(f"Cache miss count: {cpu.cache.cache_miss}")
  print(f"Cache' tags: {list(entry['tag'] for entry in cpu.cache.data)}")
  print(f"Cache state: {cpu.cache.data}")
  
def exercise2():
  instructions=[8,3,4,12,10,7,3,2,6,3,1,7,8,6]
  cpu = CPU(cache_associative_set=2)
  
  for location_to_read in instructions:
    cpu.read(location_to_read)
  
  print() 
  print(f"Cache hit count: {cpu.cache.cache_hit}")
  print(f"Cache miss count: {cpu.cache.cache_miss}")
  print(f"Cache' tags: {list(entry['tag'] for entry in cpu.cache.data)}")
  print(f"Cache state: {cpu.cache.data}")

if __name__ == '__main__':
  exercise2()