import streamlit as st
import pandas as pd

st.set_page_config(page_title="ERP Dashboard", page_icon="📊")

st.sidebar.title("System Access")
role = st.sidebar.selectbox(
    "Select Identity",
    ["Administrator", "Plant Manager", "Warehouse Staff"]
)

def get_system_data():
    raw_data = {
        'Part_No': ['YF-2026-001', 'YF-2026-002', 'YF-2026-003', 'YF-2026-004'],
        'Description': ['Stainless Steel Component', 'High Pressure Valve', 'Precision Seal', 'Industrial Lubricant'],
        'Stock': [1500, 45, 8000, 120],
        'Safety_Stock': [1000, 50, 5000, 100],
        'Unit_Cost': [1200, 8500, 15, 600],
        'Vendor': ['Taiwan Steel', 'Global Trade', 'Yongfa Rubber', 'CPC Corp']
    }
    return pd.DataFrame(raw_data)

df = get_system_data()

st.title("T100 ERP Integrated Management")
st.divider()

st.subheader("Material Status Overview")

if role == "Warehouse Staff":
    st.warning("Data Governance: Cost-sensitive columns are restricted.")
    view_df = df.drop(columns=['Unit_Cost'])
    st.dataframe(view_df, use_container_width=True)
else:
    st.success(f"Identity Verified: Full access granted for {role}.")
    st.dataframe(df, use_container_width=True)

st.subheader("Automated Inventory Alerts")
alerts = df[df['Stock'] < df['Safety_Stock']]

if not alerts.empty:
    for _, row in alerts.iterrows():
        st.error(f"Alert: {row['Part_No']} ({row['Description']}) stock below safety limit. Contact {row['Vendor']}.")
else:
    st.info("Status: All stock levels stable.")

with st.expander("Technical Logic - SQL Query"):
    st.code("""
    SELECT imaa001, imaa002, invb005, invb008, imaa009
    FROM imaa_t 
    LEFT JOIN invb_t ON imaa001 = invb001
    WHERE invb005 < invb008;
    """, language="sql")

st.caption("Internal Data Governance Demonstration")
