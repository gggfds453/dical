import streamlit as st

st.title("dilCal")
st.write("輸入原始濃度 $a \\times 10^b$ 體積 $c$，和目標濃度 $d \\times 10^e$ 體積 $f$     自行注意因次")

col1, col2 = st.columns(2)

# 建立左右兩個欄位
col1, col2 = st.columns(2)

# 左邊欄位：輸入原始數據
with col1:
    st.subheader("原始資料")
    # 加入 format="%.g" 可以讓介面更乾淨，並配合 step=None 隱藏按鈕
    a = st.number_input("輸入係數 a", value=0.0, step=None, format="%.g")
    b = st.number_input("輸入冪次 b", value=0, step=None)
    c = st.number_input("輸入體積 c (µL)", value=0.0, step=None, format="%.g")

# 右邊欄位：輸入最終數據
with col2:
    st.subheader("最終目標")
    d = st.number_input("輸入係數 d", value=0.0, step=None, format="%.g")
    e = st.number_input("輸入冪次 e", value=0, step=None)
    f = st.number_input("輸入體積 f (µL)", value=0.0, step=None, format="%.g")




