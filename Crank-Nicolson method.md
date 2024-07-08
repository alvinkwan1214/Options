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
A_i^{k} =\frac{1}{2}\nu_{1}a_{i}^{k}-\frac{1}{4}\nu_{2}b_{i}^{k} \;\;\;\;\;
B_i^{k} =-\nu_{1}a_{i}^{k}+\frac{1}{2}\delta t c_{i}^{k} \;\;\;\;\;
C_{i}^{k}=\frac{1}{2}\nu_{1}a_{i}^{k}+\frac{1}{4}\nu_{2}b_{i}^{k} 
\end{gathered}$$
In Matrix form, 
$$\begin{gathered}
\left(\begin{array}{ccccccc}-A_1^{k+1}&1-B_1^{k+1}&-C_1^{k+1}&0&.&.&.\\0&-A_2^{k+1}&1-B_2^{k+1}&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&1-B_{l-2}^{k+1}&-C_{l-2}^{k+1}&0\\.&.&.&0&-A_{l-1}^{k+1}&1-B_{l-1}^{k+1}&-C_{l-1}^{k+1}\end{array}\right)\left(\begin{array}{c}V_0^{k+1}\\V_1^{k+1}\\.\\.\\.\\.\\.\\V_{l-1}^{k+1}\\\end{array}\right)\\
=\left(\begin{array}{cccccc}A_1^k&1+B_1^k&C_1^k&0&.&.&.\\0&A_2^k&1+B_2^k&.&.&.&.\\.&0&.&.&.&0&.\\.&.&.&.&1+B_{I-2}^k&C_{I-2}^k&0\\.&.&.&0&A_{I-1}^k&1+B_{I-1}^k&C_{I-1}^k\end{array}\right)\left(\begin{array}{c}V_0^k\\V_1^k\\.\\.\\.\\.\\.\\V_{I-1}^k\\V_I^k\end{array}\right)
\end{gathered}$$