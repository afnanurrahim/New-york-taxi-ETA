import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Feature Error Analyzer")
st.write("Exploring Model Performance Across Features")

df = pd.read_csv("prediction.csv")

st.subheader(":orange[Numeric columns]")

numeric_col = st.selectbox(
    "Select a numeric feature",
    ('trip_time', 'trip_miles', 'feel', 'humidity',	'wind_speed', 'traffic'))

col1, col2 = st.columns(2, gap="large")

with col1:
    st.write("> Less than 99th percentile error")
    less_than_99 = df[df['error']<df['error'].quantile(0.99)]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hexbin(x=less_than_99[numeric_col], y=less_than_99['error'], cmap="Reds")
    plt.xlabel(numeric_col,fontsize=15)
    plt.ylabel("error (in minutes)", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    st.pyplot(fig)

with col2:
    st.write("> Greater than 95th percentile error")
    greater_than_99 = df[df['error']>df['error'].quantile(0.99)]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hexbin(x=greater_than_99[numeric_col], y=greater_than_99['error'], cmap="Reds")
    plt.xlabel(numeric_col,fontsize=15)
    plt.ylabel("error (in minutes)", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    st.pyplot(fig)

st.divider()

st.subheader(":orange[Binary columns]")

binary_col = st.selectbox(
    "Select a binary feature",
    ('wav_request_flag', 'wav_match_flag', 'any_tolls', 'BR',	'CLR', 'SN'))

col1, col2 = st.columns(2, gap="large")
with col1:
    st.write(f"> {binary_col} == True")
    selected_df = df[df[binary_col]==1]

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.kdeplot(data=selected_df, x="error", color="red")
    plt.xlabel("error (in minutes)", fontsize=15)
    plt.ylabel("density")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    st.pyplot(fig)


with col2:
    st.write(f"> {binary_col} == False")
    selected_df = df[df[binary_col]==0]

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.kdeplot(data=selected_df, x="error", color="red")
    plt.xlabel("error (in minutes)", fontsize=15)
    plt.ylabel("density")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    st.pyplot(fig)

st.divider()

st.subheader(":orange[Nominal columns]")

nominal_col = st.selectbox(
    "Select a nominal feature",
    ('taxi_company', 'PUservice_zone', 'PUBorough', 'DOBorough', 'DOservice_zone','day_of_week', 'hour_of_day','month', 'wind_direction'))

new_dict = {"feature": [], "stat": [], "error": []}

for u in df[nominal_col].unique():
    new_dict['feature'].append(u)
    new_dict['feature'].append(u)
    mn = df[df[nominal_col]==u]['error'].mean()
    new_dict['stat'].append("mean")
    new_dict['error'].append(mn)
    md = df[df[nominal_col]==u]['error'].median()
    new_dict['stat'].append("median")
    new_dict['error'].append(md)

new_df = pd.DataFrame(new_dict)

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=new_df, x="feature", y="error", hue="stat")
plt.ylabel("error (in minutes)")
st.pyplot(fig)

st.divider()

st.subheader(":orange[High Nominal columns]")

high_nominal_col = st.selectbox(
    "Select a high nominal feature",
    ('dispatching_base_num', 'PUZone', 'DOZone'))

grouped_df = df.groupby(high_nominal_col).agg({"error": ["mean", "median"]})['error']

col1, col2 = st.columns(2, gap="large")
with col1:
    st.text(f"Highest mean error in {high_nominal_col}")
    st.dataframe(grouped_df.sort_values("mean", ascending=False).iloc[:5])

with col2:
    st.text(f"Lowest mean error in {high_nominal_col}")
    st.dataframe(grouped_df.sort_values("mean").iloc[:5])
