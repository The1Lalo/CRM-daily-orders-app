# app.py
import streamlit as st
import pandas as pd

# --- ۱) داده‌های تاریخی ---
nli_share = pd.DataFrame({
    1: [21.711684, 16.118861, 15.034289, 16.583282, 12.209929, 9.912489, 8.429466],
    2: [21.213604, 15.335324, 11.963968, 18.106597, 12.785003, 10.154376, 10.441128],
    3: [20.610673, 14.943540, 11.409406, 20.422512, 13.551898, 10.061606, 9.000365],
    4: [20.827834, 14.786823, 11.563077, 19.189448, 13.577198, 10.934636, 9.120985],
    5: [20.628490, 10.088083, 11.353579, 20.676401, 15.158034, 12.881254, 9.214158],
}, index=[1,2,3,4,5,6,7])
nli_share.index.name = 'Day'

churn_shares = pd.DataFrame({
    1: [20.284210, 16.364614, 12.778718, 18.437817, 12.517431, 11.110729, 8.506481],
    2: [20.587293, 15.803377, 11.659074, 19.384095, 13.959417, 11.957428, 6.649317],
    3: [20.250918, 11.259850, 10.081655, 19.287457, 14.421064, 14.493234, 10.205822],
}, index=[1,2,3,4,5,6,7])
churn_shares.index.name = 'Day'

# تنظیمات صفحه
st.set_page_config(
    page_title="Daily Orders Calculator",
    layout="wide"
)
st.title("🎯 Daily Orders Calculator")

# نگاشت برچسب‌ها به شاخص‌ها
nli_map = {
    "nli_1&2Ord 1-14": 1,
    "nli_1&2 ord 15_28": 2,
    "nli1&2ord 29_60": 3,
    "nli1&2ord 61_90": 4,
    "nli1&2ord 90_sd": 5,
}
churn_map = {
    "churn 29_60": 1,
    "churn 61_90": 2,
    "churn 91_startdate": 3,
}

# انتخاب نوع داده
mode = st.sidebar.radio(
    "کدام داده را می‌خواهید محاسبه کنید؟",
    ("NLI Segments", "Churn Groups")
)

if mode == "NLI Segments":
    st.header("📊 NLI Daily Orders")
    # نمایش منوی کشویی با برچسب
    seg_label = st.sidebar.selectbox("انتخاب Segment", options=list(nli_map.keys()))
    seg = nli_map[seg_label]
    size = st.sidebar.number_input("Seg Size", min_value=1, value=1000, step=100)
    seg_cr_pct = st.sidebar.slider("Seg CR", min_value=0.0, max_value=100.0, value=5.0, step=0.5, format="%.1f%%")
    cr = seg_cr_pct / 100

    total = size * cr
    daily = (nli_share[seg] / 100 * total).round(2).to_frame("Daily Orders")
    st.subheader(f"{seg_label} — Total Orders: {int(total)}")
    st.table(daily)
    st.bar_chart(daily, use_container_width=True)

else:
    st.header("📊 Churn Daily Orders")
    ch_label = st.sidebar.selectbox("انتخاب Churn Group", options=list(churn_map.keys()))
    ch = churn_map[ch_label]
    size = st.sidebar.number_input("Churn Size", min_value=1, value=500, step=50)
    churn_cr_pct = st.sidebar.slider("Churn Rate", min_value=0.0, max_value=100.0, value=2.0, step=0.5, format="%.1f%%")
    cr = churn_cr_pct / 100

    total = size * cr
    daily = (churn_shares[ch] / 100 * total).round(2).to_frame("Daily Orders")
    st.subheader(f"{ch_label} — Total Orders: {int(total)}")
    st.table(daily)
    st.line_chart(daily, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
