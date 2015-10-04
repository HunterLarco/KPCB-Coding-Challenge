
def wrapped_range(range_size, start, traversal_length):
  if start > range_size: start %= range_size
  for i in range(traversal_length):
    yield (start + i) % range_size



def wrapping_generator(self, key):
  bucket_index = hash(key) % self.size
  for i in wrapped_range(self.size, bucket_index, self.size):
    bucket = self.buckets[i]
    yield (i, bucket)
    



class HashMap(object):
  
  def __init__(self, size):
    self.items   = 0
    self.size    = size
    self.buckets = [None] * size
  
  # returns bool if successful true else false
  def set(self, key, value):
    for i, bucket in wrapping_generator(self, key):
      if bucket is None:
        self.buckets[i] = [key, value]
        self.items += 1
        return True
      elif bucket[0] is key:
        bucket[1] = value
        return True
    return False
  
  # returns value or None
  def get(self, key):
    for i, bucket in wrapping_generator(self, key):
      if bucket is not None and bucket[0] is key:
        return bucket[1]
    return None
  
  # returns value or None
  def delete(self, key):
    for i, bucket in wrapping_generator(self, key):
      if bucket is not None and bucket[0] is key:
        value = bucket[1]
        self.items -= 1
        self.buckets[i] = None
        return value
    return None
  
  # returns float
  def load(self):
    return float(self.items) / self.size
  
  # returns None
  def clear(self):
    self.buckets = [None] * self.size
    self.items = 0
    
  


if __name__ == '__main__':
  print('<Begin Testing>')
  
  model = HashMap(10)
  model.set(1 , 'a')
  model.set(2 , 'b')
  model.set(3 , 'c')
  model.set(4 , 'd')
  model.set(5 , 'e')
  model.set(6 , 'f')
  model.set(7 , 'g')
  model.set(8 , 'h')
  model.set(9 , 'i')
  model.set(10, 'j')
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  model.set(10, 'first')
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  model.clear()
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  model = HashMap(10)
  model.set(1 , 'a')
  model.set(2 , 'b')
  model.set(3 , 'c')
  model.set(5 , 'e')
  model.set(6 , 'f')
  model.set(7 , 'g')
  model.set(8 , 'h')
  model.set(9 , 'i')
  model.set(10, 'j')
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  model.set('ah', 'd')
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  model = HashMap(10)
  model.set('a', 1 )
  model.set('b', 2 )
  model.set('c', 3 )
  model.set('d', 4 )
  model.set('e', 5 )
  model.set('f', 6 )
  model.set('g', 7 )
  model.set('h', 8 )
  model.set('i', 9 )
  model.set('j', 10)
  
  print(model.buckets)
  print(model.load())
  print(model.items)
  
  print(model.get('e'))
  print(model.get('j'))
  
  print(model.set('z', 1))
  print(model.delete('a'))
  print(model.load())
  print(model.set('z', 1))
  print(model.load())
  
  print('<End Testing>')