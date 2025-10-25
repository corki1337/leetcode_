class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        suma = numBottles
        puste = numBottles
        while puste >= numExchange:
            suma += puste // numExchange
            puste = puste // numExchange + puste % numExchange
            
        return suma