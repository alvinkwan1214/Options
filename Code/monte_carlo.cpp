#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <random>
#include <time.h>
#include <string.h>

using namespace std;

double monte_carlo_price(const int& n_sim, const double& S, const double& K, const double& r, const double& vol, const double& T, int option_type) {
double drift = (r - 0.5 * vol * vol) * T;
double diffusion = vol * sqrt(T);
double payoff_sum = 0.0;
std::default_random_engine generator;
std::normal_distribution<double> normal(0.0, 1.0);
for (int i = 0; i <= n_sim; i++) {
double Z = normal(generator);
double S_forward = S * exp(drift + diffusion * Z);
payoff_sum = payoff_sum + std::max(option_type*(K - S_forward), 0.0);
}
return (payoff_sum / n_sim) * exp(-r * T);
}

int main(int argc, char ** argv) {
clock_t start, end;
start = clock();
int num_sims = 5000000; // Number of simulated asset paths
double S = 100.0; // Option price
double K = 100.0; // Strike price
double r = 0.05; // Risk-free rate (5%)
double vol = 0.2; // Volatility of the underlying (20%)
double T = 1.0; // One year until expiry
// Then we calculate the call/put values via Monte Carlo
//double Call_Value = monte_carlo_call_price(num_sims, S, K, r, vol, T);
//double Put_Value = monte_carlo_put_price(num_sims, S, K, r, vol, T);
double Call_Value = monte_carlo_price(num_sims, S, K, r, vol, T, -1);
double Put_Value = monte_carlo_price(num_sims, S, K, r, vol, T, 1);
end = clock();
float time = float(end - start) / CLOCKS_PER_SEC;
std::ofstream outfile("European_Option_Value_MonteCarlo.txt");
outfile << "Values using Monte Carlo simulation:" << endl;
outfile << "Call option value: " << Call_Value << endl;
outfile << "Put option value: " << Put_Value << endl;
outfile << "CPU Time: " << time << endl;
outfile << "Simulations: " << num_sims << endl;
outfile.close();
return 0;
}