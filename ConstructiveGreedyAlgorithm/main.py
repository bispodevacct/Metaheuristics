# Problema da Mochila
# Alunos: Isabelle Vimercati e Marcus Bispo

import knapsack as k

weights = []
profits = []

#Capturando as informações do arquivo txt
with open("items.txt", "r") as f:
    knapsackCapacity = int(f.readline().strip())
    for line in f:
        w, pr = map(int, line.strip().split())      
        weights.append(w)
        profits.append(pr)

knapsack = k.Knapsack(knapsackCapacity)
# knapsack.calculate(profits, weights)
knapsack.simulatedAnnealing(profits, weights, 10, 100, 0.99)

""" print(f'Items: {knapsack.getItems()}')
print(f'Selected items: {knapsack.getSelectedItems()}')
print(f'Knapsack profit: {knapsack.getKnapsackProfit()}')
print(f'Knapsack weight: {knapsack.getKnapsackWeight()}') """