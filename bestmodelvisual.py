import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data = {
    "Country": ["Antarctica", "Australia", "Beijing", "Berlin", "Brasilia", "Pretoria", "Washington"],
    "Best Model for Power": ["ANN", "ANN", "SVR", "SVR", "XGB", "SVR", "ANN"],
    "Best Model for Efficiency": ["LGBM", "CatBoost", "CatBoost", "CatBoost", "Bagging", "CatBoost", "CatBoost"]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Create a new DataFrame to hold the encoded data
encoded_data = pd.DataFrame(index=df['Country'], columns=pd.unique(df[['Best Model for Power', 'Best Model for Efficiency']].values.ravel('K')))

# Initialize all values to zero
encoded_data.fillna(0, inplace=True)

# Encode the data (1 for Power, -1 for Efficiency)
for index, row in df.iterrows():
    encoded_data.at[row['Country'], row['Best Model for Power']] = 1
    encoded_data.at[row['Country'], row['Best Model for Efficiency']] = -1

# Drawing the heatmap
plt.figure(figsize=(10, 8))
sns.set(style="white", font_scale=1.2)  # Setting the style and context for academic look

# Drawing the heatmap
ax = sns.heatmap(encoded_data, cmap="coolwarm", annot=True, center=0, fmt="d",
                 cbar_kws={'label': 'Model Preference\n(1 for Power, -1 for Efficiency)'})

# Adding informative title
plt.title('Country Preferences for Models', pad=20)

# Adding axis labels
plt.xlabel('Model', labelpad=10)
plt.ylabel('Country', labelpad=10)

# Removing the axis lines for a cleaner look
sns.despine()

# Adjusting the layout to ensure everything fits without overlap
plt.tight_layout()

# # Saving the plot with a higher resolution suitable for academic papers
# file_path = '/academic_heatmap_with_colorbar_and_howto.png'
# plt.savefig(file_path, dpi=300)

# Displaying the plot
plt.show()