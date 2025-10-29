# matrix = []

# for _ in range(5):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# ci, cj = float("inf"), float("inf")
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j] == 1:
#             ci, cj = i, j
#             break
#     if ci != float("inf") or cj != float("inf"):
#         break

# print(abs(2 - ci) + abs(2 - cj))


# udpated version

matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))
            exit()