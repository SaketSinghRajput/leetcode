class Solution:
    def canPartitionKSubsets(self, nums, k):

        # Step 1: Find total sum
        total = sum(nums)

        # Step 2: Total must be divisible by k
        if total % k != 0:
            return False

        # Target sum of every subset
        target = total // k

        # Step 3: Largest number cannot be bigger than target
        if max(nums) > target:
            return False

        # Step 4: Sort in descending order
        nums.sort(reverse=True)

        # Step 5: Keep track of used elements
        used = [False] * len(nums)

        # Step 6: Backtracking function
        def backtrack(start, curr_sum, subsets):

            # Current subset is complete
            if curr_sum == target:

                # If only one subset remains,
                # all remaining elements must form it
                if subsets == 1:
                    return True

                # Start building the next subset
                return backtrack(0, 0, subsets - 1)

            # Try every unused element
            for i in range(start, len(nums)):

                # Element already used
                if used[i]:
                    continue

                # Don't exceed target
                if curr_sum + nums[i] > target:
                    continue

                # Choose nums[i]
                used[i] = True

                # Continue searching
                if backtrack(
                    i + 1,
                    curr_sum + nums[i],
                    subsets
                ):
                    return True

                # Undo choice
                used[i] = False

            return False

        # Start with k empty subsets
        return backtrack(0, 0, k)