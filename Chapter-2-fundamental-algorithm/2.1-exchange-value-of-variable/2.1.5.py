'''
What happens when the argument given to the procedure exchange are i and a[i]?

'''

 

def exchange_variable(arr, i):
    if i < len(arr):
    	print(f'Before exchange : arr[{i}] = {arr[i]}, arr[arr[{i}]] = {arr[arr[i]]}')

    	arr[i], arr[arr[i]] = arr[arr[i]], arr[i]

    	print(f'Afetr exchange : arr[{i}] = {arr[i]}, arr[arr[{i}]] = {arr[arr[i]]}')


my_array = [1, 2, 3, 4, 5]
i = 2        # index i

exchange_variable(my_array, i)
