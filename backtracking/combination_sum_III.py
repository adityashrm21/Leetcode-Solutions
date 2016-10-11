class Solution(object):
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 10)]):
            return []
        ans=[] 
        self.combs(k, n, ans, 1, [])
        return ans
        
    def combs(self, k, n, ans, curnum, path):
        if len(path)==k:
            if sum(path)==n:
                ans.append(list(path))
            return
        
        if len(path)>k or curnum>9:
            return

        for i in range(curnum, 10):
            path.append(i)
            self.combs(k, n, ans, i+1, path)
            path.pop()
            
