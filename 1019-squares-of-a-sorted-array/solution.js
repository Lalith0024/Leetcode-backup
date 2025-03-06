/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    const ansarr = nums.map((val,indx)=>val*val)
    return ansarr.sort((a,b)=>a-b)
    
};
