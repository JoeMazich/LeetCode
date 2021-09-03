from ast import Num
from typing import List
import math

def twoSum0(nums: List[int], target: int) -> List[int]:
    
    for out1, int1 in enumerate(nums):
        new_target = target - int1
        if new_target in nums and nums.index(new_target) != out1:
            return [out1, nums.index(new_target)]

def twoSum1(nums: List[int], target: int) -> List[int]:
    all_complemnts = {}

    for index, num in enumerate(nums):
        complemnt = target - num
        if complemnt in all_complemnts:
            return [index, all_complemnts[complemnt]]
        else:
            all_complemnts[num] = index


def reverse0(x: int) -> int:
    if x == 0:
        return 0
    if x > 0:
        answer = int(str(x)[::-1])
    else:
        answer = -int(str(abs(x))[::-1])

    if abs(answer) < 2**31 and x != 2**31 - 1:
        return answer
    return 0

def reverse1(x: int) -> int:
    n_flag = False
    if x == 0 :
        return 0
    if x < 0:
        x = -x
        n_flag = True
    
    answer, x = 0, x * 10
    while ( (x := int(x / 10) ) != 0):
        answer = answer * 10 + x % 10 
    
    if answer > pow(2, 31) - 1 or answer < -pow(2, 32):
        return 0
    return answer if not n_flag else -answer
    
def isPalindrome0(x: int) -> bool:
    if x < 0: return False
    if x == 0: return True

    if reverse1(x) == x: return True
    else: return False

def isPalindrome1(x: int) -> bool:
    if x < 0: return False
    elif x == 0: return True
    length = int(math.log10(x))

    dividing = pow(10, length)

    for i in range(int((length + 1)/2)):
        right_digit = x % 10
        left_digit = int( (x / dividing) % 10 )
        if right_digit != left_digit: return False
        dividing /= 100
        x = int(x/10)

    return True

def romanToInt0(s: str) -> int:

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    answer, previous = 0, 0
    
    for numeral in reversed(s):
        if previous > roman_dict[numeral]:
            answer -= roman_dict[numeral]
        else:
            answer += roman_dict[numeral]
        previous = roman_dict[numeral]

    return answer

if __name__ == '__main__':
    print(isPalindrome1(0))
