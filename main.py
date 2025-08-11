from typing import List

def sorted_squares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    answer = []
    while left <= right:
        leftSquared = nums[left] ** 2
        rightSquared = nums[right] ** 2
        if leftSquared > rightSquared:
            answer.insert(0, leftSquared)
            left += 1
        else:
            answer.insert(0, rightSquared)
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
