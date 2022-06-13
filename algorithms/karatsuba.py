#implements karatsuba multiplication algorithm
from math import ceil, floor

def mul(x, y):
  if x<10 and y<10:
    return x*y
  n = ceil(len(str(x)))
  a = floor(x // (10**(n/2))) 
  b = x %  (10**(n/2))
  c = floor(y // (10**(n/2)))
  d = y %  (10**(n/2))
  print(a, b, c, d)  
  s1 = mul(a, c)
  s2 = mul(b, d)
  s3 = mul(a+b, c+d) - s2 - s1
  print(s1, s2, s3)
  return (10**n * s1) + (s3 * 10**(n/2)) + s2 
print(mul(1234, 5678))
