import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("accident_prediction_india.csv")   # change filename if different

# Clean column names (replace spaces with underscores)
df.columns = df.columns.str.replace(" ", "_")

# ======================
# 1. Accidents by Road Condition
# ======================
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Road_Condition",
              order=df["Road_Condition"].value_counts().index,
              palette="Set2")
plt.title("Accidents by Road Condition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("accidents_by_road_condition.png")
plt.close()

# ======================
# 2. Accidents by Weather Conditions
# ======================
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Weather_Conditions",
              order=df["Weather_Conditions"].value_counts().index,
              palette="Set1")
plt.title("Accidents by Weather Conditions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("accidents_by_weather.png")
plt.close()

# ======================
# 3. Accidents by Time of Day
# ======================
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Time_of_Day",
              order=df["Time_of_Day"].value_counts().index,
              palette="coolwarm")
plt.title("Accidents by Time of Day")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("accidents_by_time.png")
plt.close()

# ======================
# 4. Accident Severity Distribution
# ======================
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Accident_Severity",
              order=df["Accident_Severity"].value_counts().index,
              palette="pastel")
plt.title("Accident Severity Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("accident_severity.png")
plt.close()

# ======================
# 5. Top Accident Locations
# ======================
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="Accident_Location_Details",
              order=df["Accident_Location_Details"].value_counts().head(10).index,
              palette="viridis")
plt.title("Top 10 Accident Location Types")
plt.tight_layout()
plt.savefig("accident_locations.png")
plt.close()

print("✅ Analysis complete! All plots saved as PNG files with different colors.")
