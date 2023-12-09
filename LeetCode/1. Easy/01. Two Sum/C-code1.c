/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// nums=number array, numsSize=size of array
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* result = (int*)malloc(sizeof(int)*2);
    // 1. Check malloc
    if(!result) return NULL;
    // 2. Check Sum
    int i, j;
    for(i=0;i<numsSize-1;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                *returnSize=2;
                result[0]=i;
                result[1]=j;
                return result;
            }
        }
    }
    // 3, There's no case
    *returnSize=0;
    return NULL;
}
