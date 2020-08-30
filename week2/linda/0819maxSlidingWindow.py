class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:  # 判空
            return []

        stack = []
        for i in range(k):  # 滑动指针，开始形成第一个窗口
            while stack and stack[-1] < nums[i]:  # 保证递减性
                stack.pop()
            stack.append(nums[i])

        result = [stack[0]]
        for j in range(k, len(nums)):  # 滑动窗口
            if stack[0] == nums[j - k]:  # 窗口起点的下标超过最大值的下标时，舍弃最大值
                stack = stack[1:]
            while stack and stack[-1] < nums[j]:  # 舍弃小于nums[j]的值，保证递减性
                stack.pop()
            stack.append(nums[j])
            result.append(stack[0])

        return result

