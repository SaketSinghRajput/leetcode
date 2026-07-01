class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] complement = new int[nums.length];

        int ind_1 = -1;
        int ind_2 = -1;

        // Store complements
        for (int i = 0; i < nums.length; i++) {
            complement[i] = target - nums[i];
        }

        // Find matching pair
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {

                if (i != j && nums[i] == complement[j]) {
                    ind_1 = i;
                    ind_2 = j;
                    return new int[] {ind_1, ind_2};
                }
            }
        }

        return new int[] {};
    }
}