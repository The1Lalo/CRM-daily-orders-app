# app.py
import streamlit as st
import pandas as pd

# --- داده‌های تاریخی ---
# NLI shares for rem_nli Day 4 scenario (Relative Day 1-7)
nli_day4 = pd.DataFrame({
    1: [21.711684, 16.118861, 15.034289, 16.583282, 12.209929, 9.912489, 8.429466],
    2: [21.213604, 15.335324, 11.963968, 18.106597, 12.785003, 10.154376, 10.441128],
    3: [20.610673, 14.943540, 11.409406, 20.422512, 13.551898, 10.061606, 9.000365],
    4: [20.827834, 14.786823, 11.563077, 19.189448, 13.577198, 10.934636, 9.120985],
    5: [20.628490, 10.088083, 11.353579, 20.676401, 15.158034, 12.881254, 9.214158],
}, index=[1,2,3,4,5,6,7])
nli_day4.index.name = 'Day'

# NLI shares for Reminder Day 5 (only segments 2-4 provided, 1 & 5 averaged)
nli_day5 = pd.DataFrame({
    2: [24.265389, 14.380861, 9.495267, 9.269872, 18.347022, 15.460416, 8.781174],
    3: [22.910380, 14.013488, 9.750170, 8.227991, 18.392384, 17.221041, 9.484546],
    4: [23.826975, 14.149628, 9.696535, 8.299591, 19.013721, 16.241660, 8.771890],
}, index=[1,2,3,4,5,6,7])
nli_day5.index.name = 'Day'
# Fill segments 1 & 5 by averaging 2-4
avg_nli = nli_day5.mean(axis=1)
nli_day5[1] = avg_nli
nli_day5[5] = avg_nli
nli_day5 = nli_day5[[1,2,3,4,5]]

# Churn shares for two reminder scenarios
churn_day4 = pd.DataFrame({
    1: [20.284210, 16.364614, 12.778718, 18.437817, 12.517431, 11.110729, 8.506481],
    2: [20.587293, 15.803377, 11.659074, 19.384095, 13.959417, 11.957428, 6.649317],
    3: [20.250918, 11.259850, 10.081655, 19.287457, 14.421064, 14.493234, 10.205822],
}, index=[1,2,3,4,5,6,7])
churn_day4.index.name = 'Day'

churn_day5 = pd.DataFrame({
    1: [25.227468, 15.982380, 11.053946, 8.574631, 15.792417, 15.887211, 7.481948],
    2: [21.839262, 15.252314, 13.406240, 13.175335, 17.053160, 12.539152, 6.734537],
    3: [23.851160, 12.611638, 13.306372, 10.842209, 16.645724, 15.215174, 7.527723],
}, index=[1,2,3,4,5,6,7])
churn_day5.index.name = 'Day'

# تنظیمات صفحه
st.set_page_config(page_title="Daily Orders Calculator", layout="wide")
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

# نوار کناری: انتخاب داده و سناریو
mode = st.sidebar.radio("کدام داده را می‌خواهید محاسبه کنید؟", ("NLI Segments", "Churn Groups"))

if mode == "NLI Segments":
    st.header("📊 NLI Daily Orders")
    rem_nli = st.sidebar.radio("Reminder Day for NLI", ("Day 4", "Day 5"))
    shares = nli_day4 if rem_nli == "Day 4" else nli_day5

    seg_label = st.sidebar.selectbox("انتخاب Segment", options=list(nli_map.keys()))
    seg = nli_map[seg_label]
    size = st.sidebar.number_input("Seg Size", min_value=1, value=1000, step=100)
    seg_cr_pct = st.sidebar.slider("Seg CR", min_value=0.0, max_value=100.0, value=5.0, step=0.5, format="%.1f%%")
    cr = seg_cr_pct / 100

    total = size * cr
    daily = (shares[seg] / 100 * total).round(2).to_frame("Daily Orders")
    st.subheader(f"{seg_label} ({rem_nli}) — Total Orders: {int(total)}")
    st.table(daily)
    st.bar_chart(daily, use_container_width=True)

else:
    st.header("📊 Churn Daily Orders")
    rem_ch = st.sidebar.radio("Reminder Day for Churn", ("Day 4", "Day 5"))
    shares = churn_day4 if rem_ch == "Day 4" else churn_day5

    ch_label = st.sidebar.selectbox("انتخاب Churn Group", options=list(churn_map.keys()))
    ch = churn_map[ch_label]
    # unified Seg Size label
    size = st.sidebar.number_input("Seg Size", min_value=1, value=500, step=50)
    churn_cr_pct = st.sidebar.slider("Seg CR", min_value=0.0, max_value=100.0, value=2.0, step=0.5, format="%.1f%%")
    cr = churn_cr_pct / 100

    total = size * cr
    daily = (shares[ch] / 100 * total).round(2).to_frame("Daily Orders")
    st.subheader(f"{ch_label} ({rem_ch}) — Total Orders: {int(total)}")
    st.table(daily)
    st.line_chart(daily, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
