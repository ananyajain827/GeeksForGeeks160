'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
'''
class Solution:
    def getSecondLargest(self, arr):
        first=second=-1
        for num in range(len(arr)):
            if num>first:
                first=second
                num=first
            elif num>second and num!=first:
                num=second
        return second
                

