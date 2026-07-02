class Counter:
   count=0

   def __init__(self):
        Counter.count += 1

   @classmethod
   def total_objects(cls):
        return cls.count 
      
        
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()

print("Total objects created:", Counter.total_objects())