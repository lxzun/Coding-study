class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        broken = list(brokenLetters.strip())
        ans = len(text)
        for i in broken:
            for idx , j in enumerate(text):
                if i in j:
                    ans -= 1
                    text[idx]=''
                    continue
        return ans
    
    
    
    
    
    
    
class TweetCounts:

    def __init__(self):
        self.info = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int):
        insort(self.info[tweetName],time) # 정렬해서 삽입

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = []
        if freq == 'minute':
            sec = 60
        elif freq == 'hour':
            sec = 3600
        else:
            sec = 86400
            
        while startTime <= endTime:
            end = min(startTime + sec, endTime + 1) # 단위로 쪼개서
            ans.append(bisect_left(self.info[tweetName],end) - bisect_left(self.info[tweetName],startTime))
            startTime += sec
        return ans
