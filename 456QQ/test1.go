func find132pattern(nums []int) bool {
	if len(nums) < 3 {
		return false
	}
	sta := make([]int, 0)
	second := -10000000000
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] < second {
			return true
		}
		for len(sta) > 0 && sta[len(sta)-1] < nums[i] {
			second = sta[len(sta)-1]
			sta = sta[:len(sta)-1]
		}
		sta = append(sta, nums[i])
	}
	return false
}