import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
X_scaled = StandardScaler().fit_transform(X)
print(df['species'].values)
features = X_scaled.T 
cov_matrix = np.cov(features)

values, vectors = np.linalg.eig(cov_matrix)

explained_variances = []
for i in range(len(values)):
    explained_variances.append(values[i] / np.sum(values))


projected_1 = X_scaled.dot(vectors.T[0])
projected_2 = X_scaled.dot(vectors.T[1])
projected_3 = X_scaled.dot(vectors.T[2])

res = pd.DataFrame(projected_1, columns=['PC1'])
res['PC2'] = projected_2
res['PC3'] = projected_3
res['Y'] = df['species'].values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for x, y, z, col in zip(res['PC1'].values,res['PC2'].values,res['PC3'].values, res['Y'].values):
	if col=='setosa':
		color='green'
	elif col=='versicolor':
		color='red'
	else:
		color='blue'
	ax.scatter(x, y, z,color=color)
# plt.show()
# plt.imshow(cov_matrix)
# plt.legend()
plt.legend()
plt.show()