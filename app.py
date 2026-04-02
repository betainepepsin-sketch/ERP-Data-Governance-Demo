import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuration for Professional Enterprise Layout
st.set_page_config(page_title="T100 Enterprise ERP System", layout="wide")

# Global System Constants
DEPT_MASTER = [
    "資材部 (INV)", "採購部 (PUR)", "生管部 (PMC)", "銷售部 (SAL)", 
    "製造部 (MFG)", "品管部 (QC)", "研發部 (R&D)", "財務部 (FIN)", 
    "管理部 (ADM)", "會計部 (ACC)", "總經理室 (GM)", "資訊部 (MIS)"
]

def get_dt(d=0):
    return (datetime.now() + timedelta(days=d)).strftime("%Y-%m-%d %H:%M")

# Sidebar Control
st.sidebar.header("T100 System Terminal")
u_id = st.sidebar.selectbox("Active User", ["SYS_ADMIN_01", "MGR_YANG_05", "OP_SFC_12"])
current_dept = st.sidebar.selectbox("Access Department Scope", DEPT_MASTER)
st.sidebar.divider()
st.sidebar.info("Database: T100_PROD\nNode: TW-North-01\nEncryption: AES-256")

# Global Header
st.title("T100 ERP Integrated Enterprise Management")

h1, h2, h3 = st.columns([2, 1, 1])
with h1:
    st.text_input("🔍 Global Search (Doc No / Lot No / Part No / Vendor / Customer)", "")
with h2:
    order_ts = st.selectbox("訂單時間 (Order Period)", ["2026-04", "2026-03", "2026-Q1", "2025-Q4"])
with h3:
    factory_site = st.selectbox("Operational Site", ["一廠 (台北)", "二廠 (桃園)", "三廠 (越南)", "外包加工倉"])

st.divider()

# Module Definition
tabs = st.tabs([
    "📦 庫存資材", "🛒 採購供應", "⚙️ 生產管制", "💰 財務應付", 
    "📊 銷售管理", "🧪 品質檢驗", "🛠️ 研發工程", "📂 人事薪資", 
    "🚚 物流配送", "📐 固定資產", "📈 成本會計", "📝 稽核紀錄"
])

# 1. Inventory & Material
with tabs[0]:
    inv_rows = []
    for i in range(15):
        inv_rows.append({
            "料號代碼": f"YF-P-{500+i}", "品名規格": f"Component-X{i}", "類別": "半成品", "儲位": f"WH-A{i}",
            "現有庫存": 1500+i, "預計領用": 200, "安全水位": 500, "在途量": 100, "外包商": "N/A",
            "一廠庫存": 800, "二廠庫存": 700, "批號控制": f"BN-{202604+i}", "單位": "PCS",
            "建立者": u_id, "建立日期": get_dt(-10), "修改日期": get_dt(), "狀態": "Active"
        })
    st.data_editor(pd.DataFrame(inv_rows), use_container_width=True, hide_index=True)

# 2. Procurement
with tabs[1]:
    pur_rows = []
    for i in range(15):
        pur_rows.append({
            "採購單號": f"PO-{20260400+i}", "供應商代號": f"V{100+i}", "供應商名稱": f"Vendor-Steel-{i}",
            "採購類型": "一般採購", "付款方式": "T/T 60D", "票期": "60D", "幣別": "TWD", "稅率": "5%",
            "交貨日期": get_dt(i+7), "負責人": "PUR-MGR", "核价單號": f"PRI-{i}", "已交量": 1000,
            "未交量": 200, "備註": "Urgent", "修改人": u_id, "時間戳": get_dt()
        })
    st.data_editor(pd.DataFrame(pur_rows), use_container_width=True, hide_index=True)

# 3. Shop Floor Control
with tabs[2]:
    sfc_rows = []
    for i in range(15):
        sfc_rows.append({
            "工單編號": f"WO-{i:03d}", "產品料號": f"FIN-A{i}", "計畫產量": 5000, "報工數量": 4200,
            "製程站別": "組裝段", "產線": "LINE-01", "機台代號": f"MC-{i}", "良率": "99.2%",
            "預計開工": get_dt(-1), "預計完工": get_dt(2), "班別": "Day-Shift", "作業員": f"OP-{i}",
            "工時紀錄": "8.5H", "缺料狀態": "None", "更新者": u_id
        })
    st.data_editor(pd.DataFrame(sfc_rows), use_container_width=True, hide_index=True)

