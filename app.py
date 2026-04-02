import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Standard enterprise configuration
st.set_page_config(page_title="T100 Enterprise ERP System", layout="wide")

def get_ts(offset=0):
    return (datetime.now() + timedelta(days=offset)).strftime("%Y-%m-%d %H:%M")

# User Identity Simulation
st.sidebar.header("User Control Panel")
op_id = st.sidebar.selectbox("System User ID", ["MIS-ADMIN-01", "SALES-MGR-02", "FIN-ACC-05", "PMC-USER-08"])
st.sidebar.divider()
st.sidebar.info("DB Instance: T100_PROD\nRegion: Taiwan-HQ")

st.title("T100 Enterprise Resource Planning - Professional Integration")

# Global Context Headers
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    search_main = st.text_input("🔍 全域關鍵字檢索 (工單/料號/供應商/批號)", "")
with c2:
    target_site = st.selectbox("廠別區域", ["第一廠 (Main Plant)", "第二廠 (Assembly)", "外包加工廠", "保稅倉庫"])
with c3:
    period_select = st.selectbox("會計期間", ["2026-04", "2026-03", "2026-Q1"])

st.divider()

# 12 Professional ERP Modules
tab_labels = [
    "📦 庫存資材", "🛒 採購供應", "⚙️ 生產管制", "💰 財務應付", 
    "📊 銷售管理", "🧪 品質檢驗", "🛠️ 研發工程", "📂 人事薪資", 
    "🚚 物流配送", "📐 固定資產", "📈 成本會計", "📝 稽核紀錄"
]
tabs = st.tabs(tab_labels)

# --- TAB 1: Inventory (觸發左右拉桿) ---
with tabs[0]:
    st.subheader("INV - Inventory Material Control")
    inv_data = {
        "料號": [f"YF-P-{100+i:03d}" for i in range(12)],
        "品名規格": ["不鏽鋼機殼", "主板電路", "馬達模組", "封口墊片", "控制面板", "連接線組", "散熱鰭片", "電源器", "傳感器", "緊固件", "標籤組", "包裝箱"],
        "類別": ["半成品", "組裝品", "組裝品", "原料", "半成品", "原料", "半成品", "外購件", "外購件", "原料", "耗材", "耗材"],
        "現有庫存": [1500, 240, 85, 8000, 450, 2000, 120, 35, 600, 50000, 3000, 1200],
        "未來可用庫存": [1800, 300, 100, 7500, 500, 2100, 150, 40, 650, 48000, 2800, 1100],
        "單位": ["PCS", "PCS", "SET", "M", "PCS", "PCS", "SET", "PCS", "PCS", "KG", "ROLL", "PCS"],
        "儲位代號": [f"W1-A{i:02d}" for i in range(12)],
        "所在廠區": [target_site for _ in range(12)],
        "外包狀態": ["自有" if i % 3 != 0 else "外包加工" for i in range(12)],
        "批號": [f"BATCH2604-{i:02d}" for i in range(12)],
        "安全水位": [500 for _ in range(12)],
        "建立時間": [get_ts(-60) for _ in range(12)],
        "最後異動": [get_ts() for _ in range(12)],
        "經手人": [op_id for _ in range(12)],
        "備註紀錄": ["N/A" for _ in range(12)]
    }
    # 超過 8 個欄位會自動出現左右拉桿
    st.data_editor(pd.DataFrame(inv_data), use_container_width=True, hide_index=True)

# --- TAB 5: Sales (補全內容) ---
with tabs[4]:
    st.subheader("SAL - Order & Shipping Management")
    sal_data = {
        "訂單編號": [f"SO-2026-{i:04d}" for i in range(12)],
        "客戶代號": [f"CUST-{i:03d}" for i in range(12)],
        "客戶名稱": ["美商 Apple", "日商 Sony", "台積電", "鴻海精密", "廣達電腦", "華碩電腦", "微星科技", "戴爾", "惠普", "聯想", "三星", "LG"],
        "預計交期": [get_ts(i+10) for i in range(12)],
        "幣別": ["USD", "TWD", "JPY", "EUR", "USD", "TWD", "TWD", "USD", "USD", "CNY", "KRW", "USD"],
        "訂單總額": [50000 * i for i in range(1, 13)],
        "業務負責人": ["SALES-01" for _ in range(12)],
        "出貨狀態": ["待出貨", "部分交貨", "已結案", "待出貨", "待出貨", "待出貨", "已結案", "部分交貨", "已結案", "待出貨", "待出貨", "待出貨"],
        "付款條件": "OA 30 Days",
        "建立時間": get_ts(-5),
        "修改紀錄": "Rev.0"
    }
    st.data_editor(pd.DataFrame(sal_data), use_container_width=True, hide_index=True)

