import streamlit as st

st.title("dilCal")
st.write(r"請輸入原始濃度 $a \times 10^b$ 與目標需求 $d \times 10^e$ 體積 $f$")

col_a, col_b = st.columns(2)
with col_a:
    a = st.number_input("輸入原始係數 a", value=0.0, step=None, format="%.g")
with col_b:
    b = st.number_input("輸入原始冪次 b", value=0.0, step=None, format="%.g")

col_d, col_e, col_f = st.columns(3)
with col_d:
    d = st.number_input("輸入目標係數 d", value=0.0, step=None, format="%.g")
with col_e:
    e = st.number_input("輸入目標冪次 e", value=0.0, step=None, format="%.g")
with col_f:
    f = st.number_input("輸入目標體積 f", value=0.0, step=None, format="%.g")

if a > 0 and d > 0 and f > 0:
    required_c = (d * f * (10**e)) / (a * (10**b))
    st.divider()
    st.warning(f"根據目標，你最少需要準備 {required_c:.4f} 的原始液體 c")
    
    c = st.number_input("請確認並輸入你擁有的原始體積 c", value=0.0, step=None, format="%.g")
    
    if st.button("開始計算步驟"):
        if c < required_c:
            st.error(f"量不夠！輸入體積 {c} 低於門檻 {required_c:.4f}")
        else:
            curr_a, curr_b = a, b
            if curr_a < d:
                curr_a = curr_a * 10
                curr_b = curr_b - 1
                
            step = 1
            R1 = curr_a / d
            st.subheader(f"步驟 {step}")
            st.write(f"稀釋 {R1:.2f} 倍")
            st.info(f"操作：取 1 加上 {R1 - 1:.2f}")
            st.caption(f"當前濃度: {d} * 10^{int(curr_b)}")
            
            while curr_b > e:
                step += 1
                curr_b -= 1
                st.subheader(f"步驟 {step}")
                st.write("稀釋 10.00 倍")
                st.info("操作：取 1 加上 9.00")
                st.caption(f"當前濃度: {d} * 10^{int(curr_b)}")
            
            st.success("計算完成")
            st.balloons()
