class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        """
        3 4 1 2 5 7 3
        pivot = 3

        3 3 1 2 5 7 4

        left = i + 1
        while left < pivot:
            left ++
            if left :
                break
        while right > pivot:
            right --
            if right == left:
                break
        
        """ 

        # def quicksort(l, r, arr):
        #     if r - l <= 0:
        #         return

        #     index = l + (r-l)//2
        #     arr[l], arr[index] = arr[index], arr[l]
        #     pivot = arr[l]  # Use the first element of the subarray as pivot
        #     left = l + 1
        #     right = r   # assuming r is exclusive; if inclusive, adjust accordingly

        #     while left <= right:
        #         while left <= right and arr[left] < pivot:
        #             left += 1
        #         while left <= right and arr[right] > pivot:
        #             right -= 1

        #         if left <= right:
        #             arr[left], arr[right] = arr[right], arr[left]
        #             left += 1
        #             right -= 1
        #     # Place pivot in its correct position
        #     arr[l], arr[right] = arr[right], arr[l]

        #     quicksort(l, right, arr)
        #     quicksort(right + 1, r, arr)

        # quicksort(0,len(nums) - 1, nums)
        # return nums

        def mergesort(arr):
            if len(arr) == 1:
                return arr

            left = mergesort(arr[0:len(arr)//2])
            right = mergesort(arr[len(arr)//2:])

            l = 0
            r = 0
            while l <len(left) and r <len(right):
                if left[l] <= right[r]:
                    arr[l + r] = left[l]
                    l+=1
                else:
                    arr[l + r] = right[r]
                    r+=1
            while l < len(left):
                arr[l + r] = left[l]
                l +=1
            while r < len(right):
                arr[l + r] = right[r]
                r+=1
            return arr
        return mergesort(nums)