# 4. Financial (A/P)
with tabs[3]:
    fin_rows = []
    for i in range(15):
        fin_rows.append({
            "應付單號": f"AP-{i:03d}", "對帳單號": f"ST-{i}", "來源單號": f"PO-{i}", "金額": 150000+i,
            "發票號碼": f"GUV-{i}", "科目代碼": "2141", "對象": "Vendor-A", "票據日期": get_dt(30),
            "付款條件": "月結", "銀行帳號": "008-123XXX", "幣別": "TWD", "匯率": 1.0, "審核": "Approved"
        })
    st.data_editor(pd.DataFrame(fin_rows), use_container_width=True, hide_index=True)

# 5. Sales Management
with tabs[4]:
    sal_rows = []
    for i in range(15):
        sal_rows.append({
            "銷單號": f"SO-{i:03d}", "客戶代號": f"C-{i}", "客戶名稱": "Global-Tech", "預計交期": get_dt(10),
            "訂單總額": 500000, "出貨倉庫": factory_site, "運送方式": "Truck", "業務": "SALES-A",
            "付款協議": "O/A 30", "信用額度": 1000000, "已出貨": 0, "未出貨": 500000, "修改": u_id
        })
    st.data_editor(pd.DataFrame(sal_rows), use_container_width=True, hide_index=True)

# 6. Quality Control
with tabs[5]:
    qc_rows = []
    for i in range(15):
        qc_rows.append({
            "檢驗單": f"QC-{i}", "來源": "IQC", "判定": "Pass", "不良數": 0, "檢驗員": "QC-MGR",
            "AQL標準": "0.65", "抽樣數": 80, "異常代碼": "N/A", "處理建議": "Release", "時間": get_dt()
        })
    st.data_editor(pd.DataFrame(qc_rows), use_container_width=True, hide_index=True)

# 7. R&D Engineering
with tabs[6]:
    rd_rows = []
    for i in range(15):
        rd_rows.append({
            "BOM編號": f"BOM-{i}", "主料號": f"FIN-{i}", "版本": f"REV-{i}", "設計者": "ENG-WANG",
            "ECN單號": f"ECN-{i}", "圖面編號": f"DWG-{i}", "研發狀態": "Production", "發行日期": get_dt(-100)
        })
    st.data_editor(pd.DataFrame(rd_rows), use_container_width=True, hide_index=True)

# 8. Human Resources
with tabs[7]:
    hr_rows = []
    for i in range(15):
        hr_rows.append({
            "工號": f"EMP-{i:03d}", "姓名": f"Staff-{i}", "職位": "Senior Eng", "到職日": "2022-01-01",
            "考勤": "Normal", "薪資卡號": "822-000XXX", "保險狀態": "Insured", "合約": "Permanent"
        })
    st.data_editor(pd.DataFrame(hr_rows), use_container_width=True, hide_index=True)

# 9. Logistics
with tabs[8]:
    log_rows = []
    for i in range(15):
        log_rows.append({
            "配送單": f"DEL-{i}", "承運商": "SF-Exp", "車號": f"CAR-{i}", "司機": "Driver-A",
            "路徑": "Plant -> Port", "預計抵達": get_dt(1), "狀態": "In-Transit", "簽收": "Pending"
        })
    st.data_editor(pd.DataFrame(log_rows), use_container_width=True, hide_index=True)

# 10. Fixed Assets
with tabs[9]:
    fam_rows = []
    for i in range(15):
        fam_rows.append({
            "資產ID": f"FA-{i}", "名稱": "CNC Machine", "原值": 1200000, "累計折舊": 200000,
            "淨值": 1000000, "保管人": "MFG-MGR", "存放點": "Workshop-A", "購買日": "2024-01-01"
        })
    st.data_editor(pd.DataFrame(fam_rows), use_container_width=True, hide_index=True)

# 11. Cost Accounting
with tabs[10]:
    cost_rows = []
    for i in range(15):
        cost_rows.append({
            "產品": f"P-{i}", "料工費合計": 450.5, "材料費": 300, "人工費": 100, "製費": 50.5,
            "標準": 440, "差異": 10.5, "分析日期": "2026-03-31", "結算人": "FIN-ACC"
        })
    st.data_editor(pd.DataFrame(cost_rows), use_container_width=True, hide_index=True)

# 12. Audit System Logs
with tabs[11]:
    sys_rows = []
    for i in range(15):
        sys_rows.append({
            "ID": i, "Action": "UPDATE", "Table": "TB_PUR_01", "User": u_id, "IP": "10.2.14.5",
            "Result": "SUCCESS", "Time": get_dt(), "Payload": f"DocID={20260400+i}"
        })
    st.dataframe(pd.DataFrame(sys_rows), use_container_width=True, hide_index=True)

# System Footer
st.divider()
st.caption("Terminal Cluster: AS-HOST-01 | Instance: PRD_T100 | Kernel: v5.8.22")
