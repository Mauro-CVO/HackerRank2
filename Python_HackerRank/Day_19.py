class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    
    def __init__(self):
        self.lst = list()
        #self.answer = 0
        #self.x 
        
    def divisorSum(self, n):
        answer = 0
        x = list(range(n+1))
        for i in x[1:]:
            if n%i == 0:
                self.lst.append(i)
            else:
                continue
        for i in self.lst:
            answer = answer + i
        return answer
                        


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)