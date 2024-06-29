# Options basics

**Call Options**: The right to buy a particular asset for an agreed amount at a specified time in the future

**Put Options**: The right to sell a particular asset for an agreed amount at a specified time in the future

**European Options**
**American Options**
## Common terms
**Premium**: The amount paid for the contract
**Underlying Price**: The financial instrument on which the option value depends on
**Strike Price**: The amount for which the underlying can be bought/sold
**Expiration**: Date on which the option can be exercised or date on which the option ceases to exist or give the holder any rights
**Intrinsic Value**: The payoff that would be received if the underlying is at its current leve when the option expires
**Time Value**: Any value that the option has above its intrinsic value
**In the money**: An option with positive intrinsic value - a call option when the assest price is above the strike; a put option when the asset price is below the strike
**Out of the money**: An option with no instrinsic value, only time value - a call option when the asset price is below the strike price; a put option when the assest price is above the strike 
**At the money**: A call or put with a strike price that is close to the current asset level\
**Long position**: A positive amount of a quantity, or a positive exposure to a quantity 
**Short position**: A negative amount of a quantity, or a negative exposure to a quantity



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
[Monte Carlo Simulation](Monte%20Carlo%20Simulation.md)

[Greeks](Greeks.md)


testing again
