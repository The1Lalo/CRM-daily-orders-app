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

# --- Vendor segment data (two actions, need to average) ---

# Action 1 percentages for days 1–7 (Noon send)
vendor_action1 = pd.Series(
    [33.84353741, 22.27891156,  9.013605442,  7.908163265,
     8.588435374,  9.523809524,  8.843537415],
    index=[1,2,3,4,5,6,7]
)

# Action 2 percentages for days 1–7 (Noon send)
vendor_action2 = pd.Series(
    [35.65836299, 20.56939502, 13.23843416, 10.46263345,
     10.03558719,  7.402135231,  2.633451957],
    index=[1,2,3,4,5,6,7]
)

# Compute vendor average percentages for Noon
vendor_avg_noon = ((vendor_action1 + vendor_action2) / 2).round(1)

# Vendor percentages for Night send (new values)
vendor_night = pd.Series(
    [20.57649667, 24.12416851, 15.96452328,
     13.52549889, 10.33259424,  8.337028825, 7.139689579],
    index=[1,2,3,4,5,6,7]
).round(1)

# Label maps for NLI/Churn/SUNO
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

# Mode selection (including new "Vendor")
mode = st.sidebar.radio(
    "Mode",
    ("NLI Segments", "Churn Segments", "SUNO Segments", "Vendor", "Custom Mix")
)

# --- NLI Segments ---
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

    # If Night send & segment is "nli1&2ord 90_sd", use custom NLI-night data
    if send_nli_time == "Night" and label == "nli1&2ord 90_sd":
        percent_series = pd.Series([13.3, 18.1, 13.4, 21.5, 13.6, 11.8, 8.3], index=[1,2,3,4,5,6,7])
    else:
        percent_series = shares[idx].round(1)

    daily = (percent_series / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series.map(lambda x: f"{x:.1f}"),
        "Daily Orders": daily
    })
    df_out.index.name = 'Day'

    total = df_out["Daily Orders"].sum()
    header = f"{send_nli_time}" + (f" {rem_nli}" if send_nli_time == "Noon" else "")
    st.markdown(f"##### {label} ({header}) — Total Orders: {total}")
    st.table(df_out)

    csv = df_out.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name=f"nli_{label.replace(' ', '_')}_{header.replace(' ', '_')}.csv",
        mime="text/csv"
    )

