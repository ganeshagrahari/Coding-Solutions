class solution:
    def product(self,nums):
        n = len(nums)
        l_mult,r_mult = 1,1
        l_arr,r_arr = [0]*n,[0]*n
        for i in range(n):
            j = -i-1
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult*=nums[i]
            r_mult*nums[j]

        return  (l*r for l, r in zip(l_arr,r_arr))

# Test the original code
def test_original():
    print("=== Testing Original Code ===")
    sol = solution()
    test_cases = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [1, 0, 3, 4]
    ]
    
    for nums in test_cases:
        print(f"Input: {nums}")
        try:
            result = sol.product(nums)
            print(f"Result type: {type(result)}")
            print(f"Result: {list(result)}")  # Convert generator to list
        except Exception as e:
            print(f"Error: {e}")
        print()

if __name__ == "__main__":
    test_original()
