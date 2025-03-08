from memory import Memory, MainMemory

class Cache(Memory):
  def __init__(self, size:int = 4, associative_set:int = 1):
    super().__init__(name="Cache", access_time=0.5)
    self.main_memory = MainMemory()
    self.size = size
    self.fifo_index = 0
    self.cache_hit = 0
    self.cache_miss = 0 
    
    #TODO: able to configure cache's parameters from app.py and/or external file
    #TODO: generalise-able with log(associative_set, 2) is an integer
    if associative_set not in [1, 2, 4]:
      print("Unknown policy for cache's associativity. Revert to default policy: fully associative")
      associative_set = 1
    self.associative_set = associative_set # Set to 1, 2 or 4
    self.fifo_indices = [0, None, None, None]

    # Sets self.fifo_indicies based on 
    # the number of sets in the cache
    if self.associative_set == 2:
      self.fifo_indices = [0, 2, None, None]
    elif self.associative_set == 4:
      self.fifo_indices = [0, 1, 2, 3]
    
    self.data = [
      {"tag": None, "data": ""} for _ in range(self.size)
    ]

  def read(self, address: int):
    super().read()
    data = None
    entry = self.get_entry(address)
    if entry is not None:
      data = entry["data"]
    else:
      data = self.main_memory.read(address)
      self.replace_entry(address, data)

    return data

  def replace_entry(self, address: int, data: str) -> None:
    index = 0
    set_number = address % self.associative_set
    index = self.fifo_policy(set_number)
    set_data =  {"tag": address, "data": data}
    self.data[index] = set_data

  def random_policy(self, set_number):
    from random import randint
    if self.sets == 1:
      return randint(0, self.size-1)
    elif self.sets == 2:
      return randint(set_number*2, set_number*2+1)
    
    return set_number

  def fifo_policy(self, set_number: int) -> int:
    index: int = self.fifo_indices[set_number]
    self.fifo_indices[set_number] += 1
    magik:int = int(self.size/self.associative_set+(set_number*self.size/self.associative_set))
    if self.fifo_indices[set_number] == magik:
      self.fifo_indices[set_number] = set_number*int(self.size/self.associative_set)

    return index

  # Adds data in an empty entry
  def add_entry(self, address, data):
    for entry in self.data:
      if entry["tag"] == None:
        entry["tag"] = address
        entry["data"] = data
        return

  # Returns entry on cache hit
  # Returns None on cache miss
  def get_entry(self, address: int):
    for entry in self.data:
      if entry["tag"] == address:
          print(f"HIT: ", end="")
          self._count_hit()
          return entry

    print(f"MISS", end="")
    self._count_miss()
    return None

  def get_exec_time(self):
    exec_time = self.exec_time + self.main_memory.get_exec_time()
    return exec_time
  
  def get_current_cache(self) -> list:
    return self.data
  
  def _count_hit(self) -> None:
    self.cache_hit += 1
    
  def get_cache_hit(self) -> int:
    return self.cache_hit
  
  def _count_miss(self) -> None:
    self.cache_miss += 1
    
  def get_cache_miss(self) -> int:
    return self.cache_miss