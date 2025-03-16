class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        array_length = len(arr)
        current_pointer = array_length - 1
    
        while current_pointer >= 0:
            if current_pointer + zeros < array_length:
                arr[current_pointer + zeros] = arr[current_pointer]
            
            if arr[current_pointer] == 0:
                zeros -= 1
                if current_pointer + zeros < array_length:
                    arr[current_pointer + zeros] = 0
            
            current_pointer -= 1