# --- TAB 6: Quality (補全內容) ---
with tabs[5]:
    st.subheader("QC - Quality Assurance & Inspection")
    qc_data = {
        "檢驗單號": [f"QC-0402-{i:03d}" for i in range(12)],
        "來源單號": [f"PUR-0401-{i:03d}" for i in range(12)],
        "品名規格": ["精密螺母", "電容 A1", "鋁質外殼", "連接頭", "包裝膜", "說明書", "PCB板", "散熱膠", "電池芯", "塑膠件", "緩衝墊", "外盒"],
        "檢驗結果": ["合格", "合格", "異常", "合格", "待複檢", "合格", "合格", "異常", "合格", "合格", "合格", "待複檢"],
        "異常原因": ["無", "無", "表面刮傷", "無", "厚度不足", "無", "無", "過期", "無", "無", "無", "印刷錯誤"],
        "檢驗員": ["QC-DAVID" for _ in range(12)],
        "判定時間": get_ts()
    }
    st.data_editor(pd.DataFrame(qc_data), use_container_width=True, hide_index=True)

# --- TAB 7: R&D (補全內容) ---
with tabs[6]:
    st.subheader("R&D - Product Engineering (BOM)")
    rd_data = {
        "專案代號": [f"PROJ-V26-{i:02d}" for i in range(12)],
        "版本號": [f"V{i}.0" for i in range(12)],
        "設計負責人": ["ENG-CHEN", "ENG-LIN", "ENG-WANG"] * 4,
        "研發狀態": ["設計中", "打樣中", "驗證完成", "量產導入"] * 3,
        "CAD檔案編號": [f"DWG-F{1000+i}" for i in range(12)],
        "建立日期": get_ts(-100)
    }
    st.data_editor(pd.DataFrame(rd_data), use_container_width=True, hide_index=True)

# --- TAB 8: HR (補全內容) ---
with tabs[7]:
    st.subheader("HR - Personnel & Payroll Admin")
    hr_data = {
        "工號": [f"EMP-{1000+i}" for i in range(12)],
        "姓名": ["張一", "李二", "王三", "趙四", "錢五", "孫六", "李七", "周八", "吳九", "鄭十", "劉十一", "陳十二"],
        "部門": DEPARTMENTS * 1,
        "職位": ["經理", "課長", "組長", "專員", "技術員", "技術員", "專員", "專員", "課長", "經理", "技術員", "專員"],
        "出勤狀況": "正常",
        "入職日期": "2020-01-01"
    }
    st.data_editor(pd.DataFrame(hr_data), use_container_width=True, hide_index=True)

# --- TAB 9: Logistics (補全內容) ---
with tabs[8]:
    st.subheader("DEL - Logistics & Fleet Tracking")
    del_data = {
        "物流單號": [f"SHIP-{i:04d}" for i in range(12)],
        "物流公司": ["順豐", "黑貓", "嘉里大榮", "新竹物流"] * 3,
        "車牌號碼": [f"ABC-{100+i}" for i in range(12)],
        "目的地": ["桃園總倉", "台中分部", "高雄二廠", "新竹園區"] * 3,
        "配送狀態": "運送中",
        "預計到達": get_ts(1)
    }
    st.data_editor(pd.DataFrame(del_data), use_container_width=True, hide_index=True)

# --- TAB 10: Fixed Assets (補全內容) ---
with tabs[9]:
    st.subheader("FAM - Fixed Asset Management")
    fam_data = {
        "資產編號": [f"FA-MACH-{i:03d}" for i in range(12)],
        "資產名稱": ["沖壓機", "CNC切削機", "SMT機台", "測試機", "堆高機", "伺服器", "辦公室家具", "空壓機", "封口機", "噴碼機", "投影機", "冷氣主機"],
        "原值": [500000 * i for i in range(1, 13)],
        "折舊年限": ["10年", "8年", "5年", "5年", "10年", "3年", "5年", "8年", "5年", "5年", "3年", "10年"],
        "使用狀態": "使用中"
    }
    st.data_editor(pd.DataFrame(fam_data), use_container_width=True, hide_index=True)

# --- TAB 11: Cost (補全內容) ---
with tabs[10]:
    st.subheader("COST - Product Costing & Analysis")
    cost_data = {
        "產品代號": [f"YF-PROD-{i:03d}" for i in range(12)],
        "標準成本": [100.0, 150.5, 200.0, 45.0, 89.0, 120.0, 350.0, 1000.0, 55.0, 78.0, 12.0, 95.0],
        "實際成本": [102.0, 149.0, 210.0, 44.0, 92.0, 118.0, 360.0, 980.0, 56.0, 80.0, 13.0, 90.0],
        "差異額": [2.0, -1.5, 10.0, -1.0, 3.0, -2.0, 10.0, -20.0, 1.0, 2.0, 1.0, -5.0],
        "結算日期": "2026-03-31"
    }
    st.data_editor(pd.DataFrame(cost_data), use_container_width=True, hide_index=True)

# --- TAB 12: Audit ---
with tabs[11]:
    st.subheader("SYS - Security Audit Tracking")
    # 此處已修正，不使用 code 形式，改用 Table
    audit_data = {
        "Seq": range(1, 13),
        "Event_ID": [f"EVT-99{i:02d}" for i in range(12)],
        "User": op_id,
        "Table_Modified": "TB_GLOBAL_MASTER",
        "Action": "Query/Update",
        "Client_IP": "172.16.0.45",
        "Time": get_ts()
    }
    st.table(pd.DataFrame(audit_data))
