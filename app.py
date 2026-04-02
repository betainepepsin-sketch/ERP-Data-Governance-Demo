import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="T100 Enterprise ERP System", layout="wide")

if 'audit_trail' not in st.session_state:
    st.session_state.audit_trail = []

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

operator_id = st.sidebar.selectbox("Operator ID", ["MIS-9901", "PUR-2005", "SFC-3001", "FIN-1002", "SAL-4008"])
st.sidebar.divider()
st.sidebar.write(f"Server: T100-PROD-AS01")
st.sidebar.write(f"Database: Oracle 19.3c")

st.title("T100 Enterprise Resource Planning - Standard Edition")

col_h1, col_h2, col_h3 = st.columns([2, 1, 1])
with col_h1:
    search_bar = st.text_input("Global Search (Doc No / Part No / Vendor)", "")
with col_h2:
    dept_select = st.selectbox("Department / 權責部門", [
        "資材部 (Material)", "生管部 (PMC)", "採購部 (PUR)", "業務部 (SALES)", 
        "研發部 (R&D)", "製造部 (MFG)", "品管部 (QC)", "財務部 (FIN)", 
        "管理部 (ADMIN)", "經理室 (MANAGER)", "總經理室 (GM)", "資訊部 (MIS)"
    ])
with col_h3:
    doc_status = st.multiselect("Doc Status", ["Draft", "Open", "Approved", "Closed", "Hold"], default=["Open", "Approved"])

st.divider()

tab_inv, tab_pur, tab_sfc, tab_fin, tab_sys = st.tabs([
    "📦 庫存資材管理", "🛒 採購與供應鏈", "⚙️ 生產現場管制", "💰 財務應收應付", "🛠️ 系統稽核維護"
])

# --- TAB: Inventory ---
with tab_inv:
    st.subheader("Inventory Stock Status (INV)")
    inv_data = {
        "料號": ["YF-2026-001", "YF-2026-002", "YF-2026-003"],
        "品名規格": ["SUS304 Cold Rolled", "Power Unit V2", "IC Controller B1"],
        "庫存數量": [5000.0, 120.0, 850.0],
        "未交貨量": [200.0, 15.0, 100.0],
        "已交貨量": [4800.0, 105.0, 750.0],
        "單位": ["KG", "SET", "PCS"],
        "儲位代號": ["WH01-A1", "WH02-B3", "WH01-C2"],
        "建立時間": ["2026-01-10 08:00", "2026-02-15 10:30", "2026-03-01 14:00"],
        "修改時間": [get_timestamp(), get_timestamp(), get_timestamp()],
        "經手人": ["WH-001", "WH-002", "WH-001"]
    }
    st.data_editor(pd.DataFrame(inv_data), use_container_width=True)

# --- TAB: Purchase ---
with tab_pur:
    st.subheader("Purchase Order Management (PUR)")
    pur_data = {
        "採購單號": ["PUR26040001", "PUR26040002", "PUR26040003"],
        "供應商代號": ["V00125", "V00342", "V00089"],
        "供應商名稱": ["台鋼金屬工業", "精密電子組件", "永泰化學"],
        "付款方式": ["T/T 30 Days", "L/C at Sight", "T/T 60 Days"],
        "票期": ["30D", "0D", "60D"],
        "交貨時間": ["2026-04-15", "2026-04-20", "2026-05-01"],
        "負責人": ["PUR-ZHANG", "PUR-LEE", "PUR-WANG"],
        "建立時間": ["2026-03-25 09:00", "2026-03-28 11:00", "2026-04-01 16:00"],
        "修改紀錄": ["User: PUR-ZHANG | Rev: 1", "User: PUR-LEE | Rev: 0", "User: PUR-WANG | Rev: 2"]
    }
    st.data_editor(pd.DataFrame(pur_data), use_container_width=True)

# --- TAB: SFC ---
with tab_sfc:
    st.subheader("Shop Floor Control (SFC)")
    sfc_data = {
        "工單編號": ["WO-040201", "WO-040202"],
        "產線代號": ["LINE-01", "LINE-03"],
        "計畫產量": [1000, 500],
        "報工數量": [850, 0],
        "良率": ["98.5%", "0.0%"],
        "開工時間": ["2026-04-02 08:00", "2026-04-03 08:00"],
        "預計完工": ["2026-04-02 17:00", "2026-04-03 17:00"],
        "經手人": ["OP-A01", "OP-B05"]
    }
    st.data_editor(pd.DataFrame(sfc_data), use_container_width=True)

# --- TAB: Approval/Financial ---
with tab_fin:
    st.subheader("BPM Workflow & Financial Approval")
    bpm_data = {
        "Approve": [False, False, False],
        "單據編號": ["AP-2604001", "PAY-2604015", "EXP-2604009"],
        "金額": [1250000.0, 45000.0, 8900.0],
        "幣別": ["TWD", "USD", "TWD"],
        "申請人": ["PMC-LEE", "PUR-ZHANG", "MIS-DAVID"],
        "簽核階段": ["經理部審核", "財務部覆核", "總經理核决"],
        "建立時間": ["2026-04-01 10:00", "2026-04-01 14:00", "2026-04-02 09:00"]
    }
    # Interactive selection for approval
    selected_apps = st.data_editor(pd.DataFrame(bpm_data), use_container_width=True, hide_index=True)
    
    c1, c2, c3 = st.columns([1, 1, 8])
    if c1.button("Bulk Approve"):
        st.success(f"Audit Trail: Operator {operator_id} approved selected records at {get_timestamp()}")
        st.session_state.audit_trail.append({"Time": get_timestamp(), "User": operator_id, "Event": "Bulk Approval Executed"})
    if c2.button("Reject"):
        st.error("Workflow status updated to: REJECTED")

# --- TAB: System Maintenance ---
with tab_sys:
    st.subheader("System Audit Log (Standard Compliance)")
    if st.session_state.audit_trail:
        st.table(pd.DataFrame(st.session_state.audit_trail))
    else:
        st.write("No critical changes recorded in current session.")
    
    st.divider()
    st.subheader("Database Health")
    st.json({
        "Instance": "T100_PROD",
        "SGA_Size": "32GB",
        "Active_Processes": 452,
        "Last_Backup": "2026-04-02 02:00:01",
        "Tablespace_Usage": "68.5%"
    })
