import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# CSV file path
csv_file = BASE_DIR / "weather_tokyo_data.csv"

# Read CSV file
# sep="\t" because the data is separated by TAB
df = pd.read_csv(csv_file, sep="\t")

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# Print dataframe information
print(df.info())

# Show column names
print("\nColumns:")
print(df.columns.tolist())

# --------------------------------------------------
# 1. Create full date
# --------------------------------------------------

df["full_date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"].astype(str),
    format="%Y/%m/%d"
)

# --------------------------------------------------
# 2. Clean temperature
# --------------------------------------------------

df["temperature"] = df["temperature"].astype(str)

df["temperature"] = df["temperature"].str.replace(
    r"\([^)]*\)",
    "",
    regex=True
)

df["temperature"] = pd.to_numeric(
    df["temperature"],
    errors="coerce"
)

# Remove rows where temperature is missing
df = df.dropna(subset=["temperature"])

# Sort by date
df = df.sort_values(by="full_date")

# Print updated information
print("\nUpdated DataFrame:")
print(df.info())

# --------------------------------------------------
# 3. Average Temperature
# --------------------------------------------------

mean_temperature = df["temperature"].mean()

print(
    f"\nThe average temperature for the entire dataset is "
    f"{mean_temperature:.2f} °C"
)

# --------------------------------------------------
# 4. Monthly Temperature
# --------------------------------------------------

mean_temp_by_month = (
    df.groupby(df["full_date"].dt.month)["temperature"].mean()
)

print("\nThe mean temperature for each month is:")
print(mean_temp_by_month)

# Create monthly temperature graph
plt.figure(figsize=(10, 6))

plt.bar(
    mean_temp_by_month.index,
    mean_temp_by_month.values
)

plt.title("Mean Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Mean Temperature (°C)")

plt.xticks(
    range(1, 13),
    [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.7
)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 5. Hottest and Coldest Day
# --------------------------------------------------

hottest_day = df[
    df["temperature"] == df["temperature"].max()
]

print("\nThe hottest day recorded:")
print(hottest_day)

coldest_day = df[
    df["temperature"] == df["temperature"].min()
]

print("\nThe coldest day recorded:")
print(coldest_day)

# --------------------------------------------------
# 6. Temperature Trends
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["full_date"],
    df["temperature"]
)

plt.title("Temperature Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 7. Seasons
# --------------------------------------------------

def get_season(month):

    if month in [12, 1, 2]:
        return "Winter"

    elif month in [3, 4, 5]:
        return "Spring"

    elif month in [6, 7, 8]:
        return "Summer"

    else:
        return "Fall"


# Create season column
df["season"] = df["full_date"].dt.month.apply(get_season)

# Calculate average temperature by season
seasonal_temperature = (
    df.groupby("season")["temperature"].mean()
)

print("\nSeasonal Average Temperature:")
print(seasonal_temperature)

# --------------------------------------------------
# 8. Seasonal Graph
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    seasonal_temperature.index,
    seasonal_temperature.values,
    marker="o",
    linestyle="-",
    linewidth=2
)

plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.7
)

plt.tight_layout()
plt.show()