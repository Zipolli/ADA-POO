from Aula.fibonacci_module import recur_fibo

n = 100
fib_series = [recur_fibo(i) for i in range(n)]
print(f"Série de Fibonacci com {n} números: {fib_series}")
