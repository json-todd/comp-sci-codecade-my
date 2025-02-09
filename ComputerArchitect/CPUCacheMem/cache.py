from memory import Memory, MainMemory

class Cache(Memory):
  def __init__(self):
    super().__init__(name="Cache", access_time=0.5)
    self.main_memory = MainMemory()
    self.fifo_index = 0
    self.cache_hit = 0
    self.cache_miss = 0 
    
    self.data = [
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
      {"tag": None, "data": ""},
    ]

  def read(self, address):
    super().read()
    data = None
    entry = self.get_entry(address)
    if entry is not None:
      data = entry["data"]
    else:
      data = self.main_memory.read(address)
      self.replace_entry(address, data)

    return data

  def replace_entry(self, address, data):
    index = self.fifo_policy()
    self.data[index] = {"tag": address, "data": data}

  def random_policy(self):
    from random import randint
    return randint(0, len(self.data)-1)

  def fifo_policy(self):
    index = self.fifo_index
    self.fifo_index += 1
    if self.fifo_index == len(self.data):
      self.fifo_index = 0

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
  def get_entry(self, address):
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
    
  def get_cache_miss(self) -> None:
    return self.cache_miss