import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Data Analyst JARVIS",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.title("👩‍💻 About")

    st.write(
        """
        **AI Data Analyst JARVIS**

        AI-powered analytics dashboard built using
        Python, Pandas, Streamlit, and Plotly.

        Upload any CSV dataset and instantly generate
        automated analysis and visualizations.
        """
    )

    st.markdown("---")

    st.markdown(
        "[🌐 Live App](https://ai-data-jarvis-ew4nkkyz7e2bgj9iwxysh4.streamlit.app/)"
    )

    st.markdown(
        "[💻 GitHub Repository](https://github.com/ManasiRawas/AI-Data-JARVIS)"
    )

    st.markdown(
        "[🔗 LinkedIn](https://linkedin.com/in/manasi-rawas-analytics)"
    )

# ==========================================
# TITLE SECTION
# ==========================================

st.title("🤖 AI Data Analyst JARVIS")

st.markdown(
    """
    ### Upload any CSV dataset to generate automated analysis,
    interactive visualizations, and actionable insights within seconds.
    """
)

st.markdown("---")

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "📂 Upload CSV File",
    type=["csv"]
)

# ==========================================
# MAIN APPLICATION
# ==========================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Loaded Successfully")

    st.markdown("---")

    # ======================================
    # DATA PREVIEW
    # ======================================

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # ======================================
    # DATASET OVERVIEW
    # ======================================

    st.subheader("📊 Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", f"{df.shape[0]:,}")

    with col2:
        st.metric("Columns", f"{df.shape[1]:,}")

    # ======================================
    # COLUMN LIST
    # ======================================

    st.subheader("🧾 Dataset Columns")

    st.dataframe(
        pd.DataFrame(
            {"Columns": df.columns}
        ),
        use_container_width=True
    )

    # ======================================
    # MISSING VALUES
    # ======================================

    st.subheader("⚠️ Missing Values Analysis")

    missing_df = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing_df.columns = [
        "Column",
        "Missing Values"
    ]

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    # ======================================
    # GENDER DISTRIBUTION
    # ======================================

    if "gender" in df.columns:

        st.subheader("👥 Gender Distribution")

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
            use_container_width=True
        )

    # ======================================
    # EDUCATION LEVEL
    # ======================================

    if "education_level" in df.columns:

        st.subheader("🎓 Education Level")

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
            use_container_width=True
        )

    # ======================================
    # EXPERIENCE
    # ======================================

    if "experience" in df.columns:

        st.subheader("💼 Experience Distribution")

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
            use_container_width=True
        )

    # ======================================
    # JOB CHANGE
    # ======================================

    if "target" in df.columns:

        st.subheader("🎯 Job Change Distribution")

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
            use_container_width=True
        )

    # ======================================
    # STATISTICS
    # ======================================

    st.subheader("📈 Dataset Statistics")

    st.dataframe(
        df.describe(include="all"),
        use_container_width=True
    )

    # ======================================
    # DOWNLOAD
    # ======================================

    st.subheader("📥 Download Processed Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="processed_dataset.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.caption(
        "Built by Manasi Rawas | Data Analytics • Data Science • AI"
    )

else:

    st.info(
        "👆 Upload a CSV file to start analyzing your data."
    )
