#q3

import math

def q3_func():
    
    pow = 5 ** 7
    pow_root = pow ** 0.5
    
    log_pow_root = math.log(pow_root, 5)
    
    return log_pow_root


print "log_5(sqrt(5^7)):", q3_func()
