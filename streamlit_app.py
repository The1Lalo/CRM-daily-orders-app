# app.py
import streamlit as st
import pandas as pd

# --- Historical share data ---
# NLI shares for reminder scenarios
nli_day4 = pd.DataFrame({
    1: [21.711684,16.118861,15.034289,16.583282,12.209929,9.912489,8.429466],
    2: [21.213604,15.335324,11.963968,18.106597,12.785003,10.154376,10.441128],
    3: [20.610673,14.943540,11.409406,20.422512,13.551898,10.061606,9.000365],
    4: [20.827834,14.786823,11.563077,19.189448,13.577198,10.934636,9.120985],
    5: [20.628490,10.088083,11.353579,20.676401,15.158034,12.881254,9.214158],
}, index=[1,2,3,4,5,6,7])
nli_day4.index.name='Day'

nli_day5 = pd.DataFrame({
    2: [24.265389,14.380861,9.495267,9.269872,18.347022,15.460416,8.781174],
    3: [22.910380,14.013488,9.750170,8.227991,18.392384,17.221041,9.484546],
    4: [23.826975,14.149628,9.696535,8.299591,19.013721,16.241660,8.771890],
}, index=[1,2,3,4,5,6,7])
nli_day5.index.name='Day'
avg_nli=nli_day5.mean(axis=1)
nli_day5[1]=avg_nli; nli_day5[5]=avg_nli
nli_day5=nli_day5[[1,2,3,4,5]]

# Churn shares for reminder scenarios (noon)
churn_day4=pd.DataFrame({
    1:[20.284210,16.364614,12.778718,18.437817,12.517431,11.110729,8.506481],
    2:[20.587293,15.803377,11.659074,19.384095,13.959417,11.957428,6.649317],
    3:[20.250918,11.259850,10.081655,19.287457,14.421064,14.493234,10.205822],
}, index=[1,2,3,4,5,6,7])
churn_day4.index.name='Day'

churn_day5=pd.DataFrame({
    1:[25.227468,15.982380,11.053946,8.574631,15.792417,15.887211,7.481948],
    2:[21.839262,15.252314,13.406240,13.175335,17.053160,12.539152,6.734537],
    3:[23.851160,12.611638,13.306372,10.842209,16.645724,15.215174,7.527723],
}, index=[1,2,3,4,5,6,7])
churn_day5.index.name='Day'

# Churn shares for night send scenario (reminder Day 4)
churn_night_day4=pd.DataFrame({
    1:[12.444968,19.761227,11.236781,23.485016,13.685019,10.855740,8.531249],
    2:[11.317538,22.526437,13.398942,20.103059,13.705939,11.167455,7.780631],
    3:[14.508197,20.901639,13.442623,19.918033,8.852459,13.114754,9.262295],
}, index=[1,2,3,4,5,6,7])
churn_night_day4.index.name='Day'

# SUNO shares for reminder Day 5
suno_day5=pd.DataFrame({
    1:[26.925197,13.303347,9.895528,6.161128,22.352256,13.337876,8.024668],
    2:[25.177297,12.389750,9.354067,6.076514,22.598724,14.089013,10.314636],
    3:[25.482682,10.398605,8.001933,6.041134,25.664506,14.709364,9.701776],
    4:[23.970033,10.544025,7.250834,6.004116,25.754893,15.729818,10.746282],
    5:[23.914282,11.726879,8.608781,6.270109,24.791565,14.105966,10.582418],
    6:[23.498621,11.911483,7.084567,6.475340,25.688482,14.275750,11.065757],
}, index=[1,2,3,4,5,6,7])
suno_day5.index.name='Day'

# Label maps
nli_map={"nli_1&2Ord 1-14":1,"nli_1&2 ord 15_28":2,"nli1&2ord 29_60":3,"nli1&2ord 61_90":4,"nli1&2ord 90_sd":5}
churn_map={"churn 29_60":1,"churn 61_90":2,"churn 91_startdate":3}
suno_map={"suno 3-7":1,"suno 8-14":2,"suno 15-28":3,"suno 29-63":4,"suno 64-91":5,"suno 92-sd":6}

# Page config
st.set_page_config(page_title="Daily Orders Calculator", layout="wide")
st.header("🎯 Daily Orders Calculator")

# Main mode selection
mode=st.sidebar.radio("Mode",("NLI Segments","Churn Segments","SUNO Segments","Custom Mix"))

# Helper to download table only
def download_table(df,filename):
    csv=df.to_csv(index=True,index_label="Day").encode('utf-8')
    st.download_button("Download table as CSV",data=csv,file_name=filename,mime="text/csv")

