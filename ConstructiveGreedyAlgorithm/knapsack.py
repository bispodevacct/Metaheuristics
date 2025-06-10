import random
import time as t
import math

import os

# Criação da classe Mochila, a manipulação dos espaços será feita nos métodos da classe
class Knapsack:
    def __init__(self, capacity):   # Para instanciar uma mochila, precisamos apenas da capacidade dela
        self.capacity = capacity
    
    #Método do Simulated Annealing
    def simulatedAnnealing(self, profits, weights, time, temperature, coolingRate):
        self.calculate(profits, weights)
        
        start = t.time()
        temp = temperature

        s0 = self.selectedItems.copy()
        best = s0.copy()

        while (time > t.time() - start): #definimos um tempo que o Simulated Annealing permanecerá rodando
            s1 = self.newSolution(s0)

            s0Profit = self.evaluate(s0)
            s1Profit = self.evaluate(s1)

            if random.random() < self.temperatureAcceptance(s0Profit, s1Profit, temp):
                s0 = s1.copy()

                if self.evaluate(s0) > self.evaluate(best):
                    best = s0.copy()
            
            temp *= coolingRate

            print(s0Profit)
        
        self.selectedItems = best.copy()
    
    def calculate(self, profits, weights):
        self.putItems(profits, weights)
        self.sortItems()
        self.selectItems()
    
    def putItems(self, profits, weights):
        self.items = [(profits[i], weights[i], round(profits[i]/weights[i], 3)) for i in range(len(weights))]
    
    # Ordena os itens de acordo com o valor de valor/peso
    def sortItems(self):
        self.items = sorted(self.items, key = lambda tuple : tuple[2], reverse = True)
    
    # Seleciona os itens caso eles caibam dentro da capacidade da mochila
    def selectItems(self):
        self.selectedItems = [0 for i in range(len(self.items))]
        
        capacity = self.capacity

        for item in range(len(self.items)):
            if self.items[item][1] <= capacity:
                self.selectedItems[item] = 1
                capacity -= self.items[item][1]
    
    # Método para fazer a (possível) troca de bit de um item da solução
    def newSolution(self, solution):
        newSolution = solution.copy()

        item = random.randint(0, len(newSolution) - 1) # A escolha do item é feita de maneira aleatória dentro do tamanho da solução original

        if newSolution[item] == 0:
            newSolution[item] = 1
        else:
            newSolution[item] = 0
        
        return newSolution
    
    """  Método para conferir se a nova solução excede a capacidade da mochila.
     Se a solução excede ela é descartada e o método retorna 0, se não, retorna o valor total """
    def evaluate(self, solution):
        profit = 0
        weight = 0

        for item in range(len(solution)):
            profit += solution[item] * self.items[item][0]
            weight += solution[item] * self.items[item][1]
        
        if weight > self.capacity:
            return 0
        else:
            return profit
    
    """ Método temperatura sempre aceita a nova solução se o valor for maior que o anterior.
     Caso contrário, ela faz o calculo de probabilidade de aceite usando a temperatura ( Essa probabilidade permite que soluções piores sejam aceitas, especialmente em temperaturas mais altas.) """
    def temperatureAcceptance(self, s0Profit, s1Profit, temperature):
        if s1Profit > s0Profit:
            return 1.0
        else:
            return math.exp((s1Profit - s0Profit) / temperature)
    
    def getItems(self):
        try:
            return self.items
        except:
            print('There are no items!')
    
    def getSelectedItems(self):
        try:
            return self.selectedItems
        except:
            print('There are no selected items!')
    
    def getKnapsackProfit(self):
        knapsackProfit = 0

        for item in range(len(self.selectedItems)):
            knapsackProfit += self.selectedItems[item] * self.items[item][0]
        
        return knapsackProfit
    
    def getKnapsackWeight(self):
        knapsackWeight = 0

        for item in range(len(self.selectedItems)):
            knapsackWeight += self.selectedItems[item] * self.items[item][1]
        
        return knapsackWeight
