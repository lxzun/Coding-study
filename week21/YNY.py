class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        check_point = [-1]
        for i in range (len(s)-1):
            if s[i]+s[i+1]=='01' or s[i]+s[i+1]=='10':
                check_point.append(i)
        check_point.append(len(s)-1)

        for check_idx in range(0,len(check_point)-2):
            ans += min(check_point[check_idx+1]-check_point[check_idx],check_point[check_idx+2]-check_point[check_idx+1])
        return ans
      
      
      

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        max_beans = sum(beans)
        ans = sum(beans)
        for i in range (len(beans)):
            target = max_beans - (len(beans)-i)*beans[i]
            ans = min(ans,target)
        return ans
