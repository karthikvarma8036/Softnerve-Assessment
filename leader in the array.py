def find_leaders(arr):
        n = len(arr)
        leaders = []
        max_right = float('-inf')    
        for i in range(n-1, -1, -1):
              if arr[i] > max_right:
                    max_right = arr[i]
                    leaders.append(arr[i])
        leaders.reverse() 
        return leaders
array = [7,10,4,10,6,5,2]
result = find_leaders(array)
print(result)

