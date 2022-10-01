两个有序数组的笛卡尔积的最大最小值
questions\0000\redo\2022.9.29\q2040.py
https://leetcode.com/contest/biweekly-contest-63/problems/kth-smallest-product-of-two-sorted-arrays/
···
        res =[]
        for i in nums1:
            res.append(i* nums2[0])
        for j in nums2:
            res.append(j * nums1[0])
        
        for i in nums1:
            res.append(i* nums2[-1])
        for j in nums2:
            res.append(j * nums1[-1])
        l = min(res)
        r =max(res)
···


## Timeout issue for using sortedlist

For qustion https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/submissions/

using sortedlist will timeout:
https://leetcode.com/submissions/detail/812406546/
questions\0000\redo\2022.9.29\q2071.sortedList.py

Using list will pass:
https://leetcode.com/submissions/detail/812409495/

questions\0000\redo\2022.9.29\q2071.py

## Timeout for DSU
如果用DSU加上DFS就会timeout questions\0000\redo\2022.9.29\q2092.py
https://leetcode.com/problems/find-all-people-with-secret/submissions/

using dijstra with time serialise (dijstra on multi-dimension group) questions\0000\redo\2022.9.29\q2092.2.py

可以使用DSU先合并后恢复的做法 questions\0000\redo\2022.9.29\q2092.dus2.py