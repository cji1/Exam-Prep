from pytest import raises
import random
import math
from simplemaths.simplemaths import SimpleMaths as sm

rand_int = random.randint(1, 12)
test_num = sm(rand_int)

class TestSimpleMaths():
    
    def test_constructor_pos(self):
        # positive constructor test for int type 
        assert type(test_num.number) == int
            
    def test_constructor_float(self):
        # negative constructor test for float input
        rand_float = random.uniform(1, 12)
        with raises(TypeError):
            a = sm(rand_float)

    def test_constructor_string(self):
        # positive constructor test for int type 
        rand_string = str(test_num)
        with raises (TypeError):
            b = sm(rand_string)
    
    def test_square(self):
        assert test_num.square() == test_num.number ** 2
    
    def test_factorial(self):
        test_fac = math.factorial(test_num.number)
        assert test_num.factorial() == test_fac
        
    def test_factorial_neg(self):
        test_num_neg = sm(0 - test_num.number)
        with raises(Exception):
           c =  test_num_neg.factorial()
            
    
    def test_power(self):
        rand_index = random.randint(1,5)
        assert test_num.power(rand_index) == test_num.number ** rand_index
    
    def test_power_2(self):
        test_num_neg = sm(0 - test_num.number)
        assert test_num_neg.power(2) == test_num.power(rand_index)
    
    def test_root(self):
        assert test_num.power(0.5) == math.sqrt(test_num.number)
        
    def test_root_neg
        with raises(ValueError):
            d = test_num_neg.power()
            
    def test_odd_or_even(self):
        #use modulo 2 as index for correct string
        even_odd_str = ["Even", "Odd"]
        test_odd_or_even = even_odd_str[test_num % 2]
        
        assert test_num.odd_or_even() == test_odd_or_even
        
    