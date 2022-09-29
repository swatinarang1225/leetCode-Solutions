class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = []
        n = len(arr)
       
        def SearchCrossOver (arr,l,r,x):
            if arr[r] <= x:
                return r
            if arr[l] >x:
                return l
            mid = (r+l) //2
            
            if arr[mid]<= x and arr[mid+1] > x:
                return mid
            
            if (arr[mid]<x):
                return SearchCrossOver(arr,mid+1,r,x)
            
            return SearchCrossOver(arr,l,mid-1,x)
            
        
        def result(arr,x,n,k):
            i = SearchCrossOver(arr,0,n-1,x)
            
            j = i+1
            count = 0
            if arr[i] == x:
                output.append(x)
                i -= 1
                
            while((i>=0 and j <n) and len(output)< k):
                a = arr[i]
                b = arr[j]
                if (abs(a-x) <= abs(b-x)) and a<b:
                    output.append(a)
                    i -= 1
                else:
                    output.append(b)
                    j += 1
            while(len(output) < k and i<0):
                c = arr[j]
                output.append(c)
                j +=1
        
            while(len(output) < k and j>=n):
                c = arr[i]
                output.append(c)
                i -=1
          
            return sorted(output)
                
        return result(arr,x,n,k)

       
            

            
