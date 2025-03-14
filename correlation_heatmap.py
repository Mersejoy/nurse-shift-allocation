import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data based on given correlations
data = {
    "Workload": np.random.normal(50, 10, 100),
    "Burnout": np.random.normal(50, 10, 100),
    "Task Diversity": np.random.normal(50, 10, 100),
    "Emotional Exhaustion": np.random.normal(50, 10, 100),
    "Job Satisfaction": np.random.normal(50, 10, 100),
    "ONWS": np.random.normal(50, 10, 100)
}

df = pd.DataFrame(data)

# Manually setting correlations
df["Burnout"] = df["Workload"] * 0.65 + np.random.normal(0, 5, 100)
df["Emotional Exhaustion"] = df["Task Diversity"] * -0.58 + np.random.normal(0, 5, 100)
df["ONWS"] = df["Job Satisfaction"] * 0.89 + np.random.normal(0, 5, 100)

# Compute correlation matrix
corr_matrix = df.corr()

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Nurse Wellness Factors")
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()
