mod = int(1e9)+7
n = int(input())
arr = [0]+list(map(int,input().split()))
print(arr)
cnt = [1,0]
dp = [0]*(n+1)
print(dp)
sm=ans=0
for i in range(1,n+1):
    sm += arr[i]
    sm %= 2
    dp[i] += cnt[sm]+dp[i-1]
    cnt[sm] += 1
cnt = [1,0]; sm=0
for i in range(n,0,-1):
    sm += arr[i]
    sm %= 2
    ans += dp[i-1]*cnt[sm]
    ans %= mod
    cnt[sm] += 1
print(ans)