'''
Find the k largest numbers in a given array of numbers
Time Complexity: O(nlogn)
'''
def klargest(k, arr):
	arr.sort()
	arr=arr[::-1]
	for i in range(k):
		print(arr[i])
	
input=[1,2,6,9,2134,65356,234324,12,34]
k=2
klargest(k,input)
