
## [Xor subArray](algorithm/array/subarray/AndOrToK)


## Subset Or 之和

提示 1
对于异或运算，每个比特位是互相独立的，我们可以先思考只有一个比特位的情况，也就是 nums 中只有 0 和 1 的情况。（从特殊到一般）

在这种情况下，如果子集中有偶数个 1，那么异或和为 0；如果子集中有奇数个 1，那么异或和为 1。所以关键是求出异或和为 1 的子集个数。

设 nums 的长度为 n，且包含 1。我们可以先把其中一个 1 拿出来，剩下 n−1 个数随便选或不选，有 2**（n−1）种选法。

如果这 n−1 个数中选了偶数个 1，那么放入我们拿出来的 1（选这个 1），得到奇数个 1，异或和为 1。
如果这 n−1 个数中选了奇数个 1，那么不放入我们拿出来的 1（不选这个 1），得到奇数个 1，异或和为 1。
所以，恰好有 2 **（n−1）个子集的异或和为 1


注意这个结论与 nums 中有多少个 1 是无关的，只要有 1，异或和为 1 的子集个数就是 2 **(n−1)。如果 nums 中没有 1，那么有 0 个子集的异或和为 1。

所以，在有至少一个 1 的情况下，nums 的所有子集的异或和的总和为2**（n−1）

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << (len(nums) - 1)

<!-- 作者：灵茶山艾府
链接：https://leetcode.cn/problems/sum-of-all-subset-xor-totals/solutions/3614974/on-shu-xue-zuo-fa-pythonjavaccgojsrust-b-9txy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 -->