The Crank-Nicolson method is the average of the explicit method and the fully implicit method. Turning the [Black-Scholes Equation](Black-Scholes%20Equation.md) in to the finite-difference notation gives: 

$$\begin{gathered}
\frac{V_{i}^{k}-V_{i}^{k+1}}{\delta t} \\
+ \frac{a_{i}^{k+1}}{2}\left(\frac{V_{i+1}^{k+1}-2V_{i}^{k+1}+V_{i-1}^{k+1}}{\delta S^{2}}\right)+\frac{a_{i}^{k}}{2}\left(\frac{V_{i+1}^{k}-2V_{i}^{k}+V_{i-1}^{k}}{\delta S^{2}}\right) \\
+ \frac{b_{i}^{k+1}}{2}\left(\frac{V_{i+1}^{k+1}-V_{i-1}^{k+1}}{2 \delta S}\right)+\frac{b_{i}^{k}}{2}\left(\frac{V_{i+1}^{k}-V_{i-1}^{k}}{2 \delta S}\right) \\
+\frac{1}{2}c_{i}^{k+1}V_{i}^{k+1}+\frac{1}{2}c_{i}^{k}V_{i}^{k}=O(\delta t^{2},\delta S^{2})
\end{gathered}$$
Hence, it can be written as 

$$-A_i^{k+1}V_{i-1}^{k+1}+(1-B_i^{k+1})V_i^{k+1}-C_i^{k+1}V_{i+1}^{k+1}=A_i^kV_{i-1}^k+(1+B_i^k)V_i^k+C_i^kV_{i+1}^k$$
where, 
$$\begin{gathered}
A_i^{k} =\frac{1}{2}\nu_{1}a_{i}^{k}-\frac{1}{4}\nu_{2}b_{i}^{k} ,\quad
B_i^{k} =-\nu_{1}a_{i}^{k}+\frac{1}{2}\delta t c_{i}^{k} ,\quad
C_{i}^{k}=\frac{1}{2}\nu_{1}a_{i}^{k}+\frac{1}{4}\nu_{2}b_{i}^{k} 
\end{gathered}$$
In Matrix form, 
$$\begin{gathered}
\left(\begin{array}{ccccccc}-A_1^{k+1}&1-B_1^{k+1}&-C_1^{k+1}&0&.&.&.\\0&-A_2^{k+1}&1-B_2^{k+1}&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&1-B_{l-2}^{k+1}&-C_{l-2}^{k+1}&0\\.&.&.&0&-A_{l-1}^{k+1}&1-B_{l-1}^{k+1}&-C_{l-1}^{k+1}\end{array}\right)\left(\begin{array}{c}V_0^{k+1}\\V_1^{k+1}\\.\\.\\.\\.\\V_{l-1}^{k+1}\\V_{l}^{k+1}\\\end{array}\right)\\
=\left(\begin{array}{cccccc}A_1^k&1+B_1^k&C_1^k&0&.&.&.\\0&A_2^k&1+B_2^k&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&1+B_{I-2}^k&C_{I-2}^k&0\\.&.&.&0&A_{I-1}^k&1+B_{I-1}^k&C_{I-1}^k\end{array}\right)\left(\begin{array}{c}V_0^k\\V_1^k\\.\\.\\.\\.\\.\\V_{I-1}^k\\V_I^k\end{array}\right)
\end{gathered}$$
The goal is to write the system of equations into this form 
$$\mathbf{M}_{L}^{k+1}\mathbf{v}^{k+1}+\mathbf{r}^{k} = \mathbf{M}_{R}^{k}\mathbf{v}^{k}$$

