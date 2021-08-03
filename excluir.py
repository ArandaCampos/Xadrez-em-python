def fatorial(n, m = 1, resul = 1):
    if m > n:
        print(resul)
        return resul
    else:
        resul *= m
        fatorial(n, m + 1, resul)

n = int(input())
r = fatorial(n)
print(r)