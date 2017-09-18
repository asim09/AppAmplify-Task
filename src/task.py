
from time import time

class Random(object):
    '''
    It generators multiple random numbers with biased higher and lower persentage.
    '''
    def __init__(self):
        pass

    def random(self, start, end):
        '''
        This function gives you random number b/w start and end.
        '''
        seed = time() * 1000000
        diff = end - start
        lower_random = seed % diff
        return int(start + lower_random)

    def random_with_limit(self, start, end, times, lower_persent, higher_persent):
        '''
        This function gives you final result and generate random numbers 73% biased to the higher number.
        '''
        result = []
        mid = (end - start) / 2 + start
        total_lower = int(round(times*lower_persent/100.0))
        total_higher = int(round(times*higher_persent/100.0))
        for i in range(total_lower):
            val = self.random(start, mid)
            result.append(val)
        for i in range(total_higher):
            val = self.random(mid, end)
            result.append(val)
        return result


if __name__ == "__main__":
    RN = Random()
    print (RN.random_with_limit(1, 95, 100, 27, 73))