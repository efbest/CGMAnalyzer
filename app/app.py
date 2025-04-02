import streamlit as st
from app.data_loader import load_and_parse_file
from app.metrics import compute_metrics
from app.visualizations import plot_agp, plot_time_series
from app.report import generate_pdf_report
import tempfile

st.set_page_config(page_title="CGMAnalyzer", layout="wide")
st.title("CGM Clinical Analyzer 🐬")

uploaded_file = st.file_uploader("Upload your CGM CSV file", type="csv")
if uploaded_file:
    df, source = load_and_parse_file(uploaded_file)
    if df is not None:
        st.success(f"File parsed as: {source}")
        st.dataframe(df.head())

        metrics = compute_metrics(df)
        st.write(metrics)

        st.plotly_chart(plot_time_series(df), use_container_width=True)
        st.plotly_chart(plot_agp(df), use_container_width=True)

        if st.button("Generate PDF Report"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                generate_pdf_report(df, metrics, source, tmp.name)
                with open(tmp.name, "rb") as f:
                    st.download_button("Download Report", f, file_name="CGM_Report.pdf")
