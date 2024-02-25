qtdCarros = input()
carros = list(map(int, input().split()))
tempos = list(map(float, input().split()))

# Lista de tuplas e ordenando com sorted
ordenado = sorted(list(zip(carros, tempos)), key=lambda x: x[1]) 
[print(f'Carro #{carro[0]}: Tempo {carro[1]:.1f} segundos') for carro in ordenado]
