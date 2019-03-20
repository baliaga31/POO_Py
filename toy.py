class Toy ():
  def __init__(self, name, size):
    self.toy = name
    self.size = size

class Horse(Toy):
  def __init__(self, size):
    super(Horse, self).__init__('Horse', 2)
    super(Horse, self).talk()

class Doll(Toy):
  def __init__(self, size):
    super(Doll, self).__init__('Doll', 1)

class Car(Toy):
  def __init__(self, size):
    super(Car, self).__init__('Car', size)
    
class Factory():
  def __init__(self):
    pass

  def create_toy(self, type, size=1):
    return type(size)

if __name__ == '__main__':
  t = Toy('cqr', 2) # --> a = new Toy();   a.__init__(a, 'cqr'); return a 
  print(t.toy)
  print(hasattr(t, 'test'))
  print(t.talk()) # cqr
  print(isinstance(h, Toy))
  print(isinstance(h, Horse))
  f = Factory()
  h = f.create_toy(Horse size=1)
  f = f.create_toy(Car, size=10)
