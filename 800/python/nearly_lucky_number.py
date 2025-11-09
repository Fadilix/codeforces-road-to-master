n = int(input())

print("YES" if all(i == "7" or i == "4" for i in str(str(n).count("7") + str(n).count("4"))) else "NO")