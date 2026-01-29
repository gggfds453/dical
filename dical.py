import streamlit as st

st.title("dilCal")
st.write("輸入原始濃度 $a \\times 10^b$ 體積 $c$，和目標濃度 $d \\times 10^e$ 體積 $f$")

col1, col2 = st.columns(2)

with col1:
    st.subheader("原始資料")
    a = st.number_input("輸入係數 a", value=0.0, step=1)
    b = st.number_input("輸入冪次 b", value=0, step=1)
    c = st.number_input("輸入體積 c (µL)", value=0.0, step=1)

with col2:
    st.subheader("最終目標")
    d = st.number_input("輸入係數 d", value=0.0, step=1)
    e = st.number_input("輸入冪次 e", value=0, step=1)
    f = st.number_input("輸入體積 f (µL)", value=0.0, step=1)






