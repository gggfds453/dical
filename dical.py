import streamlit as st

st.title("dilCal")
st.write("輸入原始濃度 $a \\times 10^b$ 體積 $c$&目標濃度 $d \\times 10^e$ 體積 $f$")
st.write("自行注意因次單位一致 然後不要輸一些奇怪數字搞它")

col1, col2 = st.columns(2)

with col1:
    st.subheader("原始資料")
    a = st.number_input("輸入係數 a", value=0.0, step=None)
    b = st.number_input("輸入冪次 b", value=0, step=None)
    c = st.number_input("輸入體積 c", value=0.0, step=None)

with col2:
    st.subheader("最終目標")
    d = st.number_input("輸入係數 d", value=0.0, step=None)
    e = st.number_input("輸入冪次 e", value=0, step=None)
    f = st.number_input("輸入體積 f", value=0.0, step=None)
    
if st.button("開始計算步驟"):
    if a > 0 and c > 0 and d > 0 and f > 0:
        if a < d :
            a = a * 10
            b = b-1

        step=1
        R=a/d
        st.subheader(f"步驟 {step}")
        st.write(f"稀釋 {R:.2f} 倍")
        st.info(f"操作：取 1 加 {R - 1:.2f}")
        st.caption(f"當前濃度: {d} * 10^{int(b)}")
        while b > e:
            step += 1
            b -= 1
            st.subheader(f"步驟 {step}")
            st.write("稀釋 10 倍")
            st.info("操作：取 1 加上 9")
            st.caption(f"當前濃度: {d} * 10^{int(b)}")
        
else:
        st.warning("數字怪怪的")
    
















