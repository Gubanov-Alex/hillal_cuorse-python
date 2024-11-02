class Counter:
   """Create counter"""

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value
       self._validate_current()


   def set_current(self, start):
       """Set current value"""
       self.current = start
       self._validate_current()


   def set_max(self, max_max):
       """Set max value"""
       self.max_value = max_max
       self._validate_current()


   def set_min(self, min_min):
       """Set min value"""
       self.min_value = min_min
       self._validate_current()


   def step_up(self):
       """Step up = 1"""
       if self.current >= self.max_value:
           raise ValueError("Ты куда полетел,стоп!")
       self.current += 1


   def step_down(self):
       """Step down = -1"""
       if self.current <= self.min_value:
          raise ValueError("Мы на дне,спасайтесь братцы!")
       self.current -= 1


   def get_current(self):
       """Get current value"""
       return self.current


   def _validate_current(self):
       """Validate if current is in the valid range [min_value, max_value]"""
       if not (self.min_value <= self.current <= self.max_value):
           raise ValueError("Пиши в диапазоне салага!")

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'


try:
    counter_2 = Counter(50,40,54)
    counter_2.step_down()
    counter_2.step_down()
    counter_2.step_down()
    assert counter_2.get_current() == 47, 'Test7'
    print(counter_2.get_current())
    counter_2.set_current(35)
except ValueError as e:
    print(e)