# --- Churn Segments ---
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

    percent_series = shares[idx].round(1)
    daily = (percent_series / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series.map(lambda x: f"{x:.1f}"),
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

# --- SUNO Segments ---
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

    percent_series = suno_day5[idx].round(1)
    daily = (percent_series / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series.map(lambda x: f"{x:.1f}"),
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

# --- Vendor Segment (no reminders, can send Noon or Night) ---
elif mode == "Vendor":
    send_vendor_time = st.sidebar.radio("Send Time for Vendor", ("Noon", "Night"), key="send_vendor_time")

    size = st.sidebar.number_input("Vendor Seg Size", min_value=1, value=1000, step=100)
    cr_pct = st.sidebar.number_input(
        "Vendor Seg CR (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.1f"
    )

    # Choose percent_series based on send time:
    if send_vendor_time == "Noon":
        percent_series = vendor_avg_noon.copy()   # previously computed average for Noon
    else:
        percent_series = vendor_night.copy()      # new nighttime percentages

    daily = (percent_series / 100 * size * (cr_pct / 100)).round(0).astype(int)

    df_out = pd.DataFrame({
        "Share (%)": percent_series.map(lambda x: f"{x:.1f}"),
        "Daily Orders": daily
    })
    df_out.index.name = 'Day'

    total = df_out["Daily Orders"].sum()
    st.markdown(f"##### Vendor ({send_vendor_time}) — Total Orders: {total}")
    st.table(df_out)

    csv = df_out.to_csv(index=True, index_label="Day").encode("utf-8")
    st.download_button(
        "Download table as CSV",
        data=csv,
        file_name=f"vendor_{send_vendor_time}.csv",
        mime="text/csv"
    )

# --- Custom Mix (including Vendor) ---
else:
    count = st.sidebar.number_input("How many segment entries?", min_value=1, value=1, step=1)

    total_orders = pd.Series(0.0, index=range(1, 8), name="Total Orders")
    percent_sum = pd.Series(0.0, index=range(1, 8), name="Percent Sum")

    for i in range(count):
        st.sidebar.markdown(f"--- Entry #{i+1} ---")
        seg_type = st.sidebar.selectbox(
            f"Type #{i+1}",
            ["NLI", "Churn", "SUNO", "Vendor"],
            key=f"type_{i}"
        )

        if seg_type == "NLI":
            send = st.sidebar.radio(f"Send Time #{i+1}", ["Noon", "Night"], key=f"send_nli_{i}")
            if send == "Noon":
                rem = st.sidebar.radio(f"Reminder Day #{i+1}", ["Day 4", "Day 5"], key=f"rem_nli_{i}")
                shares = nli_day4 if rem == "Day 4" else nli_day5
            else:
                shares = nli_night_day4

            label = st.sidebar.selectbox(
                f"Select NLI Segment #{i+1}",
                options=list(nli_map.keys()),
                key=f"seg_{i}"
            )
            idx = nli_map[label]

            sz = st.sidebar.number_input(
                f"Size #{i+1}", min_value=1, value=1000, step=100, key=f"sz_{i}"
            )
            crp = st.sidebar.number_input(
                f"CR #{i+1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                key=f"cr_{i}"
            )

            if send == "Night" and label == "nli1&2ord 90_sd":
                this_percent = pd.Series([13.3, 18.1, 13.4, 21.5, 13.6, 11.8, 8.3], index=[1,2,3,4,5,6,7])
            else:
                this_percent = shares[idx].round(1)

        elif seg_type == "Churn":
            send = st.sidebar.radio(f"Send Time #{i+1}", ["Noon", "Night"], key=f"send_ch_{i}")
            if send == "Noon":
                rem = st.sidebar.radio(f"Reminder Day #{i+1}", ["Day 4", "Day 5"], key=f"rem_ch_{i}")
                shares = churn_day4 if rem == "Day 4" else churn_day5
            else:
                shares = churn_night_day4

            label = st.sidebar.selectbox(
                f"Select Churn Segment #{i+1}",
                options=list(churn_map.keys()),
                key=f"seg_{i}"
            )
            idx = churn_map[label]

            sz = st.sidebar.number_input(
                f"Size #{i+1}", min_value=1, value=500, step=50, key=f"sz_{i}"
            )
            crp = st.sidebar.number_input(
                f"CR #{i+1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=2.0,
                step=0.1,
                format="%.1f",
                key=f"cr_{i}"
            )

            this_percent = shares[idx].round(1)

        elif seg_type == "SUNO":
            send, rem, shares, mapping = "Noon", "Day 5", suno_day5, suno_map

            label = st.sidebar.selectbox(
                f"Select SUNO Segment #{i+1}",
                options=list(suno_map.keys()),
                key=f"seg_{i}"
            )
            idx = suno_map[label]

            sz = st.sidebar.number_input(
                f"Size #{i+1}", min_value=1, value=1000, step=100, key=f"sz_{i}"
            )
            crp = st.sidebar.number_input(
                f"CR #{i+1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                key=f"cr_{i}"
            )

            this_percent = shares[idx].round(1)

        else:  # seg_type == "Vendor"
            send_vendor = st.sidebar.radio(f"Send Time #{i+1}", ["Noon", "Night"], key=f"send_vendor_{i}")

            sz = st.sidebar.number_input(
                f"Size #{i+1}", min_value=1, value=1000, step=100, key=f"sz_{i}"
            )
            crp = st.sidebar.number_input(
                f"CR #{i+1} (%)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                key=f"cr_{i}"
            )

            # For Vendor in Custom Mix, choose percent series by send time:
            if send_vendor == "Noon":
                this_percent = vendor_avg_noon.copy()
            else:
                this_percent = vendor_night.copy()

        # Accumulate percent and orders
        percent_sum += this_percent
        total_orders += (this_percent / 100 * (sz * crp / 100))

    # Compute average percent across all entries
    percent_avg = (percent_sum / count).round(1).map(lambda x: f"{x:.1f}")
    total_orders = total_orders.round(0).astype(int)

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
