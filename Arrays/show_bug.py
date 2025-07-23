class solution_original:
    def product(self, nums):
        n = len(nums)
        l_mult, r_mult = 1, 1
        l_arr, r_arr = [0]*n, [0]*n
        for i in range(n):
            j = -i-1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            
            l_mult *= nums[i]
            r_mult * nums[j]  # BUG: This line does nothing! Missing assignment
            
        return (l*r for l, r in zip(l_arr, r_arr))

def show_bug():
    print("=== Demonstrating the Bug ===")
    sol = solution_original()
    
    # Test with [1, 2, 3, 4]
    nums = [1, 2, 3, 4]
    result = list(sol.product(nums))
    
    print(f"Input: {nums}")
    print(f"Result with bug: {result}")
    print(f"Expected result: [24, 12, 8, 6]")
    print()
    
    # Let's trace what happens to r_mult
    print("Tracing r_mult values:")
    r_mult = 1
    for i in range(len(nums)):
        j = -i-1
        print(f"Iteration {i}: r_mult = {r_mult} (should multiply by nums[{j}] = {nums[j]})")
        # r_mult * nums[j]  # This does nothing!
        # r_mult remains unchanged
    
    print(f"Final r_mult: {r_mult} (should be {1*4*3*2*1})")

if __name__ == "__main__":
    show_bug()
