# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        self.result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if end < cur_interval[0]:
                self.result.append([start, end])
                start = cur_interval[0]
                end = cur_interval[1]
            else:
                if end < cur_interval[1]:
                    end = cur_interval[1]
        self.result.append([start, end])
        return self.result

input = [[1, 4], [0, 4]]
result = Solution().merge(input)
print(result)

    # def merge(self, intervals):
    #     """
    #     :type intervals: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     if len(intervals) == 0:
    #         return []
    #     if len(intervals) == 1:
    #         return intervals
    #     self.result = []
    #     cur_idx = 0
    #     cur_interval = intervals[cur_idx]
    #     next_idx = 1
    #     while next_idx < len(intervals):
    #         next_interval = intervals[next_idx]
    #         if next_idx == len(intervals) - 1:
    #             if cur_interval[1] < next_interval[0]:
    #                 self.result.append(next_interval)
    #             else:
    #                 if cur_interval[1] < next_interval[1]:
    #                     cur_interval = [cur_interval[0], next_interval[1]]
    #                 else:
    #                     cur_interval = [cur_interval[0], cur_interval[1]]
    #                 self.result.append([cur_interval])
    #
    #         if cur_interval[1] < next_interval[0]:
    #             self.result.append(cur_interval)
    #             cur_interval = intervals[next_idx]
    #             next_idx += 1
    #         else:
    #             if cur_interval[1] < next_interval[1]:
    #                 cur_interval = [cur_interval[0], next_interval[1]]
    #                 next_idx += 1
    #             else:
    #                 cur_interval = [cur_interval[0], cur_interval[1]]
    #                 next_idx += 1
    #     return self.result

