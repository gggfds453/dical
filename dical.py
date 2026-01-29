import streamlit as st

st.title("dilCal")
st.write("輸入原始濃度 $a \\times 10^b$ 體積 $c$，和目標濃度 $d \\times 10^e$ 體積 $f$     自行注意因次")

col1, col2 = st.columns(2)

with col1:
    st.subheader("原始資料")
    a = st.number_input("輸入係數 a", value=1.0, step=0.1)
    b = st.number_input("輸入冪次 b", value=9, step=1)
    c = st.number_input("輸入體積 c (µL)", value=100.0, step=1.0)

with col2:
    st.subheader("最終目標")
    d = st.number_input("輸入係數 d", value=1.0, step=0.1)
    e = st.number_input("輸入冪次 e", value=3, step=1)
    f = st.number_input("輸入體積 f (µL)", value=1000.0, step=1.0)



