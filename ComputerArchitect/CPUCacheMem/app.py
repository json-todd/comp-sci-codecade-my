from cache import Cache
from memory import MainMemory

class CPU:
  def __init__(self):
    self.cache = Cache()
    self.main_memo = MainMemory()
  
  def read(self, address) -> str:
    return self.cache.read(address)

def exercise1():
  instructions=[8,3,4,12,10,7,3,2,6,3,1,7,8,6]
  cpu = CPU()
  
  for instruction_index, location_to_read in enumerate(instructions):
    data_from_reading_location = cpu.read(location_to_read)
    
  print(f"Cache hit count: {cpu.cache.cache_hit}")
  print(f"Cache miss count: {cpu.cache.cache_miss}")
  print(f"Cache' tags: {list(entry['tag'] for entry in cpu.cache.data)}")
  print(f"Cache state: {cpu.cache.data}")

if __name__ == '__main__':
  exercise1()