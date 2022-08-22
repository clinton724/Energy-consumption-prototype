import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("results.csv")
pdop= data.iloc[:,24:25].values.tolist()
satellite = data.iloc[:,25:26].values.tolist()
plt.plot(satellite,)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("A simple line graph")
plt.show()