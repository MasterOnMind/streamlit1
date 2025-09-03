import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="NYC Payroll Explorer", layout="centered")

# Title
st.title("💰 NYC Payroll Data Explorer")

# Generate sample data
def generate_data():
    departments = ["POLICE", "FIRE", "EDUCATION", "SANITATION", "TRANSPORTATION"]
    titles = ["OFFICER", "TEACHER", "WORKER", "MANAGER", "SUPERVISOR"]
    
    data = []
    for year in [2019, 2020, 2021]:
        for dept in departments:
            for title in titles:
                num_employees = np.random.randint(50, 200)
                for _ in range(num_employees):
                    base_salary = np.random.normal(60000, 15000)
                    ot_hours = np.random.normal(20, 10)
                    ot_pay = ot_hours * (base_salary / 2080 * 1.5)
                    total_pay = base_salary + ot_pay
                    
                    data.append({
                        "Year": year,
                        "Department": dept,
                        "Title": f"{dept} {title}",
                        "Base Salary": base_salary,
                        "OT Hours": ot_hours,
                        "OT Pay": ot_pay,
                        "Total Pay": total_pay
                    })
    return pd.DataFrame(data)

df = generate_data()

# Filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Year", df["Year"].unique())
selected_dept = st.sidebar.selectbox("Department", df["Department"].unique())

# Filter data
filtered_df = df[(df["Year"] == selected_year) & (df["Department"] == selected_dept)]

# Display metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Salary", f"${filtered_df['Base Salary'].mean():,.0f}")
with col2:
    st.metric("Avg OT Hours", f"{filtered_df['OT Hours'].mean():.1f}")
with col3:
    st.metric("Total Employees", len(filtered_df))

# Salary distribution chart
st.subheader("Salary Distribution")
fig = px.histogram(filtered_df, x="Base Salary", nbins=20)
st.plotly_chart(fig, use_container_width=True)

# Top earners
st.subheader("Top 10 Earners")
top_earners = filtered_df.nlargest(10, "Total Pay")[["Title", "Base Salary", "OT Pay", "Total Pay"]]
top_earners["Base Salary"] = top_earners["Base Salary"].apply(lambda x: f"${x:,.0f}")
top_earners["OT Pay"] = top_earners["OT Pay"].apply(lambda x: f"${x:,.0f}")
top_earners["Total Pay"] = top_earners["Total Pay"].apply(lambda x: f"${x:,.0f}")
st.dataframe(top_earners, use_container_width=True)

# Department comparison
st.subheader("Department Comparison")
dept_avg = df.groupby("Department")["Total Pay"].mean().reset_index()
fig2 = px.bar(dept_avg, x="Department", y="Total Pay", title="Average Total Pay by Department")
st.plotly_chart(fig2, use_container_width=True)