## Boundary Conditions 
### 1. $V^{k+1}_{0}$ is given 
when we know that our option has a particular value on the boundary of i = 0 or i = I
if we have a European put, we know that:
$$V(0, t) = E e^{-r(T-t)}  \to V^{k+1}_{0} = E e^{-r(k + 1)\delta t}$$
Hence, 
$$\begin{gathered}
\left(\begin{array}{ccccccc}-A_1^{k+1}&1-B_1^{k+1}&-C_1^{k+1}&0&.&.&.\\0&-A_2^{k+1}&1-B_2^{k+1}&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&1-B_{l-2}^{k+1}&-C_{l-2}^{k+1}&0\\.&.&.&0&-A_{l-1}^{k+1}&1-B_{l-1}^{k+1}&-C_{l-1}^{k+1}\end{array}\right)\left(\begin{array}{c}V_0^{k+1}\\V_1^{k+1}\\.\\.\\.\\.\\V_{l-1}^{k+1}\\V_{l}^{k+1}\\\end{array}\right)\\
\end{gathered}$$
can be written as:
$$\begin{gathered}\left(\begin{array}{ccccc}1-B_{1}^{k+1}&-C_{1}^{k+1}&0&.&.\\-A_{2}^{k+1}&1-B_{2}^{k+1}&.&.&.\\&0&.&.&.&0\\&.&.&.&1-B_{l-2}^{k+1}&-C_{l-2}^{k+1}\\&.&.&0&-A_{l-1}^{k+1}&1-B_{l-1}^{k+1}\end{array}\right)\left(\begin{array}{c}V_{1}^{k+1}\\.\\.\\.\\.\\.\\.\\V_{l-1}^{k+1}\end{array}\right)\\+\left(\begin{array}{c}-A_{1}^{k+1}V_{0}^{k+1}\\0\\0\\.\\.\\0\\.\end{array}\right)=\mathbf{M}_{L}^{k+1}\mathbf{v}^{k+1}+\mathbf{r}^{k}\end{gathered}$$
the vector $r^{k}$ has the length of $I -1$ and has non-zero elements at the top (and bottom), and it is completely known because it only depends on the function A and the value of V at the boundary.

### 2. Relationship between $V^{k+1}_{0}$ and $V^{k+1}_{1}$
If we have a [Barrier option](Barrier%20option.md) for which a grid point does no coincide with the barrier, we must use the approximation: 
$$V_0^{k+1}=\frac{1}{\alpha}\left(f-(1-\alpha)V_1^{k+1}\right)$$
Perhaps the slop of the option value for large or small S, giving us a gradient boundary condition

if we use a one-sided difference for the derivative then the boundary condition can also be written as a relationship between the last grid point and the last but one. More generally, suppose we have: 

$$V_0^{k+1}=a+ bV_1^{k+1}$$
The LHS of 
$$\begin{gathered}
\begin{pmatrix}1-B_1^{k+1}&-C_1^{k+1}&0&.&.\\-A_2^{k+1}&1-B_2^{k+1}&.&.&.\\&0&.&.&.&0\\&.&.&.&1-B_{I-2}^{k+1}&-C_{I-2}^{k+1}\\&.&.&0&-A_{I-1}^{k+1}&1-B_{I-1}^{k+1}\end{pmatrix}\begin{pmatrix}V_1^{k+1}\\.\\.\\.\\.\\.\\V_{I-1}^{k+1}\end{pmatrix} \\+ \begin{pmatrix}-A_1^{k+1}(a+bV_1^{k+1})\\0\\0\\.\\.\\0\\.\end{pmatrix}
\end{gathered}$$
$$\begin{gathered}
\begin{pmatrix}1-B_1^{k+1}-bA_1^{k+1}&-C_1^{k+1}&0&.&.\\-A_2^{k+1}&1-B_2^{k+1}&.&.&.\\&0&.&.&.&0\\&.&.&.&1-B_{I-2}^{k+1}&-C_{I-2}^{k+1}\\&.&.&0&-A_{I-1}^{k+1}&1-B_{I-1}^{k+1}\end{pmatrix}\begin{pmatrix}V_1^{k+1}\\.\\.\\.\\.\\.\\V_{I-1}^{k+1}\end{pmatrix} \\ +\begin{pmatrix}-aA_1^{k+1}\\0\\0\\.\\.\\0\\.\end{pmatrix}
\end{gathered}$$
Hence it is in the form of $\mathbf{M}_{L}^{k+1}\mathbf{v}^{k+1}+\mathbf{r}^{k} = \mathbf{M}_{R}^{k}\mathbf{v}^{k}$, with $\mathbf{M}_{L}^{k+1}$ and $r^k$ both are known.

