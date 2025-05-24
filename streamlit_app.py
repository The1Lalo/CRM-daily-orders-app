# app.py
import streamlit as st
import pandas as pd

# --- داده‌های تاریخی ---
# NLI shares
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
avg_nli = nli_day5.mean(axis=1)
nli_day5[1] = avg_nli
nli_day5[5] = avg_nli
nli_day5 = nli_day5[[1,2,3,4,5]]

# Churn shares
day4 = pd.DataFrame({1:[20.284210,16.364614,12.778718,18.437817,12.517431,11.110729,8.506481],
                       2:[20.587293,15.803377,11.659074,19.384095,13.959417,11.957428,6.649317],
                       3:[20.250918,11.259850,10.081655,19.287457,14.421064,14.493234,10.205822]},
                      index=[1,2,3,4,5,6,7])
day4.index.name='Day'

churn_day5 = pd.DataFrame({1:[25.227468,15.982380,11.053946,8.574631,15.792417,15.887211,7.481948],
                           2:[21.839262,15.252314,13.406240,13.175335,17.053160,12.539152,6.734537],
                           3:[23.851160,12.611638,13.306372,10.842209,16.645724,15.215174,7.527723]},
                          index=[1,2,3,4,5,6,7])
churn_day5.index.name='Day'

# Label maps
nli_map={"nli_1&2Ord 1-14":1,"nli_1&2 ord 15_28":2,
         "nli1&2ord 29_60":3,"nli1&2ord 61_90":4,"nli1&2ord 90_sd":5}
churn_map={"churn 29_60":1,"churn 61_90":2,"churn 91_startdate":3}

# Page config
st.set_page_config(page_title="Daily Orders Calculator",layout="wide")
st.title("🎯 Daily Orders Calculator")

# Mode selection
mode=st.sidebar.radio("Mode",("NLI Segments","Churn Groups","Custom Mix"))

# NLI Segments
if mode=="NLI Segments":
    st.header("📊 NLI Daily Orders")
    rem=st.sidebar.radio("Reminder Day for NLI",("Day 4","Day 5"),key="rem_nli_main")
    shares=nli_day4 if rem=="Day 4" else nli_day5
    seg_lbl=st.sidebar.selectbox("انتخاب Segment",options=list(nli_map.keys()))
    seg=nli_map[seg_lbl]
    size=st.sidebar.number_input("Seg Size",min_value=1,value=1000,step=100)
    cr_pct=st.sidebar.slider("Seg CR",0.0,100.0,5.0,0.5,format="%.1f%%")
    total=size*(cr_pct/100)
    daily=(shares[seg]/100*total).round(2)
    st.subheader(f"{seg_lbl} ({rem}) — Total Orders: {int(total)}")
    st.table(daily.to_frame("Daily Orders"))
    st.bar_chart(daily)

# Churn Groups
elif mode=="Churn Groups":
    st.header("📊 Churn Daily Orders")
    rem=st.sidebar.radio("Reminder Day for Churn",("Day 4","Day 5"),key="rem_ch_main")
    shares=day4 if rem=="Day 4" else churn_day5
    lbl=st.sidebar.selectbox("انتخاب Churn Group",options=list(churn_map.keys()))
    idx=churn_map[lbl]
    size=st.sidebar.number_input("Seg Size",min_value=1,value=500,step=50)
    cr_pct=st.sidebar.slider("Seg CR",0.0,100.0,2.0,0.5,format="%.1f%%")
    total=size*(cr_pct/100)
    daily=(shares[idx]/100*total).round(2)
    st.subheader(f"{lbl} ({rem}) — Total Orders: {int(total)}")
    st.table(daily.to_frame("Daily Orders"))
    st.line_chart(daily)

# Custom Mix: sequential entries
else:
    st.header("🧩 Custom Mix Daily Orders")
    # Reminder settings\    rem_nli=st.sidebar.radio("Reminder Day for NLI",("Day 4","Day 5"),key="rem_nli_c")
    rem_ch=st.sidebar.radio("Reminder Day for Churn",("Day 4","Day 5"),key="rem_ch_c")
    shares_nli=nli_day4 if rem_nli=="Day 4" else nli_day5
    shares_ch=day4 if rem_ch=="Day 4" else churn_day5
    # number of entries\    count=st.sidebar.number_input("How many segments to add?",min_value=1,value=1,step=1)
    total_df=pd.Series(0.0,index=range(1,8),name="Total Orders")
    for i in range(count):
        st.sidebar.markdown(f"--- Segment Entry #{i+1} ---")
        type_i=st.sidebar.selectbox(f"Type #{i+1}",["NLI","Churn"],key=f"type_{i}")
        if type_i=="NLI":
            lbl=st.sidebar.selectbox(f"Select NLI Segment #{i+1}",options=list(nli_map.keys()),key=f"seg_{i}")
            idx=nli_map[lbl]
            shares=shares_nli
        else:
            lbl=st.sidebar.selectbox(f"Select Churn Group #{i+1}",options=list(churn_map.keys()),key=f"seg_{i}")
            idx=churn_map[lbl]
            shares=shares_ch
        sz=st.sidebar.number_input(f"Seg Size #{i+1}",min_value=1,value=1000,step=100,key=f"sz_{i}")
        crp=st.sidebar.slider(f"Seg CR #{i+1}",0.0,100.0,5.0,0.5,format="%.1f%%",key=f"cr_{i}")
        total_df+=shares[idx]/100*(sz*(crp/100))
    df_mix=total_df.round(2).to_frame()
    st.subheader("Custom Mix — Total Daily Orders")
    st.table(df_mix)
    st.bar_chart(df_mix)

st.caption("Built with ❤️ using Streamlit")
