class EasyProblems{

    /*
    Given an array of integers nums and an integer target, return indices of the two
        numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not
        use the same element twice.
    You can return the answer in any order.

    3/28/2021
     */
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length-1; i++){
            for(int j = i+1; j < nums.length; j++)
                if(nums[i]+nums[j] == target)
                    return new int[]{i,j};
        }

        return new int[]{};
    }

    /*
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).
    Return the running sum of nums.

    4/25/21
     */
    public int[] runningSum(int[] nums) {
        for(int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }
        return nums;
    }

    /*
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".

    4/25/2021
     */
    public String defangIPaddr(String address) {
        String out = "";
        for(char ch: address.toCharArray()){
            if(ch == '.') {
                out += "[.]";
            } else {
                out += ch;
            }
        }
        return out;
    }

}

