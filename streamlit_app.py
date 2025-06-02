import streamlit as st
import pandas as pd

# --- Historical share data ---

# NLI shares for reminder scenarios (Noon)
nli_day4 = pd.DataFrame({
    1: [21.711684, 16.118861, 15.034289, 16.583282, 12.209929, 9.912489, 8.429466],
    2: [21.213604, 15.335324, 11.963968, 18.106597, 12.785003, 10.154376, 10.441128],
    3: [20.610673, 14.943540, 11.409406, 20.422512, 13.551898, 10.061606, 9.000365],
    4: [20.827834, 14.786823, 11.563077, 19.189448, 13.577198, 10.934636, 9.120985],
    5: [20.628490, 10.088083, 11.353579, 20.676401, 15.158034, 12.881254, 9.214158],
}, index=[1,2,3,4,5,6,7])
nli_day4.index.name = 'Day'

nli_day5 = pd.DataFrame({
    2: [24.265389, 14.380861,  9.495267,  9.269872, 18.347022, 15.460416,  8.781174],
    3: [22.910380, 14.013488,  9.750170,  8.227991, 18.392384, 17.221041,  9.484546],
    4: [23.826975, 14.149628,  9.696535,  8.299591, 19.013721, 16.241660,  8.771890],
}, index=[1,2,3,4,5,6,7])
nli_day5.index.name = 'Day'
avg_nli = nli_day5.mean(axis=1)
nli_day5[1] = avg_nli
nli_day5[5] = avg_nli
nli_day5 = nli_day5[[1,2,3,4,5]]

# NLI shares for Night send (reminder Day 4)
nli_night_day4 = pd.DataFrame({
    2: [14.616076, 13.584018, 14.454298, 22.983899, 16.352979,  9.555648,  8.453083],
    3: [11.076736, 18.660828, 11.942349, 22.129921, 14.113088, 13.370239,  8.706839],
    4: [12.631487, 20.987466, 13.173300, 19.091041, 15.416813, 10.465618,  8.234276],
    5: [14.821537, 19.217584, 14.216576, 21.657592,  8.650938, 13.611615,  7.824158],
}, index=[1,2,3,4,5,6,7])
nli_night_day4.index.name = 'Day'
avg_nli_night = nli_night_day4.mean(axis=1)
nli_night_day4[1] = avg_nli_night
nli_night_day4 = nli_night_day4[[1,2,3,4,5]]

# Churn shares for reminder scenarios (Noon)
churn_day4 = pd.DataFrame({
    1: [20.284210, 16.364614, 12.778718, 18.437817, 12.517431, 11.110729,  8.506481],
    2: [20.587293, 15.803377, 11.659074, 19.384095, 13.959417, 11.957428,  6.649317],
    3: [20.250918, 11.259850, 10.081655, 19.287457, 14.421064, 14.493234, 10.205822],
}, index=[1,2,3,4,5,6,7])
churn_day4.index.name = 'Day'

churn_day5 = pd.DataFrame({
    1: [25.227468, 15.982380, 11.053946,  8.574631, 15.792417, 15.887211,  7.481948],
    2: [21.839262, 15.252314, 13.406240, 13.175335, 17.053160, 12.539152,  6.734537],
    3: [23.851160, 12.611638, 13.306372, 10.842209, 16.645724, 15.215174,  7.527723],
}, index=[1,2,3,4,5,6,7])
churn_day5.index.name = 'Day'

# Churn shares for Night send (reminder Day 4)
churn_night_day4 = pd.DataFrame({
    1: [12.444968, 19.761227, 11.236781, 23.485016, 13.685019, 10.855740,  8.531249],
    2: [11.317538, 22.526437, 13.398942, 20.103059, 13.705939, 11.167455,  7.780631],
    3: [14.508197, 20.901639, 13.442623, 19.918033,  8.852459, 13.114754,  9.262295],
}, index=[1,2,3,4,5,6,7])
churn_night_day4.index.name = 'Day'

