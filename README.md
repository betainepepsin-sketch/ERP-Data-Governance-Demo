import streamlit as st
import pandas as pd

st.set_page_config(page_title="T100 ERP Management System", layout="wide")

if 'auth_success' not in st.session_state:
    st.session_state.auth_success = False

st.sidebar.title("ERP Authentication")
access_code = st.sidebar.text_input("Enter 8-digit Access Code", type="password")

if len(access_code) == 8 and access_code == "12345678":
    st.session_state.auth_success = True
    st.sidebar.success("Authentication Verified")
elif len(access_code) > 0:
    st.sidebar.error("Invalid Access Code")

if st.session_state.auth_success:
    st.title("T100 ERP Enterprise Resource Planning")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 全域關鍵字搜尋 (料號/品名/供貨商)", "")
    with col2:
        category_filter = st.selectbox("單據類型", ["全部單據", "採購訂單", "生產工單", "庫存異動"])
    with col3:
        status_filter = st.selectbox("簽核狀態", ["全部", "待簽核", "已核准", "退回"])

    st.divider()

    tabs = st.tabs(["庫存管理作業", "生產報工系統", "電子簽核中心", "系統維護紀錄"])

    with tabs[0]:
        raw_data = {
            "料號": ["YF-A001", "YF-A002", "YF-B001", "YF-B002", "YF-C001", "YF-C002", "YF-D001", "YF-D002"],
            "品名規格": ["不鏽鋼外殼", "高壓密封墊", "主控電路板", "散熱模組", "感應器單元", "連接線組", "工業級外箱", "防震泡棉"],
            "現有庫存": [1200, 450, 80, 200, 150, 3000, 50, 500],
            "單位": ["PCS", "SET", "PCS", "PCS", "PCS", "M", "PCS", "ROLL"],
            "安全水位": [1000, 500, 100, 150, 100, 2500, 40, 400],
            "單價(未稅)": [450, 120, 3500, 850, 1200, 45, 1800, 250],
            "儲位": ["A-01-01", "A-02-05", "B-01-03", "B-03-01", "C-01-02", "D-05-01", "E-01-01", "E-02-01"],
            "供貨商": ["台鋼實業", "歐美貿易", "精密電子", "散熱專家", "感測科技", "萬聯線材", "強固包裝", "防震材料"]
        }
        df = pd.DataFrame(raw_data)
        
        if search_query:
            df = df[df['料號'].str.contains(search_query) | df['品名規格'].str.contains(search_query)]

        st.write("### 實時庫存清單 (可直接編輯數值)")
        edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

    with tabs[2]:
        st.write("### 電子簽核中心 (BPM Workflow)")
        approval_data = {
            "單據編號": ["PUR-20260401-001", "MFG-20260401-023", "INV-20260331-045"],
            "申請部門": ["採購部", "生產部", "倉庫"],
            "申請人": ["張曉明", "李大華", "王小美"],
            "摘要": ["原材料採購申請", "機殼生產報工", "逾期料件報廢"],
            "金額": [550000, 0, 12500],
            "狀態": ["待簽核", "待簽核", "已核准"]
        }
        st.table(pd.DataFrame(approval_data))
        
        col_btn1, col_btn2 = st.columns([1, 10])
        with col_btn1:
            if st.button("核准選取單據"):
                st.success("已完成簽核程序")
        with col_btn2:
            st.button("退回單據")

    with tabs[3]:
        st.info("System Version: T100-V5.3.2 | Database: Oracle 19c | Server Status: Operational")
        st.text_area("System Log", "2026-04-02 09:00:15 - Backup completed.\n2026-04-02 10:30:22 - SQL Query optimization finished.")

else:
    st.info("Please enter the 8-digit system access code in the sidebar to initialize ERP environment.")
    st.image("https://img.icons8.com/clouds/200/000000/lock-landscape.png")
