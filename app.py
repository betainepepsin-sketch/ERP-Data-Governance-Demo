import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page to wide mode for multi-column ERP tables
st.set_page_config(page_title="T100 Enterprise ERP System", layout="wide")

def get_current_time(offset_days=0):
    return (datetime.now() + timedelta(days=offset_days)).strftime("%Y-%m-%d %H:%M")

# 12 Departments according to T100 Org Structure
DEPARTMENTS = [
    "生管部 (PMC)", "採購部 (PUR)", "業務部 (SAL)", "資材部 (INV)", 
    "製造部 (MFG)", "品管部 (QC)", "研發部 (R&D)", "財務部 (FIN)", 
    "管理部 (ADM)", "經理室 (MGR)", "總經理室 (GM)", "資訊部 (MIS)"
]

# Sidebar Config
st.sidebar.header("User Environment")
current_user = st.sidebar.selectbox("Current User ID", ["SYS-ADMIN", "PMC-USER-01", "PUR-MGR-05", "FIN-ACC-02"])
st.sidebar.info(f"Connected to: T100_PROD_DB\nStatus: Operational")

# Top Header Section
st.title("T100 Enterprise Resource Planning - Multi-Module Integrated System")

h_col1, h_col2, h_col3 = st.columns([2, 1, 1])
with h_col1:
    global_search = st.text_input("🔍 全域單據/料號/供應商關鍵字搜尋", "")
with h_col2:
    dept_ctx = st.selectbox("權責部門切換", DEPARTMENTS)
with h_col3:
    st.write("")
    if st.button("執行同步 (Data Sync)"):
        st.toast("Database Sync Completed.")

st.divider()

# 12 Core ERP Modules as Tabs
tab_list = [
    "📦 庫存資材", "🛒 採購供應", "⚙️ 生產管制", "💰 財務應付", 
    "📊 銷售管理", "🧪 品質檢驗", "🛠️ 研發工程", "📂 人事薪資", 
    "🚚 物流配送", "📐 固定資產", "📈 成本會計", "📝 稽核紀錄"
]
tabs = st.tabs(tab_list)

# --- Module 01: Inventory ---
with tabs[0]:
    st.subheader("INV - Inventory Material Management")
    inv_data = {
        "料號代號": [f"YF-R-100{i}" for i in range(12)],
        "品名規格": ["不鏽鋼板", "伺服馬達", "驅動電路", "密封膠條", "高壓閥門", "散熱模組", "感應元件", "連接導線", "機殼組件", "避震彈簧", "控制面板", "緊固螺栓"],
        "現有庫存": [5200, 150, 300, 5000, 45, 210, 1500, 8000, 120, 400, 85, 50000],
        "單位": ["KG", "SET", "PCS", "M", "PCS", "PCS", "PCS", "M", "PCS", "PCS", "SET", "PCS"],
        "儲位": [f"WH-A{i:02d}" for i in range(12)],
        "建立時間": [get_current_time(-30) for _ in range(12)],
        "最後修改時間": [get_current_time() for _ in range(12)],
        "經手人": [current_user for _ in range(12)]
    }
    st.data_editor(pd.DataFrame(inv_data), use_container_width=True, hide_index=True)

# --- Module 02: Purchase ---
with tabs[1]:
    st.subheader("PUR - Strategic Sourcing & Procurement")
    pur_data = {
        "採購單號": [f"PUR202604-{i:03d}" for i in range(12)],
        "供應商代號": [f"V-TW{100+i}" for i in range(12)],
        "供應商名稱": ["台鋼工業", "精密電子", "歐美機件", "強固包裝", "萬聯線材", "感測科技", "永泰化學", "中鋼結構", "遠東紡織", "南亞塑膠", "日月光材", "光寶電組"],
        "付款方式": ["T/T 30D", "L/C at Sight", "T/T 60D", "Cash", "T/T 90D", "T/T 30D", "L/C 30D", "T/T 60D", "T/T 30D", "Cash", "T/T 30D", "L/C 60D"],
        "票期": ["30", "0", "60", "0", "90", "30", "30", "60", "30", "0", "30", "60"],
        "交貨日期": [get_current_time(i+5) for i in range(12)],
        "未交數量": [100, 20, 50, 0, 15, 200, 0, 500, 40, 0, 10, 1000],
        "已交數量": [900, 80, 250, 1000, 85, 1800, 50, 4500, 160, 500, 90, 9000],
        "負責人": ["PUR-MGR-01" for _ in range(12)]
    }
    st.data_editor(pd.DataFrame(pur_data), use_container_width=True, hide_index=True)

