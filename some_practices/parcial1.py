g = [1,2,3]
s = [1,1]

def galletas(g,s):
  for i in range(0, len(g)):
    sum = 0
    # Aca hacer multiples pasadas por el mismo valor
    for j in range(1, len(s)):
      if g[i] == s[j]:
        sum += 1
        print(sum)

galletas(g,s)