import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. 全域變數定義 (確保不發生 NameError)
DEPT_LIST = [
    "資材部 (INV)", "採購部 (PUR)", "生管部 (PMC)", "銷售部 (SAL)", 
    "製造部 (MFG)", "品管部 (QC)", "研發部 (R&D)", "財務部 (FIN)", 
    "管理部 (ADM)", "經理室 (MGR)", "總經理室 (GM)", "資訊部 (MIS)",
    "會計部 (ACC)", "物流部 (LOG)", "工安部 (ESH)"
]

st.set_page_config(page_title="T100 ERP Enterprise System", layout="wide")

def get_time(days=0):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M")

# Sidebar
st.sidebar.header("ERP 系統權限控制")
auth_user = st.sidebar.selectbox("登入帳號", ["ADMIN-001", "MANAGER-05", "USER-SFC-02"])
# 新增要求：至少 12 個部門的下拉選單
current_dept = st.sidebar.selectbox("切換當前部門", DEPT_LIST)
st.sidebar.divider()
st.sidebar.success(f"連線狀態: T100_PROD_ACTIVE")

# Header
st.title("T100 ERP 企業級整合管理系統")

c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    st.text_input("🔍 全域關鍵字搜尋 (料號/單據/供應商/批號/負責人)", "")
with c2:
    # 修改要求：下拉選單改為「訂單時間」
    order_period = st.selectbox("訂單時間 (Order Period)", ["2026-04", "2026-03", "2026-Q1", "2025-Q4"])
with c3:
    site_loc = st.selectbox("營運中心/廠區", ["一廠 (台北)", "二廠 (桃園)", "三廠 (越南)", "外包倉"])

st.divider()

# 12 Professional Tabs
tabs = st.tabs([
    "📦 庫存資材", "🛒 採購供應", "⚙️ 生產管制", "💰 財務應付", 
    "📊 銷售管理", "🧪 品質檢驗", "🛠️ 研發工程", "📂 人事薪資", 
    "🚚 物流配送", "📐 固定資產", "📈 成本會計", "📝 稽核紀錄"
])

# 共通函式：生成超過 15 欄的資料以觸發左右拉桿
def generate_erp_data(module_type):
    data = []
    for i in range(15):  # 固定生成 15 筆，觸發上下拉桿
        row = {
            "單據/料號代碼": f"{module_type}-{20260400+i}",
            "品名規格": f"工業級組件-{i:02d} 型",
            "類別": ["半成品", "組裝品", "外包加工", "原料", "成品"][i%5],
            "廠別位置": site_loc,
            "目前庫存": 1000 + (i*50),
            "未來預估庫存": 1200 + (i*45),
            "安全水位": 500,
            "供應商代號": f"V-{500+i}",
            "供應商名稱": ["台鋼", "鴻海", "廣達", "緯創", "仁寶"][i%5],
            "付款方式": ["T/T 30D", "L/C", "Cash", "T/T 60D"][i%4],
            "票期": f"{30+(i*5)}D",
            "交貨時間": get_time(i),
            "已交數量": 5000,
            "未交數量": 200,
            "經手人": f"OP-{i:03d}",
            "負責人": f"MGR-{i:02d}",
            "建立時間": get_time(-10),
            "最後修改時間": get_time(),
            "備註事項": "系統自動核算中"
        }
        data.append(row)
    return pd.DataFrame(data)

# 分別填充 12 個模組的內容
with tabs[0]: # 庫存
    st.subheader("INV - Inventory & Material Master")
    st.data_editor(generate_erp_data("INV"), use_container_width=True, hide_index=True)

with tabs[1]: # 採購
    st.subheader("PUR - Procurement Management")
    st.data_editor(generate_erp_data("PUR"), use_container_width=True, hide_index=True)

with tabs[2]: # 生產
    st.subheader("SFC - Production & Shop Floor Control")
    st.data_editor(generate_erp_data("SFC"), use_container_width=True, hide_index=True)

with tabs[3]: # 財務
    st.subheader("FIN - Accounts Payable/Receivable")
    st.data_editor(generate_erp_data("FIN"), use_container_width=True, hide_index=True)

with tabs[4]: # 銷售
    st.subheader("SAL - Sales & Distribution")
    st.data_editor(generate_erp_data("SAL"), use_container_width=True, hide_index=True)

with tabs[5]: # 品檢
    st.subheader("QC - Quality Control & Inspection")
    st.data_editor(generate_erp_data("QC"), use_container_width=True, hide_index=True)

with tabs[6]: # 研發
    st.subheader("R&D - Engineering Change Management")
    st.data_editor(generate_erp_data("R&D"), use_container_width=True, hide_index=True)

with tabs[7]: # 人事
    st.subheader("HR - Human Capital Management")
    st.data_editor(generate_erp_data("HR"), use_container_width=True, hide_index=True)

with tabs[8]: # 物流
    st.subheader("LOG - Logistics & Delivery Tracking")
    st.data_editor(generate_erp_data("LOG"), use_container_width=True, hide_index=True)

with tabs[9]: # 固資
    st.subheader("FAM - Fixed Asset Management")
    st.data_editor(generate_erp_data("FAM"), use_container_width=True, hide_index=True)

with tabs[10]: # 成本
    st.subheader("COST - Cost Accounting & Analysis")
    st.data_editor(generate_erp_data("COST"), use_container_width=True, hide_index=True)

with tabs[11]: # 稽核
    st.subheader("SYS - System Audit & Security Logs")
    # 稽核模組通常不使用 editor 改用 dataframe
    st.dataframe(generate_erp_data("LOG"), use_container_width=True, hide_index=True)

# Footer Status
st.divider()
col_f1, col_f2 = st.columns(2)
col_f1.write(f"© 2026 T100 ERP Solutions. All Rights Reserved. | Site: {site_loc}")
col_f2.write(f"系統效能: SGA 32GB | Active Processes: 452 | DB Version: Oracle 19c")
