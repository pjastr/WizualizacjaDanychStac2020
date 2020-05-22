import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
sns.distplot(df["sepal_length"], bins=20)
plt.show()
