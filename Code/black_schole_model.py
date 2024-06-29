import numpy as np 
import math
from scipy.stats import norm

N = norm.cdf #normal distrubution function

class testing():
    def __init__(self): 
        self.K = 40 #price of the underlying asset
        self.r = 0.1 #interest rate
        self.T = 0.5 #time (per annum)
        self.sigma = 0.2 #implied volatlity
        self.S = np.array([40,42,45]) #strike price


    def d1d2(self):
        d1 = (np.log(self.S/self.K) + (self.r + self.sigma**2/2)*self.T) / (self.sigma*np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2
    
    def call_payout(self, d1, d2):
        call = self.S * N(d1) - self.K * math.exp(-self.r * self.T) * N(d2)
        return call

    def put_payout(self, d1, d2):
        put = self.K * math.exp(-self.r * self.T) * N(-d2)  -  self.S * N(-d1)
        return put
    

if __name__ == "__main__":
    t = testing()
    d1, d2 = t.d1d2()
    print(t.call_payout(d1, d2))
    print(t.put_payout(d1, d2))




