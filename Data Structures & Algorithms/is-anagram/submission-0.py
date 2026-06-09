class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s1.sort()
        print("sorted s1 : ",)
        t1 = list(t)
        t1.sort()
        print("sorted t1 : ",t1 )
        if s1 == t1 : 
            return True
        else :
            return False


        

s = "racecar" 
t = "carrace"
sol = Solution()
sol.isAnagram(s,t)