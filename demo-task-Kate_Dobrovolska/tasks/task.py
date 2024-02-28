from typing import Tuple, Optional
from math import sqrt

def solution(a, b, c) -> Optional[Tuple[int, int]]:

    result = None
    #Add your code here or ca;; it from here
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        result = (-b - sqrt(discriminant))/(2 * a), (-b + sqrt(discriminant))/(2 * a)
    if discriminant == 0:
        result = -b/(2 * a),
    print (result)
    
    return result

if __name__ == "__main__":
    assert solution(1, 6, 5) == (-5, -1)
    assert solution(1, 4, 4) == (-2,)
    assert solution(1, 6, 45) is None