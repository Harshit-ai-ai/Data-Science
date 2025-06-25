import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)  # Normal distribution

# Create KDE plot
sns.kdeplot(data, fill=True, color='blue', alpha=0.5)

# Add labels and title
plt.title('Example KDE Plot')
plt.xlabel('Value')
plt.ylabel('Density')

# Show plot
plt.show()