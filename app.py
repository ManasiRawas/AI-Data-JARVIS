import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# Page Configuration
# --------------------------

st.set_page_config(
    page_title="AI Data Analyst JARVIS",
    page_icon="🤖",
    layout="wide"
)

# --------------------------
# Title
# --------------------------

st.title("🤖 AI Data Analyst JARVIS")

# --------------------------
# Upload CSV
# --------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# --------------------------
# Main Application
# --------------------------

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    # --------------------------
    # First 5 Rows
    # --------------------------

    st.subheader("First 5 Rows")
    st.dataframe(df.head())

    # --------------------------
    # Dataset Overview
    # --------------------------

    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # --------------------------
    # Columns
    # --------------------------

    st.subheader("Columns")

    st.dataframe(
        pd.DataFrame(
            {"Columns": df.columns}
        )
    )

    # --------------------------
    # Missing Values
    # --------------------------

    st.subheader("Missing Values")

    missing_df = df.isnull().sum().reset_index()

    missing_df.columns = [
        "Column",
        "Missing Values"
    ]

    st.dataframe(missing_df)

    # --------------------------
    # Gender Distribution
    # --------------------------

    if "gender" in df.columns:

        st.subheader("Gender Distribution")

        gender_count = (
            df["gender"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        gender_count.columns = [
            "Gender",
            "Count"
        ]

        fig_gender = px.pie(
            gender_count,
            names="Gender",
            values="Count",
            title="Gender Distribution"
        )

        st.plotly_chart(
            fig_gender,
            use_container_width=True,
            key="gender_chart"
        )

    # --------------------------
    # Education Level
    # --------------------------

    if "education_level" in df.columns:

        st.subheader("Education Level")

        edu_count = (
            df["education_level"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        edu_count.columns = [
            "Education",
            "Count"
        ]

        fig_education = px.bar(
            edu_count,
            x="Education",
            y="Count",
            title="Education Level"
        )

        st.plotly_chart(
            fig_education,
            use_container_width=True,
            key="education_chart"
        )

    # --------------------------
    # Experience Distribution
    # --------------------------

    if "experience" in df.columns:

        st.subheader("Experience Distribution")

        exp_count = (
            df["experience"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        exp_count.columns = [
            "Experience",
            "Count"
        ]

        fig_experience = px.bar(
            exp_count,
            x="Experience",
            y="Count",
            title="Experience Distribution"
        )

        st.plotly_chart(
            fig_experience,
            use_container_width=True,
            key="experience_chart"
        )

    # --------------------------
    # Job Change Distribution
    # --------------------------

    if "target" in df.columns:

        st.subheader("Job Change Distribution")

        target_count = (
            df["target"]
            .value_counts()
            .reset_index()
        )

        target_count.columns = [
            "Target",
            "Count"
        ]

        fig_target = px.pie(
            target_count,
            names="Target",
            values="Count",
            title="Job Change Distribution"
        )

        st.plotly_chart(
            fig_target,
            use_container_width=True,
            key="target_chart"
        )

    # --------------------------
    # Dataset Statistics
    # --------------------------

    st.subheader("Dataset Statistics")

    st.dataframe(
        df.describe(include="all")
    )

    # --------------------------
    # Download Dataset
    # --------------------------

    st.subheader("Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="processed_dataset.csv",
        mime="text/csv"
    )
