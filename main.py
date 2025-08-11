from typing import List

def sorted_squares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    answer = []
    while left <= right:
        left_squared = nums[left] ** 2
        right_squared = nums[right] ** 2
        if left_squared > right_squared:
            answer.insert(0, left_squared)
            left += 1
        else:
            answer.insert(0, right_squared)
            right -= 1
    return answer

def reverse_string(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