# --- Module 03: Production ---
with tabs[2]:
    st.subheader("SFC - Shop Floor Control & Planning")
    sfc_data = {
        "工單號碼": [f"WO-MFG-{2600+i}" for i in range(12)],
        "產品代號": [f"PROD-X{i}" for i in range(12)],
        "預計產量": [1000 for _ in range(12)],
        "完工數量": [800, 500, 1000, 0, 450, 900, 300, 700, 150, 0, 80, 500],
        "製程站別": ["沖壓", "銲接", "塗裝", "組裝", "測試", "包裝", "沖壓", "銲接", "測試", "組裝", "組裝", "檢驗"],
        "計畫開工": [get_current_time(-i) for i in range(12)],
        "計畫完工": [get_current_time(i) for i in range(12)],
        "當班負責人": ["OP-ADMIN" for _ in range(12)]
    }
    st.data_editor(pd.DataFrame(sfc_data), use_container_width=True, hide_index=True)

# --- Module 04: Financial (BPM Approval) ---
with tabs[3]:
    st.subheader("FIN - Accounts Payable & BPM Workflow")
    fin_data = {
        "勾選": [False for _ in range(12)],
        "單據編號": [f"AP-INV-{i:03d}" for i in range(12)],
        "金額 (TWD)": [15000 * i for i in range(1, 13)],
        "付款方式": "匯款",
        "申請部門": DEPARTMENTS,
        "申請人": ["USER-A" for _ in range(12)],
        "狀態": ["待簽核" if i % 2 == 0 else "核准" for i in range(12)],
        "建立時間": [get_current_time(-1) for _ in range(12)]
    }
    st.data_editor(pd.DataFrame(fin_data), use_container_width=True, hide_index=True)
    c1, c2, c3 = st.columns([1, 1, 8])
    with c1:
        if st.button("✅ 批次核准 (Post)"): st.success("Approved Successfully.")
    with c2:
        if st.button("❌ 退回 (Reject)"): st.error("Returned to Requester.")

# --- Module 12: Audit Log ---
with tabs[11]:
    st.subheader("SYS - System Audit Trail (Standard Compliance)")
    log_data = {
        "事件編號": [f"LOG-00{i:02d}" for i in range(12)],
        "操作時間": [get_current_time() for _ in range(12)],
        "操作員 ID": [current_user for _ in range(12)],
        "動作類型": ["Update", "Delete", "Login", "Approve", "Insert", "Export", "Sync", "Update", "Update", "Delete", "Login", "Approve"],
        "影響對象": ["TB_INV_BALANCE", "TB_PUR_ORDER", "SESSION_01", "TB_BPM_PROC", "TB_MFG_SFC", "REPORT_XLSX", "DB_REMOTE", "TB_SAL_PRICE", "TB_INV_SERIAL", "TB_SYS_CONFIG", "SESSION_02", "TB_BPM_PROC"],
        "來源 IP": ["192.168.1.105" for _ in range(12)],
        "備註": ["Standard Operation" for _ in range(12)]
    }
    st.dataframe(pd.DataFrame(log_data), use_container_width=True, hide_index=True)

# Placeholder for remaining empty modules
for i in range(4, 11):
    with tabs[i]:
        st.warning(f"Module '{tab_list[i]}' is currently in Read-Only Mode.")
        st.info("Please contact IT Department for full data access permissions.")
