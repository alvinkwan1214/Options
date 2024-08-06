Also known as historical volatility or realised volatility, 

- **Definition**: Historical volatility is the standard deviation of past price movements (returns) of a stock over a specific period.
- **Calculation**: It's calculated based on historical price data, as shown in the previous example.
- **Purpose**: It measures how much a stock's price has fluctuated in the past and is backward-looking.
- **Use Case**: Investors and analysts use historical volatility to understand past price behavior and to make assumptions about future volatility, although it does not predict future volatility directly.


To find the actual volatility: 

**Obtain Historical Price Data:**

Collect historical price data for the stock. The data typically includes daily closing prices, but you can use other frequencies like weekly or monthly data depending on your needs.

**Calculate Returns:**

Calculate the daily (or periodic) returns of the stock. The most common method is to use the logarithmic return, which is given by:
$$
\text{Return}_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

Where $P_t$ is the price at time $t$, and $P_{t-1}$ is the price at time $t-1$.

**Calculate the Mean Return (Optional):**

Calculate the mean of the returns over the period. This step is optional because volatility is usually calculated based on deviations from the mean.

**Calculate the Standard Deviation of Returns:**

The standard deviation of the returns over the chosen period is the volatility. This can be annualized to represent annual volatility.

The formula for standard deviation (volatility) is:

$$
\sigma = \sqrt{\frac{1}{N-1} \sum_{t=1}^{N} \left(R_t - \bar{R}\right)^2}
$$

Where:

$N$ is the number of observations (e.g., days).

$R_t$ is the return at time $t$.

$\bar{R}$ is the average return over the period.

**Annualize the Volatility:**

If you're working with daily returns, you can annualize the volatility using the following formula:

$$
\text{Annualized Volatility} = \sigma \times \sqrt{252}
$$

Where 252 represents the approximate number of trading days in a year.

