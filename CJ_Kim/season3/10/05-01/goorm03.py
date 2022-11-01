# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

row_num = int(input())
dp = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
more_dp = [[] for _ in range(100000)]
dp += more_dp

get_prev = [[0, 1, 2, 3, 4], [0, 2, 3], [0, 1, 3, 4], [0, 1, 2], [0, 2]]

answer = 0
for j in range(2, row_num+1):
	next_dp = []
	for i in range(5):
		next_sum = 0
		for k in get_prev[i]:
			next_sum+=dp[j-1][k]
		next_dp.append(next_sum)
	dp[j]=next_dp

print(sum(dp[j])%100000007)

# ------정답---------
n = int(input())
dp = [[0]*5 for i in range(n+1)]
for i in range(5):
    dp[1][i] = 1
for i in range(2, n+1):
    # 실제 코드에서는 인덱스 때문에, DP[1][0] ~ DP[1][4]로 설정했습니다.
    dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%100000007
    dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3])%100000007
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4])%100000007
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%100000007
    dp[i][4] = (dp[i-1][0] + dp[i-1][2])%100000007
print((dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3] + dp[n][4])%100000007)