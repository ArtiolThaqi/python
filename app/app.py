
import pandas as pd
import streamlit as st
from pathlib import Path



st.set_page_config(
    page_title="Tokyo Weather Analysis",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Tokyo Weather Analysis")


BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / "weather_tokyo_data.csv"


df = pd.read_csv(csv_file, sep="\t")

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()


df["full_date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"].astype(str),
    format="%Y/%m/%d"
)

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


st.header("📊 Dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rows", len(df))

with col2:
    st.metric("Total Columns", len(df.columns))

with col3:
    st.metric(
        "Average Temperature",
        f"{df['temperature'].mean():.2f} °C"
    )

st.subheader("Data Preview")
st.dataframe(df, use_container_width=True)


st.header("🌡️ Average Temperature")

mean_temperature = df["temperature"].mean()

st.metric(
    "Average Temperature",
    f"{mean_temperature:.2f} °C"
)

st.header("📅 Monthly Temperature")

mean_temp_by_month = (
    df.groupby(df["full_date"].dt.month)["temperature"].mean()
)

st.bar_chart(mean_temp_by_month)

# --------------------------------------------------
# 5 Ditet me te nxehta dhe 5 ditet me te ftohta
# --------------------------------------------------

st.header("🔥 5 Ditet më të Nxehta & 🥶 5 Ditet më të Ftohta")

# Krijojme vetem daten pa oren
df["date"] = df["full_date"].dt.date

# Gjejme temperaturen mesatare per secilen dite
daily_temperature = (
    df.groupby("date")["temperature"]
    .mean()
    .reset_index()
)

# 5 ditet me te nxehta
hottest_5_days = (
    daily_temperature
    .sort_values(by="temperature", ascending=False)
    .head(5)
)

# 5 ditet me te ftohta
coldest_5_days = (
    daily_temperature
    .sort_values(by="temperature", ascending=True)
    .head(5)
)

# Mesatarja e 5 diteve me te nxehta
average_hottest_5 = hottest_5_days["temperature"].mean()

# Mesatarja e 5 diteve me te ftohta
average_coldest_5 = coldest_5_days["temperature"].mean()


# Shfaqim rezultatet
col1, col2 = st.columns(2)

with col1:

    st.subheader("🔥 5 Ditet më të Nxehta")

    st.dataframe(
        hottest_5_days,
        use_container_width=True,
        hide_index=True
    )

    st.metric(
        "Mesatarja e 5 ditëve",
        f"{average_hottest_5:.2f} °C"
    )


with col2:

    st.subheader("🥶 5 Ditet më të Ftohta")

    st.dataframe(
        coldest_5_days,
        use_container_width=True,
        hide_index=True
    )

    st.metric(
        "Mesatarja e 5 ditëve",
        f"{average_coldest_5:.2f} °C"
    )




st.header("🔥 Hottest & 🥶 Coldest Day")

hottest_temperature = df["temperature"].max()
coldest_temperature = df["temperature"].min()

hottest_day = df[
    df["temperature"] == hottest_temperature
]

coldest_day = df[
    df["temperature"] == coldest_temperature
]

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Hottest Day")

    st.metric(
        "Temperature",
        f"{hottest_temperature:.2f} °C"
    )

    st.dataframe(
        hottest_day,
        use_container_width=True
    )

with col2:
    st.subheader("🥶 Coldest Day")

    st.metric(
        "Temperature",
        f"{coldest_temperature:.2f} °C"
    )

    st.dataframe(
        coldest_day,
        use_container_width=True
    )


st.header("📈 Temperature Trends")

temperature_chart = df.set_index("full_date")[
    ["temperature"]
]

st.line_chart(temperature_chart)


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


seasonal_temperature = (
    df.groupby("season")["temperature"].mean()
)

st.header("🍂 Seasonal Average Temperature")

st.bar_chart(seasonal_temperature)



st.subheader("Seasonal Statistics")

st.dataframe(
    seasonal_temperature.round(2),
    use_container_width=True
)


st.header("📊 Temperature Statistics")

statistics = df["temperature"].describe()

st.dataframe(
    statistics.to_frame(name="Temperature (°C)"),
    use_container_width=True
)


st.divider()

st.write(
    "Weather Analysis App • Built with Python, Pandas and Streamlit"
)

