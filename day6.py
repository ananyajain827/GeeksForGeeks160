'''
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
'''

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        if not arr:
            return[]
            
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in arr:
            if num==candidate1:
                count1 +=1
            elif num==candidate2:
                count2 +=1
            elif count1==0:
                candidate1, count1=num, 1
            elif count2==0:
                candidate2, count2=num, 1
            else:
                count1-=1
                count2-=1
                
        count1, count2=0,0
        for num in arr:
            if num==candidate1:
                count1 +=1
            elif num==candidate2:
                count2 +=1
                    
        n=len(arr)
        result=[]
        if candidate1 is not None and count1>n//3:
            result.append(candidate1)
        if candidate2 is not None and candidate2 != candidate1 and count2>n//3:
            result.append(candidate2)
                
        return sorted(result)