# NLI Segments
if mode=="NLI Segments":
    st.subheader("📊 NLI Daily Orders")
    rem_nli=st.sidebar.radio("Reminder Day for NLI",("Day 4","Day 5"),key="rem_nli_main")
    shares=nli_day4 if rem_nli=="Day 4" else nli_day5
    label=st.sidebar.selectbox("انتخاب Segment",options=list(nli_map.keys()))
    idx=nli_map[label]
    size=st.sidebar.number_input("Seg Size",min_value=1,value=1000,step=100)
    cr_pct=st.sidebar.slider("Seg CR",0.0,100.0,5.0,0.5,format="%.1f%%")
    daily=(shares[idx]/100*size*(cr_pct/100)).round(2).to_frame("Daily Orders")
    total=int(daily["Daily Orders"].sum())
    st.markdown(f"#### {label} ({rem_nli}) — Total Orders: {total}")
    st.table(daily)
    download_table(daily,f"nli_{label.replace(' ','_')}_{rem_nli}.csv")
    st.bar_chart(daily)

# Churn Segments
elif mode=="Churn Segments":
    st.subheader("📊 Churn Daily Orders")
    send_time=st.sidebar.radio("Send Time for Churn",("Noon","Night"),key="send_ch_time")
    if send_time=="Noon":
        rem_ch=st.sidebar.radio("Reminder Day for Churn",("Day 4","Day 5"),key="rem_ch_main")
        shares=churn_day4 if rem_ch=="Day 4" else churn_day5
    else:
        shares=churn_night_day4
        rem_ch="Night"
    label=st.sidebar.selectbox("انتخاب Churn Segment",options=list(churn_map.keys()))
    idx=churn_map[label]
    size=st.sidebar.number_input("Seg Size",min_value=1,value=500,step=50)
    cr_pct=st.sidebar.slider("Seg CR",0.0,100.0,2.0,0.5,format="%.1f%%")
    daily=(shares[idx]/100*size*(cr_pct/100)).round(2).to_frame("Daily Orders")
    total=int(daily["Daily Orders"].sum())
    st.markdown(f"#### {label} ({send_time}{(' '+rem_ch) if send_time=='Noon' else ''}) — Total Orders: {total}")
    st.table(daily)
    download_table(daily,f"churn_{label.replace(' ','_')}_{send_time}_{rem_ch}.csv")
    st.line_chart(daily)

# SUNO Segments
elif mode=="SUNO Segments":
    st.subheader("📊 SUNO Daily Orders")
    label=st.sidebar.selectbox("انتخاب SUNO Segment",options=list(suno_map.keys()))
    idx=suno_map[label]
    size=st.sidebar.number_input("Seg Size",min_value=1,value=1000,step=100)
    cr_pct=st.sidebar.slider("Seg CR",0.0,100.0,5.0,0.5,format="%.1f%%")
    daily=(suno_day5[idx]/100*size*(cr_pct/100)).round(2).to_frame("Daily Orders")
    total=int(daily["Daily Orders"].sum())
    st.markdown(f"#### {label} (Day 5) — Total Orders: {total}")
    st.table(daily)
    download_table(daily,f"suno_{label.replace(' ','_')}_Day5.csv")
    st.bar_chart(daily)

# Custom Mix
else:
    st.subheader("🧩 Custom Mix Daily Orders")
    rem_nli_c=st.sidebar.radio("Reminder Day for NLI",("Day 4","Day 5"),key="rem_nli_c")
    send_ch_c=st.sidebar.radio("Send Time for Churn",("Noon","Night"),key="send_ch_c")
    if send_ch_c=="Noon":
        rem_ch_c=st.sidebar.radio("Reminder Day for Churn",("Day 4","Day 5"),key="rem_ch_c")
        shares_ch=nli_day4 if rem_ch_c=="Day 4" else nli_day5
    else:
        shares_ch=churn_night_day4
        rem_ch_c="Night"
    shares_nli=nli_day4 if rem_nli_c=="Day 4" else nli_day5
    shares_suno=suno_day5
    count=st.sidebar.number_input("How many segment entries?",min_value=1,value=1,step=1)
    total_df=pd.Series(0.0,index=range(1,8),name="Total Orders")
    for i in range(count):
        st.sidebar.markdown(f"--- Entry #{i+1} ---")
        seg_type=st.sidebar.selectbox(f"Type #{i+1}",["NLI","Churn","SUNO"],key=f"type_{i}")
        if seg_type=="NLI":options,shares,mapping=list(nli_map.keys()),shares_nli,nli_map
        elif seg_type=="Churn":options,shares,mapping=list(churn_map.keys()),shares_ch,churn_map
        else:options,shares,mapping=list(suno_map.keys()),shares_suno,suno_map
        lbl=st.sidebar.selectbox(f"Select {seg_type} Segment #{i+1}",options=options,key=f"seg_{i}")
        idx=mapping[lbl]
        sz=st.sidebar.number_input(f"Size #{i+1}",min_value=1,value=1000,step=100,key=f"sz_{i}")
        crp=st.sidebar.slider(f"CR #{i+1}",0.0,100.0,5.0,0.5,format="%.1f%%",key=f"cr_{i}")
        total_df+=shares[idx]/100*(sz*(crp/100))
    df_mix=total_df.round(2).to_frame()
    st.markdown("#### Custom Mix — Total Daily Orders")
    st.table(df_mix)
    download_table(df_mix,"custom_mix_daily_orders.csv")
    st.bar_chart(df_mix)

st.caption("Built with ❤️ using Streamlit")
