import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)
st.title("📊 HR Analytics Dashboard")

df = pd.read_csv("data/cleaned_hr_data.csv")

st.sidebar.header("Filters")

department = st.sidebar.multiselect(
    "Department",
    df["Department"].unique(),
    default=df["Department"].unique()
)
gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)
filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender))
]


col1, col2, col3, col4 = st.columns(4)

col1.metric("Employees", len(filtered_df))

col2.metric("Average Salary",f"{filtered_df['Salary'].mean():,.0f}")

col3.metric("Average Age",round(filtered_df["Age"].mean(),1))

attrition = (filtered_df["Attrition"].value_counts(normalize=True).get("Yes",0))*100

col4.metric("Attrition Rate", f"{attrition:.1f}%")


st.dataframe(df)
st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "hr_data.csv"
)

# Employees by Department
st.subheader("Employees by Department")
fig, ax = plt.subplots(figsize=(8,4))
department = df["Department"].value_counts()

ax.bar(department.index, department.values)
ax.set_xlabel("Department")
ax.set_ylabel("Employees")
ax.set_title("Employees by Department")
st.pyplot(fig)

# Gender Distribution
st.subheader("Gender Distribution")
fig, ax = plt.subplots(figsize=(5,5))
gender = df["Gender"].value_counts()

ax.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Gender Distribution")
st.pyplot(fig)

# Attrition Analysis
st.subheader("Attrition Analysis")
fig, ax = plt.subplots(figsize=(6,4))
attrition = df["Attrition"].value_counts()

ax.bar(attrition.index, attrition.values)
ax.set_xlabel("Attrition")
ax.set_ylabel("Employees")
ax.set_title("Employee Attrition")
st.pyplot(fig)

# Salary Distribution
st.subheader("Salary Distribution")
fig, ax = plt.subplots(figsize=(8,4))

ax.hist(df["Salary"], bins=20)
ax.set_xlabel("Monthly Income")
ax.set_ylabel("Employees")
ax.set_title("Salary Distribution")
st.pyplot(fig)

# Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots(figsize=(8,4))

ax.hist(df["Age"], bins=10)
ax.set_xlabel("Age")
ax.set_ylabel("Employees")
ax.set_title("Age Distribution")
st.pyplot(fig)

# Performance Rating
st.subheader("Performance Rating")
fig, ax = plt.subplots(figsize=(6,4))
performance = df["Performance_Rating"].value_counts().sort_index()

ax.bar(
    performance.index.astype(str),
    performance.values
)
ax.set_xlabel("Performance Rating")
ax.set_ylabel("Employees")
ax.set_title("Performance Rating")
st.pyplot(fig)

# Job Satisfaction
st.subheader("Job Satisfaction")
fig, ax = plt.subplots(figsize=(6,4))
job_sat = df["Job_Satisfaction"].value_counts().sort_index()

ax.bar(
    job_sat.index.astype(str),
    job_sat.values
)
ax.set_xlabel("Job Satisfaction")
ax.set_ylabel("Employees")
ax.set_title("Job Satisfaction")
st.pyplot(fig)

# Overtime vs Attrition
st.subheader("Overtime vs Attrition")
overtime = pd.crosstab(
    df["Overtime"],
    df["Attrition"]
)
fig, ax = plt.subplots(figsize=(6,4))

overtime.plot(
    kind="bar",
    ax=ax
)
ax.set_xlabel("OverTime")
ax.set_ylabel("Employees")
ax.set_title("Overtime vs Attrition")
st.pyplot(fig)

# Promotion Analysis
st.subheader("Years Since Last Promotion")
fig, ax = plt.subplots(figsize=(8,4))
promotion = df["Promotion"].value_counts().sort_index()

ax.bar(
    promotion.index,
    promotion.values
)
ax.set_xlabel("Years Since Last Promotion")
ax.set_ylabel("Employees")
ax.set_title("Promotion Analysis")
st.pyplot(fig)
