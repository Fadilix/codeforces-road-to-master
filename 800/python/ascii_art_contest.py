scores = list(map(int, input().split()))

m = min(scores)
mx = max(scores)

if mx - m >= 10:
    print("check again")
else:
    scores.sort()
    print(f"final {scores[len(scores) // 2]}")