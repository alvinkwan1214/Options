import derivatives 
import numpy as np

import matplotlib.pyplot as plt 

underlying_range = np.linspace(20, 60, 41)
payout_call = derivatives.eu_option(50, underlying_range, option_type="Call", position='short', cost=5)

plt.plot(payout_call, underlying_range)