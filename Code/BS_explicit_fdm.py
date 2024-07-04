import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Parameters
vol = 0.2
r = 0.05
strike_price  = 100

#Assets 
no_i = 20 #number asset steps
#assuming infinity is twice of strike price
dS = 2 * strike_price/no_i# assest steps 

#Time
expiry_time  = 1
dt = 0.9/(vol ** 2 * no_i ** 2) #for stability
no_k = int(expiry_time/dt)+1 #number time steps
dt = expiry_time / no_k #time steps

# Asset array
v = np.zeros((no_i + 1, no_k + 1))

#Greeks array
delta_total  = np.zeros((no_i + 1, no_k + 1))
gamma_total = np.zeros((no_i + 1, no_k + 1))
theta_total = np.zeros((no_i + 1, no_k + 1))

#Initialise the grid
for i in range(no_i + 1):
    v[i,0] = np.maximum((i * dS - strike_price),0)

for k in range(1, no_k+1):
    for i in range(1, no_i):
        delta  = (v[i+1, k-1] - v[i-1, k-1])/ (2*dS)
        gamma  = (v[i+1, k-1] -2 * v[i, k-1] + v[i-1, k-1])/(dS**2)
        theta  = -0.5*(vol**2)*((i * dS)**2) * gamma - r*i * dS *delta + r*v[i, k-1]

        v[i, k] = v[i,k-1] - dt*theta
        delta_total[i,k] = delta
        gamma_total[i,k] = gamma 
        theta_total[i,k] = theta
    
    v[0,k] = v[0, k - 1] * (1 - r*dt) #Boundary condition at S = 0
    v[no_i, k] = 2 * v[no_i - 1, k] - v[no_i - 2, k] #Boundary condition at S at infinity

    #delta boundary condition
    delta_total[no_i, k] = (v[no_i, k] - v[no_i -1 , k])/dS 
    delta_total[0,k] = (v[1,k] - v[0 , k])/dS 

    #theta boundary condition
    theta_total[no_i, k] = -0.5 * (vol ** 2) * ((i*dS) ** 2) * gamma_total[no_i, k] - r * (i*dS) * delta_total[no_i, k] + r * v[no_i, k]
    theta_total[0,k] = r * v[0,k]


#create dataframe for the results
asset_range = np.arange(0, no_i + 1) * dS 
time_steps = np.arange(0, no_k + 1) * dt
rounded_time_steps = np.round(time_steps, decimals=3)
option_value = pd.DataFrame(v, index=asset_range, columns=rounded_time_steps).round(3)
delta_chart =pd.DataFrame(delta_total, index=asset_range, columns=rounded_time_steps).round(3)
gamma_chart =pd.DataFrame(gamma_total, index=asset_range, columns=rounded_time_steps).round(3)
theta_chart =pd.DataFrame(theta_total, index=asset_range, columns=rounded_time_steps).round(3)


chart_dic = {"Option Surface Plot": option_value,
             "Delta Surface Plot": delta_chart,
             "Gamma Surface Plot": gamma_chart,
            "Theta Surface Plot": theta_chart
             }


#plotting
def plot_3D(df, title, location):
    ax = fig.add_subplot(location, projection='3d')
    X, Y = np.meshgrid(df.columns, df.index)
    Z = df.values
    surf = ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_xlabel('Time')
    ax.set_ylabel('Asset Price')
    ax.set_zlabel(title.split(" ")[0])
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return

fig = plt.figure(figsize=(20, 10))
loc = 221
for chart in chart_dic:
    plot_3D(chart_dic[chart], chart, loc)
    loc += 1
plt.tight_layout()
plt.show()