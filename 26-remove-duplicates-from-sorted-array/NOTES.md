In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted?
​
So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.
​
We can keep two pointers `i` and `j`, where `i` is the slow-runner while `j` is the fast-runner. As long as `nums[i] = nums[j]`, we increment `j` to skip the duplicate.
​
​