# SUNO shares for reminder Day 5 (Noon only)
suno_day5 = pd.DataFrame({
    1: [26.925197, 13.303347,  9.895528,  6.161128, 22.352256, 13.337876,  8.024668],
    2: [25.177297, 12.389750,  9.354067,  6.076514, 22.598724, 14.089013, 10.314636],
    3: [25.482682, 10.398605,  8.001933,  6.041134, 25.664506, 14.709364,  9.701776],
    4: [23.970033, 10.544025,  7.250834,  6.004116, 25.754893, 15.729818, 10.746282],
    5: [23.914282, 11.726879,  8.608781,  6.270109, 24.791565, 14.105966, 10.582418],
    6: [23.498621, 11.911483,  7.084567,  6.475340, 25.688482, 14.275750, 11.065757],
}, index=[1,2,3,4,5,6,7])
suno_day5.index.name = 'Day'

# Label maps
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
suno_map = {
    "suno 3-7": 1,
    "suno 8-14": 2,
    "suno 15-28": 3,
    "suno 29-63": 4,
    "suno 64-91": 5,
    "suno 92-sd": 6,
}

# Page config
st.set_page_config(page_title="Daily Orders Calculator", layout="wide")
st.header("Daily Orders Calculator")

# Mode selection
mode = st.sidebar.radio(
    "Mode",
    ("NLI Segments", "Churn Segments", "SUNO Segments", "Custom Mix")
)

# NLI Segments
if mode == "NLI Segments":
    send_nli_time = st.sidebar.radio("Send Time for NLI", ("Noon", "Night"), key="send_nli_time")
    if send_nli_time == "Noon":
        rem_nli = st.sidebar.radio("Reminder Day for NLI", ("Day 4", "Day 5"), key="rem_nli_main")
        shares = nli_day4 if rem_nli == "Day 4" else nli_day5
    else:
        shares = nli_night_day4
        rem_nli = "Night"

    label = st.sidebar.selectbox("انتخاب Segment", options=list(nli_map.keys()))
    idx = nli_map[label]

    size = st.sidebar.number_input("Seg Size", min_value=1, value=1000, step=100)
    cr_pct = st.sidebar.number_input(
        "Seg CR (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.1f"
    )

    # درصد سهم سگمنت در هر روز (یک رقم اعشاری)
    percent_series = shares[idx].round(1)

    # تعداد سفارش‌های روزانه
    daily = (shares[idx] / 100 * size * (cr_pct / 100)).round(0).astype(int)

    # ساخت DataFrame با ستون‌های "Share (%)" و "Daily Orders"
    df_out = pd.DataFrame({
        "Share (%)": percent_series,
        "Daily Orders": daily
    })
    df_out.index.name = 'Day'

    total = df_out["Daily Orders"].sum()
    header = f"{send_nli_time}" + (f" {rem_nli}" if send_nli_time == "Noon" else "")
    st.markdown(f"##### {label} ({header}) — Total Orders: {total}")

    # نمایش جدول
    st.table(df_out)

    # دکمهٔ دانلود CSV
    csv = df_out.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name=f"nli_{label.replace(' ', '_')}_{header.replace(' ', '_')}.csv",
        mime="text/csv"
    )

# Churn Segments
elif mode == "Churn Segments":
    send_ch_time = st.sidebar.radio("Send Time for Churn", ("Noon", "Night"), key="send_ch_time")
    if send_ch_time == "Noon":
        rem_ch = st.sidebar.radio("Reminder Day for Churn", ("Day 4", "Day 5"), key="rem_ch_main")
        shares = churn_day4 if rem_ch == "Day 4" else churn_day5
    else:
        shares = churn_night_day4
        rem_ch = "Night"

    label = st.sidebar.selectbox("انتخاب Churn Segment", options=list(churn_map.keys()))
    idx = churn_map[label]

    size = st.sidebar.number_input("Seg Size", min_value=1, value=500, step=50)
    cr_pct = st.sidebar.number_input(
        "Seg CR (%)",
        min_value=0.0,
        max_value=100.0,
        value=2.0,
        step=0.1,
        format="%.1f"
    )

    # درصد سهم هر روز (یک رقم اعشاری)
    percent_series = shares[idx].round(1)

    # تعداد سفارش روزانه
    daily = (shares[idx] / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series,
        "Daily Orders": daily
    })
    df_out.index.name = 'Day'

    total = df_out["Daily Orders"].sum()
    header = f"{send_ch_time}" + (f" {rem_ch}" if send_ch_time == "Noon" else "")
    st.markdown(f"##### {label} ({header}) — Total Orders: {total}")

    st.table(df_out)

    csv = df_out.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name=f"churn_{label.replace(' ', '_')}_{header.replace(' ', '_')}.csv",
        mime="text/csv"
    )