### 3. when $\frac{\delta^2V} {\delta S^2 } = 0$
This condition is useful since it is independent of the type of contract, as long as the contract has a payoff that is at most linear in the underlying. In the central difference form: 
$$V_0^{k+1}=2V_1^{k+1}-V_2^{k+1}$$
Therefore, the left handside of the equation becomes: 
$$\left(\begin{array}{cccccc}1-B_1^{k+1}-2A_1^{k+1}&-C_1^{k+1}+A_1^{k+1}&0&.&.\\-A_2^{k+1}&1-B_2^{k+1}&.&.&.\\&0&.&.&.&0\\&.&.&.&1-B_{I-2}^{k+1}&-C_{I-2}^{k+1}\\&.&.&0&-A_{I-1}^{k+1}&1-B_{I-1}^{k+1}\end{array}\right)\left(\begin{array}{c}V_1^{k+1}\\.\\.\\.\\.\\.\\V_{I-1}^{k+1}\end{array}\right)$$
which is in the form of $\mathbf{M}_{L}^{k+1}\mathbf{v}^{k+1}+\mathbf{r}^{k}$ where $r^k$ is 0.


## The Matric Equation
Regardless of the boundary condition, the Crank-Nicolson scheme gives: 
$$\mathbf{M}_{L}^{k+1}\mathbf{v}^{k+1}+\mathbf{r}^{k} = \mathbf{M}_{R}^{k}\mathbf{v}^{k}$$
To find $\mathbf{v}^{k+1}$ , $\mathbf{M}_{L}^{k+1}$ can be inverted to give: 
$$\mathbf{v}^{k+1}=\left(\mathbf{M}_L^{k+1}\right)^{-1}\left(\mathbf{M}_R^k\mathbf{v}^k-\mathbf{r}^k\right)$$
However, the inversion is very time consuming and extremely inefficient from the computational point of view. 
### LU decomposition
$\mathbf{M}_{L}^{k+1}$ is a tridiagonal matric, the only non-zero elements lie along the diagonal and the sub- and superdiagonals. 
$$M = LU $$
$$\left.\begin{aligned}&\begin{pmatrix}1-B_1&-C_1&0&.&.&.&0\\-A_2&1-B_2&-C_2&0&.&.&.&.\\0&-A_3&1-B_3&.&.&.&.&.\\.&0&.&.&.&.&0&.\\.&.&.&.&.&1-B_{I-3}&-C_{I-3}&0\\.&.&.&.&0&-A_{I-2}&1-B_{I-2}&-C_{I-2}\\.&.&.&.&.&0&-A_{I-1}&1-B_{I-1}\end{pmatrix}\\&=\begin{pmatrix}1&0&0&.&.&.&0\\l_2&1&0&0&.&.&.\\0&l_3&1&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&1&0&0\\.&.&.&0&l_{I-2}&1&0\\.&.&.&.&0&l_{I-1}&1\end{pmatrix}\begin{pmatrix}d_1&u_1&0&.&.&.&0\\0&d_2&u_2&0&.&.&.&.\\0&0&d_3&.&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&d_{I-3}&u_{I-3}&0\\.&.&.&0&0&d_{I-2}&u_{I-2}\\.&.&.&.&0&0&d_{I-1}\end{pmatrix}\end{aligned}\right.$$
where 
$$d_1=1-B_1$$$$l_id_{i-1}=-A_i\quad u_{i-1}=-C_{i-1}\quad d_i=1-B_i-l_iu_{i-1}\quad\mathrm{for}\quad2\leq i\leq I-1$$

Dropping the superscript and assuming $\mathbf{v}^{k+1}=\left(\mathbf{M}_L^{k+1}\right)^{-1}\left(\mathbf{M}_R^k\mathbf{v}^k-\mathbf{r}^k\right)$ , the right hand side multiplication is done: 
$$\mathbf{M}\mathbf{v}=q \to \mathbf{L}\mathbf{U}\mathbf{v}=q$$
where q contains the old option value array at time step k and the detials of the boundary conditions
$$ \mathbf{L}\mathbf{U}\mathbf{v}=q \to \mathbf{L}\mathbf{w}=q$$
The first step gives $$w_{1} = q_{1}$$ and $$w_i=q_i-l_iw_{i-1}\quad\mathrm{for}\quad2\leq i\leq I-1.$$
Second steps involves working backwards from i = I -2 to = 1 
$$v_{I-1}=\frac{w_{I-1}}{d_{I-1}}$$
and
$$v_i=\frac{w_i-u_iv_{i+1}}{d_i}\quad\mathrm{for}\quad I-2\geq i\geq1$$
#### Advantages of LU decomposition
- fast 
- decomposition only need to be done once if the matrix M is independent of time 
#### Disadvantage of LU decomposition 
- not immediately applicable to American option 
- decomposition needed to be done each time step if the matrix M is time-dependent
### Successive Over-relaxation, SOR
