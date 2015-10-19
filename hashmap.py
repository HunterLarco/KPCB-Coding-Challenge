class HashMap(object):
  """
  ' PURPOSE
  '   A fixed-size hash map that associates string keys
  '   with arbitrary data object references.
  """
  
  def wrapped_range(self, range_size, start, traversal_length):
    """
    ' PURPOSE *private helper method*
    '   Generates a circular range starting at 'start' with
    '   the length 'traversal_length' where at most the range
    '   can extend to 'range_size' (not inclusive) where the values
    '   will wrap.
    ' EXAMPLES
    '   1. wrapped_range where range_size=10, start=4, traversal_length=15
    '       -> [4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    '   2. wrapped_range where range_size=4, start=2, traversal_length=4
    '       -> [2, 3, 0, 1]
    ' PARAMETERS
    '   <int range_size>
    '   <int start>
    '   <int traversal_length>
    ' RETURNS
    '   <generator gen>
    """
    if start > range_size: start %= range_size
    for i in range(traversal_length):
      yield (start + i) % range_size

  def wrapping_generator(self, key):
    """
    ' PURPOSE *private helper method*
    '   Given a key, created an generator that starts at the bucket
    '   expected by hashing the key and then iterates (wrapping around
    '   the HashMap) until it reaches the bucket just before the expected
    '   bucket. AKA a circular mapping starting at the hashed value.
    ' PARAMETERS
    '   <hashable key>
    ' RETURNS
    '   <generator gen>
    """
    bucket_index = hash(key) % self.size
    for i in self.wrapped_range(self.size, bucket_index, self.size):
      bucket = self.buckets[i]
      yield (i, bucket)
  
  def __init__(self, size):
    """
    ' PURPOSE
    '   Return an instance of the class with pre-allocated
    '   space for the given number of objects.
    ' PARAMETERS
    '   <int size> The pre-allocated number of objects that
    '              may fit in this HashMap.
    ' RETURNS
    '   <HashMap map>
    """
    self.items   = 0
    self.size    = size
    self.buckets = [None] * self.size
  
  def set(self, key, value):
    """
    ' PURPOSE
    '   Stores the given key/value pair in the hash map.
    '   Returns a bool indicating success or failure.
    ' PARAMETERS
    '   <hashable key>
    '   <object value>
    ' RETURNS
    '   <bool success>
    '     True if the key/value pair was added
    '     False if the kye/value pair was not added (no room)
    ' NOTES
    '   1. If a key already exists in the HashMap, setting a
    '      new value will over-write the old value.
    """
    for i, bucket in self.wrapping_generator(key):
      if bucket is None:
        self.buckets[i] = [key, value]
        self.items += 1
        return True
      elif bucket[0] is key:
        bucket[1] = value
        return True
    return False
  
  def get(self, key):
    """
    ' PURPOSE
    '   Returns the value associated with the given key.
    '   If the key does not exist, None is returned.
    ' PARAMETERS
    '   <hashable key>
    ' RETURNS
    '   <object value> if the key exists
    '   None if the key does not exist
    """
    for i, bucket in self.wrapping_generator(key):
      if bucket is None: break
      if bucket[0] is key: return bucket[1]
    return None
  
  def delete(self, key):
    """
    ' PURPOSE
    '   Removes a key and its associated value from this
    '   HashMap. If the key is removed, the value is returned.
    ' PARAMETERS
    '   <hashable key>
    ' RETURNS
    '   <object value> if the key is deleted
    '   None if the key is not deleted
    """
    for i, bucket in self.wrapping_generator(key):
      if bucket is None: break
      if bucket[0] is key:
        value = bucket[1]
        self.items -= 1
        self.buckets[i] = None
        return value
    return None
  
  def load(self):
    """
    ' PURPOSE
    '   Returns the load factor, the fraction of buckets full
    ' PARAMETERS
    '   None
    ' RETURNS
    '   <float load>
    """
    return float(self.items) / self.size
  
  def clear(self):
    """
    ' PURPOSE
    '   Clears the HashMap's buckets.
    ' PARAMETERS
    '   None
    ' RETURNS
    '   None
    ' NOTES
    '   1. Preserves the amount of buckets
    """
    self.buckets = [None] * self.size
    self.items = 0