# SUNO Segments
elif mode == "SUNO Segments":
    label = st.sidebar.selectbox("انتخاب SUNO Segment", options=list(suno_map.keys()))
    idx = suno_map[label]

    size = st.sidebar.number_input("Seg Size", min_value=1, value=1000, step=100)
    cr_pct = st.sidebar.number_input(
        "Seg CR (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.1f"
    )

    # درصد سهم روزانه (یک رقم اعشاری)
    percent_series = suno_day5[idx].round(1)

    # تعداد سفارش روزانه
    daily = (suno_day5[idx] / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series,
        "Daily Orders": daily
    })
    df_out.index.name = 'Day'

    total = df_out["Daily Orders"].sum()
    st.markdown(f"##### {label} (Day 5) — Total Orders: {total}")

    st.table(df_out)

    csv = df_out.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name=f"suno_{label.replace(' ', '_')}_Day5.csv",
        mime="text/csv"
    )

# Custom Mix
else:
    count = st.sidebar.number_input("How many segment entries?", min_value=1, value=1, step=1)

    # Series صفر برای جمع تعداد سفارش نهایی و جمع درصدها
    total_orders = pd.Series(0.0, index=range(1, 8), name="Total Orders")
    percent_sum = pd.Series(0.0, index=range(1, 8), name="Percent Sum")

    for i in range(count):
        st.sidebar.markdown(f"--- Entry #{i+1} ---")
        seg_type = st.sidebar.selectbox(f"Type #{i+1}", ["NLI", "Churn", "SUNO"], key=f"type_{i}")

        if seg_type == "NLI":
            send = st.sidebar.radio(f"Send Time #{i+1}", ["Noon", "Night"], key=f"send_nli_{i}")
            if send == "Noon":
                rem = st.sidebar.radio(f"Reminder Day #{i+1}", ["Day 4", "Day 5"], key=f"rem_nli_{i}")
                shares = nli_day4 if rem == "Day 4" else nli_day5
            else:
                shares = nli_night_day4
            mapping = nli_map

        elif seg_type == "Churn":
            send = st.sidebar.radio(f"Send Time #{i+1}", ["Noon", "Night"], key=f"send_ch_{i}")
            if send == "Noon":
                rem = st.sidebar.radio(f"Reminder Day #{i+1}", ["Day 4", "Day 5"], key=f"rem_ch_{i}")
                shares = churn_day4 if rem == "Day 4" else churn_day5
            else:
                shares = churn_night_day4
            mapping = churn_map

        else:  # seg_type == "SUNO"
            send, rem, shares, mapping = "Noon", "Day 5", suno_day5, suno_map

        label = st.sidebar.selectbox(f"Select {seg_type} Segment #{i+1}", options=list(mapping.keys()), key=f"seg_{i}")
        idx = mapping[label]

        sz = st.sidebar.number_input(f"Size #{i+1}", min_value=1, value=1000, step=100, key=f"sz_{i}")
        crp = st.sidebar.number_input(
            f"CR #{i+1} (%)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.1,
            format="%.1f",
            key=f"cr_{i}"
        )

        # سهم درصد این سگمنت در هر روز (به صورت اعشاری)
        this_percent = shares[idx]
        percent_sum += this_percent

        # تعداد سفارش روزانه این سگمنت
        this_daily = (this_percent / 100 * (sz * crp / 100))
        total_orders += this_daily

    # میانگین درصد سگمنت‌های انتخاب شده (یک رقم اعشاری)
    percent_avg = (percent_sum / count).round(1)

    # تبدیل تعداد سفارش نهایی به int
    total_orders = total_orders.round(0).astype(int)

    # ساخت DataFrame خروجی با ستون "Share (%)" و "Daily Orders"
    df_mix = pd.DataFrame({
        "Share (%)": percent_avg,
        "Daily Orders": total_orders
    })
    df_mix.index.name = 'Day'

    st.markdown("##### Custom Mix — Total Daily Orders")
    st.table(df_mix)

    csv = df_mix.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name="custom_mix_daily_orders.csv",
        mime="text/csv"
    )
