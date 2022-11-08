def minRewards(scores):

    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i-1] + 1
    
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i],rewards[i+1]+1)
    
    return sum(rewards)

if __name__ == "__main__":
    arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    res = minRewards(arr)
    print(res)

1