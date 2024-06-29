# Options
Look into different option pricing methods and greeks

Black-Scholes equation
Pay off of a European Call option:

$C(T) = max(S(T) - K , 0)$

Black-Scholes formula for the price of the call option at date t = 0 prior to maturity is given by

$c(0) = S(0)N(d_1) − e^{−rT}KN(d_2)$

$d_1 = \frac{\ln({S(0)/K}) + (r + \sigma^2/2)T}{\sigma \sqrt(T)}$   

$d_2 =  d_1 - \sigma \sqrt(T)$   

Pay off a European Put option: 

$P(T) = max[K − S(T), 0]$

Black-Scholes formula foe the price of the put option at date t = 0 is written as:

$p(0) = e^{−rT}KN(-d_2) -  S(0)N(-d_1)$

Assumptions: 
In a risk-neutrial wrold all assests earn the risk-free rate

Assuming the logartihm of the stock price is normally distributed


[Numerical Methods](Numerical%20Methods.md)
[Binary Tree](Binary%20Tree)
[[Monte Carlo Simulation]]


testing


