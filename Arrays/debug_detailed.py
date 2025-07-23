class solution_debug:
    def product(self, nums):
        print(f"Input array: {nums}")
        n = len(nums)
        print(f"Array length: {n}")
        
        l_mult, r_mult = 1, 1
        l_arr, r_arr = [0]*n, [0]*n
        print(f"Initial l_arr: {l_arr}")
        print(f"Initial r_arr: {r_arr}")
        print(f"Initial l_mult: {l_mult}, r_mult: {r_mult}")
        print()
        
        for i in range(n):
            j = -i-1
            print(f"Iteration {i}: i={i}, j={j}")
            
            # Store current multipliers
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            print(f"  l_arr[{i}] = {l_mult}")
            print(f"  r_arr[{j}] = {r_mult}")
            
            # Update multipliers
            print(f"  Before update: l_mult={l_mult}, r_mult={r_mult}")
            l_mult *= nums[i]
            print(f"  l_mult *= nums[{i}] = {nums[i]} -> l_mult = {l_mult}")
            
            # BUG FOUND HERE! Missing assignment operator
            print(f"  r_mult * nums[{j}] = {r_mult} * {nums[j]} = {r_mult * nums[j]}")
            r_mult *= nums[j]  # This should be r_mult *= nums[j], not r_mult*nums[j]
            print(f"  After correction: r_mult = {r_mult}")
            
            print(f"  Current l_arr: {l_arr}")
            print(f"  Current r_arr: {r_arr}")
            print()
        
        print(f"Final l_arr: {l_arr}")
        print(f"Final r_arr: {r_arr}")
        
        result = [l*r for l, r in zip(l_arr, r_arr)]
        print(f"Final result: {result}")
        return result

def test_debug():
    print("=== Step-by-Step Debug ===")
    sol = solution_debug()
    result = sol.product([1, 2, 3, 4])
    print(f"Expected result for [1,2,3,4]: [24, 12, 8, 6]")
    print(f"Actual result: {result}")
    print()

if __name__ == "__main__":
    test_debug()
