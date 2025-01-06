import numpy as np 
from scipy.stats import norm
N = norm.cdf #normal distrubution function

def eu_option(strike_price, underlying, option_type, position, cost=0):
    if position == "long":
        if option_type == "Call":
            return np.maximum(underlying - strike_price, 0) - cost
        elif option_type == "Put":
            return np.maximum(strike_price - underlying, 0) - cost
        else: 
            return "Please input the correct type of options"
    elif position == "short":
        if option_type == "Call":
            return np.minimum(strike_price - underlying, 0) + cost
        elif option_type == "Put":
            return np.minimum(underlying - strike_price, 0) + cost
        else: 
            return "Please input the correct type of options"

def futures(future_price, underlying, position):
    if position == "long":
        return underlying - future_price
    elif position == "short":
        return future_price - underlying
    else: 
        return "Please input the correct type of options"

def normal_stock(original_price, underlying):
    return underlying - original_price


def futures_value(spot_price, t, model = "COC model", r = 0, income_yield = 0, I = 0):
    if model == "CoC model":
        return spot_price * np.exp((r - income_yield) * t)
    if model == "known-cash income":
        return (spot_price - I) * np.exp(r * t)
    
def present_value(c, r, t_lis):
    cur = 0
    for t in t_lis:
        cur += c * np.exp(-r * t)
    return cur

def future_value(original_price, current_price, r, delta_t,other=0):
    return -(current_price - original_price*np.exp(-r * delta_t) - other)

def options_value(underlying, strike, t, r, sigma, option_type):
    d1 = (np.log(underlying/strike) + (r + sigma**2/2)*t) / (sigma*np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    if option_type == "Call":
        call_value  =  underlying * N(d1) - strike * np.exp(-r*t)* N(d2)
        return call_value
    if option_type == "Put":
        put_value  =  strike*np.exp(-r*t)*N(-d2) - underlying*N(-d1)
        return put_value
    