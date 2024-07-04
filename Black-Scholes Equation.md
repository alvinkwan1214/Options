# Black-Scholes Equation
## Basics

Black-Scholes equation
Pay off of a European Call option:

$C(T) = max(S(T) - K , 0)$

Black-Scholes formula for the price of the call option at date t = 0 prior to maturity is given by

$c(0) = S(0)N(d_1) − e^{−rT}KN(d_2)$

$d_1 = \frac{\ln({S(0)/K}) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt(T)}$   

$d_2 =  d_1 - \sigma \sqrt(T)$   

Pay off a European Put option: 

$P(T) = max[K − S(T), 0]$

Black-Scholes formula foe the price of the put option at date t = 0 is written as:

$p(0) = e^{−rT}KN(-d_2) -  S(0)N(-d_1)$




Sigma is the [Implied Volatility](Implied%20Volatility.md)


For a working example of the Black-Scholes equations, see
[Black-Scholes Code](Options\Code\black_schole_model.py)


## Assumptions
The underlying follows a lognormal random walk

The [risk-free interest rate](Risk-free%20interest%20rate.md) is a known function of time

Delta hedging is done continously

No transaction cost on the underlying

No arbitrage opportunities: [Put-Call Parity](Put-Call%20Parity.md)



## Derivation



## Variations
### Options on Dividend-Paying Equities
### Currency Options
### Commondity Options
### Options on Futures

