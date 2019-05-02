'''
Find if a given list/array of numbers includes 1 or more pythagorean triplets.
Time complexity: O(n*n)
'''

def containstriplet(nums):
	for i in range(len(nums)):
		nums[i]=nums[i]*nums[i];
	nums.sort()

	for i in range(len(nums)-1, 1, -1):
		j=0
		k=i-1
		while(j<k):
			if(nums[j]+nums[k]==nums[i]):
				return True
			elif(nums[i]>nums[j]+nums[k]):
				j+=1
			else:
				k-=1
	return False

input=[1,2,3,4,5,6,7,8,9]
if(containstriplet(input)):
	print("Yes")
else:
	print("No")
