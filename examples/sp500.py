import matplotlib.pyplot as plt
import pandas as pd

from l1tf import load_sp500, HPTrendFilter, L1TrendFilter

df = load_sp500(return_logy=True)

model = L1TrendFilter(alpha=100, prop=0.01)
model.fit(df)

forcast = model.predict()

model.plot(forcast)
plt.show()
