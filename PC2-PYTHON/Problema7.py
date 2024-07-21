def Num_perfecto(n):
    SumaDivisores = sum(i for i in range(1, n) if n % i == 0)
    return SumaDivisores == n

NumerosPerfectos = [n for n in range(1, 1000) if Num_perfecto(n)]
print("Números perfectos menores que 1000:", NumerosPerfectos)