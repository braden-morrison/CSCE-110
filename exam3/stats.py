import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('covid.csv')


grouped = df.groupby('state').sum()


grouped.plot(kind='bar', stacked=False)


plt.title('COVID Cases by State and Gender')
plt.xlabel('State')
plt.ylabel('Number of Cases')
plt.tight_layout()
plt.show()