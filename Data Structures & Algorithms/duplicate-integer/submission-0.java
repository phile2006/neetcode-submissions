class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i= 0; i<nums.length; i++){
            int check = nums[i];
            for(int j = 0; j<nums.length; j++){
                if(i == j){
                    break;
                }
                if(check == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}