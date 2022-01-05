class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0, high = nums.length-1;
        int mid = low+(high-low)/2;;
        while(low<=high) {
            if (nums[mid] == target) 
                break;
            else {
                if (nums[mid] < target) 
                    low = mid + 1;
                else
                    high = mid - 1;
            }
            mid = low+(high-low)/2;
        }
        return mid;
    }
}
