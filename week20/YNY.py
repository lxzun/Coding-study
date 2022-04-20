class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int(''.join(str(_) for _ in digits))
        nums += 1
        ans = []
        for i in str(nums):
            ans.append(int(i))
        return ans
        
        
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timePoints.append(timePoints[0])
        ans = 1440
        for i in range(len(timePoints)-1):
            first = timePoints[i].split(':')
            second = timePoints[i+1].split(':')
            first_m = int(first[-1])
            first_m += int(first[0]) * 60

            second_m = int(second[-1])
            second_m += int(second[0]) * 60

            ans_ = abs(second_m - first_m)
            ans_ = min(ans_, abs(ans_ - 1440))
            if ans_<ans:
                ans = ans_
        return ans
