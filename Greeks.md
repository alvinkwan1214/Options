# Greeks
## Delta 

Delta of an option describes the change of the option value in respect to the underlying
$$\Delta = \frac{\delta V}{\delta S}$$  V can be the value of a single contract or of a whole portfolio of contracts

It is used for [Delta Hedging](Delta%20Hedging.md) 

## Gamma
Gamma is the second derivative of the position with respect to the underlying, or it can also be seen as the sensitivity of delta to the underlying. 

$$\Gamma = \frac{\delta^2 V}{\delta S^2}$$

It is also showing how much/often a position must be rehedged in order to maintain a delta-neutral position.

In a delta-neutral position, gamma is partly repsonsible for making the return on the portfolio equal to the [Risk-free rate](Risk-free%20interest%20rate.md)

Also plays an important role when there is a mismatch between the market's view of volatility and the actual volatility of the underlying
## Theta
Theta is the rate of change of the option price with  time $$\Theta = \frac{\delta V}{\delta t}$$In a delta-hedged porfolio, the theta contributes to ensuring that the portfolio earns the risk-free rate - contributes in a completely certain way, unlike gamma which contributes the right amount on average.
## Vega

## Rho

