# Explicit Method
[Finite Difference Method](Finite%20Difference%20Method.md)

The [Black-Scholes Equation](Black-Scholes%20Equation.md) without considering dividends is:
$$\frac{\delta V} {\delta t} + \frac{1}{2}\sigma^2S^2 \frac{\delta^2  V} {\delta S^2}+ rS\frac{\delta V} {\delta S } - rV = 0$$
It can be written in a more general form:
$$\frac{\partial V}{\partial t} + a(S,t) \frac{\partial^2 V}{\partial S^2} + b(S,t) \frac{\partial V}{\partial S} + c(S,t)V = 0$$
Expressing the equation in terms of the [Greeks](Greeks.md), where 
$$\theta = \frac{\partial V}{\partial t} \;\;\;\;\;\;\ \Delta = \frac{\partial V}{\partial S} \;\;\;\;\;\;\ \Gamma = \frac{\partial^2 V}{\partial S^2}$$

## Approximating Theta
In the explicit scheme, the time derivative is approximated using forward differencing: 
$$\frac{\partial V}{\partial t} =\frac{V(S, t + h) - V(S, t)}{h}$$
Therefore, in the grid, in can be expressed as
$$\frac{\partial V}{\partial t} (S, t) \approx \frac{V_i^k - V_i^{k+1}}{\delta t}$$
Note: With forward differencing of first order derivatives, the error of the approximation: 
$$\frac{\partial V}{\partial t} (S, t) \approx \frac{V_i^k - V_i^{k+1}}{\delta t} + O(\delta t)$$
## Approximating Delta
In the explicit scheme, the spatial derivatives are approximated by central differencing: 
$$\frac{\partial V}{\partial S} (S, t) = \frac{V_{i+1}^k - V_{i-1}^k}{2 \delta S} + O(\delta S^2)$$

## Approximating Theta
Same as the Delta's approximation, 

$$\frac{\partial^2 V}{\partial S^2} (S, t) \approx \frac{V_{i+1}^k - 2V_i^k + V_{i-1}^k}{\delta S^2}$$

## Using the Explicit Finite Difference Method
The Black-Scholes equation, as shown before, can be expressed with the approxmiation of the Greeks above, hence:

$$\begin{gathered}
\frac{V_i^k-V_i^{k+1}}{\delta t} 
+a_i^k\left(\frac{V_{i+1}^k-2V_i^k+V_{i-1}^k}{\delta S^2}\right) 
+b_i^k\left(\frac{V_{i+1}^k-V_{i-1}^k}{2 \delta S}\right) \\
+c_i^kV_i^k=O(\delta t,\delta S^2)
\end{gathered}$$

Rearranging the equation: 
$$V_i^{k+1}=A_i^kV_{i-1}^k+(1+B_i^k)V_i^k+C_i^kV_{i+1}^k$$
where:
$$A_{i}^{k}=\nu_1a_i^k-\frac12\nu_2b_i^k \;\;\;\;\;\;\ B_{i}^{k}=-2\nu_1a_i^k+\delta t c_i^k \;\;\;\;\;\;\ C_{i}^{k}=\nu_1a_i^k+\frac12\nu_2b_i^k$$
where
$$\nu_{1}=\frac{\delta t}{\delta S^{2}}\quad\mathrm{and}\quad\nu_{2}=\frac{\delta t}{\delta S}$$
## Final Conditions 
At expiry, the option value can be expressed as the payoff function:
$$V(S, T) = \mathrm{max}(S - E, 0)$$
With the Finite difference notation: 
$$V_i^0=\mathrm{max}(i\mathrm{~}\delta S - E ,0)$$
## Boundary Conditions 
At S = 0, the diffusion and drift terms "switch off", meaning that on S = 0, the payoff is guaranteed, therefore, 
$$\frac{\partial V}{\partial t}(0,t)-rV(0,t)=0$$
Meaning that
$$V_0^k=(1-r\delta t)V_0^{k-1}$$


Another condition is for S tends to infinity:
$$\frac{\partial^2V}{\partial S^2}(S,t)\to0\quad\mathrm{as~}S\to\infty$$
With the finite-dfference notation: 
$$V_I^k=2V_{I-1}^k-V_{I-2}^k$$
The equations can now be solved using the explicit method. See [Code](Code/BS_explicit_fdm.py)
## Review
### Advantages of the explicit method
- Obvious to tell when it is unstable
- Copes well with coefficients that are asset/time-dependent
- Easy to incoporate accurate one-sided differences 
### Disadvantages of the explicit method
* Restriction on the time step