class Solution:
    def findMissing(self, arr, n):
        # code here
        temp = arr[0]
        d = (arr[-1] - arr[0]) // n
        
        for i in range(n-1):
            temp = arr[i] + d
            if arr[i] + d != arr[i+1]:
                return temp