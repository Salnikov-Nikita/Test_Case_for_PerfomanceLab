import statistics
import sys
nums = [int(s) for s in open(sys.argv[1])]

result = statistics.median_high(nums)
count = 0
for i in nums:
    if i != result:
        count += abs(i - result)

print(count)
