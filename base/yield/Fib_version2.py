class Fib(object):  
    """docstring for my_iterator"""  
    def __init__(self, num):  
        super(Fib, self).__init__()  
        self.num = num  
        self.n, self.a, self.b = 0, 0, 1  
  
    def next(self):  
        if self.n < self.num:  
            result = self.b  
            self.a, self.b = self.b, self.a + self.b  
            self.n += 1  
            return result  
        raise StopIteration  
  
    def __iter__(self):  
        return self  
  
  
def main():  
    for result in Fib(5):  
        print(result)

