import pandas as pd
import plotly.express as px
import streamlit as st 
from datetime import date , datetime

st.set_page_config(
    page_title="test_dash",
    page_icon=":white_check_mark:",
    layout="wide",

)

#file uploader
uploaded_file = st.file_uploader("Choose the appropriately prepared CSV file", help="CSV file must be prepared as required from XYZ company")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)


    ### filter according to status
    st.sidebar.write(datetime.now().date())
    st.sidebar.header("Filters")
    Status=st.sidebar.selectbox(
        "select the Status:",
        options=df["Status"].unique(),   
    )

    df_selection_status=df.query("Status == @Status")


    st.title(":bar_chart: My Dashboard_Test")
    st.markdown("----")

    #set KPI variables
    resolved_last30=int(df["Resolved last 30 days"].sum())
    resolved_last7=int(df["Resolved last 7 days"].sum())
    updated_last30=int(df["Updated last 30 days"].sum())
    updated_last7=int(df["Updated last 7 days"].sum())

    #some KPI's
    col_1, col_2, col_3, col_4=st.columns(4)
    with col_1:
        st.subheader("Resolved") 
        st.subheader("last 30 days: ")
        st.subheader(f"{resolved_last30}")
    with col_2:
        st.subheader("Resolved") 
        st.subheader("last 7 days: ")
        st.subheader(f"{resolved_last7}")
    with col_3:
        st.subheader("Updated") 
        st.subheader("last 30 days: ")
        st.subheader(f"{updated_last30}")
    with col_4:
        st.subheader("Updated") 
        st.subheader("last 7 days: ")
        st.subheader(f"{updated_last7}")


    st.markdown("____")

    #draw status chart
    st.subheader("Status filter")
    x=st.write(len(df_selection_status["Status"])," from ", len(df["Status"]))
    fig=px.pie(values=[len(df_selection_status["Status"]), len(df["Status"])-len(df_selection_status["Status"])],names=["Screened","Others"])
    st.plotly_chart(fig)

    st.markdown("____")

    #total cases which can be automated
    total_can_auto=int((df["Custom field (Flagged)"]=="REG-relevant").values.sum())
    st.subheader("Cases which can be automated:")
    st.subheader(f"{total_can_auto}")

