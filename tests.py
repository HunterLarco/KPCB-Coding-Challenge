from hashmap import HashMap

def test():
  def verbose(hash_map):
    print(hash_map.buckets)
    print(hash_map.load())
    print(hash_map.items)

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
  
  assert model.get(1) == 'a'
  assert model.get(2) == 'b'
  assert model.get(3) == 'c'
  assert model.get(4) == 'd'
  assert model.get(5) == 'e'
  assert model.get(6) == 'f'
  assert model.get(7) == 'g'
  assert model.get(8) == 'h'
  assert model.get(9) == 'i'
  assert model.get(10) == 'j'
  
  model.set(10, 'first')
  
  assert model.get(10) == 'first'
  assert model.load() == 1
  
  model.clear()
  
  assert model.get(10) == None
  assert model.load() == 0
  
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
  
  assert model.get(3) == 'c'
  assert model.get(4) == None
  assert model.get(5) == 'e'
  assert model.load() == 0.9
  
  model.set('ah', 'd')
  
  assert model.get('ah') == 'd'
  assert model.load() == 1
  
  assert model.set('z', 1) == False
  assert model.delete(7) == 'g'
  assert model.load() == 0.9
  assert model.set('z', 1) == True
  assert model.load() == 1
  
  print('  ALL TESTS PASSED')
  print('</End Testing>')


if __name__ == '__main__':
  test()