# https://www.kaggle.com/jsphyg/weather-dataset-rattle-package
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn import preprocessing

# read csv into dataframe
df = pd.read_csv("weatherAUS.csv", date_parser=lambda x: datetime.strptime(x, "%Y-%m-%d"))
df = df[np.isfinite(df['Rainfall'])]
df = df[np.isfinite(df['Pressure9am'])]
df = df[np.isfinite(df['Pressure3pm'])]
df.fillna(0, inplace=True)
print(df.head())
data = {
    "Rainfall": df['Rainfall'], 
    "MeanPressure": (df['Pressure9am']+df['Pressure3pm'])/2
}
df = pd.DataFrame(data)

# normalize data
normalizedData = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(df))

# set up plot
plt.scatter(normalizedData[1], normalizedData[0], alpha=0.1)
plt.ylabel("Rainfall")
plt.xlabel("Average Pressure (9am-3pm)")
plt.title("Average Pressure vs Rainfall")

# plot multivariate distribution
cov = np.cov(normalizedData[1], normalizedData[0])
mean = np.array([np.mean(normalizedData[1]),  np.mean(normalizedData[0])])
x, y = np.random.multivariate_normal(mean, cov, 1000).T
plt.plot(x, y, 'x', color="red", alpha=0.1)

# plot univariate distributions for each var
# x axis
scale = 5
mu = mean[0]
stddev = np.sqrt(np.var(normalizedData[1]))
x = np.linspace(mu - scale*stddev, mu + scale*stddev, 100)
plt.plot(x, stats.norm.pdf(x, mu, stddev), color="green")
# y axis
mu = mean[1]
stddev = np.sqrt(np.var(normalizedData[0]))
x = np.linspace(mu - scale*stddev, mu + scale*stddev, 100)
plt.plot(x, stats.norm.pdf(x, mu, stddev), color="orange")
plt.show()


