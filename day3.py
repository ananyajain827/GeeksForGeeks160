'''
You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
'''
class Solution:
    def reverseArray(self, arr):
        j=len(arr)-1
        i=0
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr