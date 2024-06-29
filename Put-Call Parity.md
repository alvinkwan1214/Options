Buying 1 European Call option and 1 European Put [option](Options.md) both with a strike price E and expiry of T. The pay off of this portfolio is: 

$max(S(T) - E,0) - max(E - S(T), 0) = S(T) - E$

where $S(T)$ is the value of the underlying at time T

It shows that portfolio of a long call and a short put gives the same payoff as a long asset and short cash position 

The equality of these cashflows is independent of the future behaviour of the stock and is model independent: 

$C - P = S - Ee^{r(T-t)}$

where C and P are today's value of the call and the put respectively. If this relationship does not hold, there would be riskless [arbitrage](Arbitrage.md) opportunites.

