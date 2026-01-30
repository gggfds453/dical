import streamlit as st

st.title("dilCal")
st.write(r"請輸入原始濃度 $a \times 10^b$ 與目標需求 $d \times 10^e$ 體積 $f$")

# 第一排：原始濃度係數與冪次
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("輸入原始係數 a", value=0.0, step=None, format="%.g")
    b = st.number_input("輸入原始冪次 b", value=0.0, step=None, format="%.g")

# 第二排：目標濃度與體積
col3, col4, col5 = st.columns(3)
with col3:
    d = st.number_input("輸入目標係數 d", value=0.0, step=None, format="%.g")
with col4:
    e = st.number_input("輸入目標冪次 e", value=0.0, step=None, format="%.g")
with col5:
    f = st.number_input("輸入目標體積 f", value=0.0, step=None, format="%.g")

# 邏輯判斷：當基本參數都填好時
if a > 0 and d > 0 and f > 0:
    required_c = (d * f * (10**e)) / (a * (10**b))
    
    st.divider()
    st.warning(f"根據目標，你最少需要準備 {required_c:.4f} 的原始液體 c")
    
    # 這時才顯示 c 的輸入框
    c = st.number_input("請確認並輸入你擁有的原始體積 c", value=0.0, step=None, format="%.g")
    
    if st.button("開始計算步驟"):
        if c < required_c:
            st.error(f"輸入體積 {c} 仍不足以配製目標總量，請增加體積 c")
        else:
            # 開始稀釋邏輯
            step = 1
            # 這裡我們用臨時變數運算，避免改到輸入框顯示
            curr_a, curr_b = a, b
            
            if curr_a < d:
                curr_a = curr_a * 10
                curr_b = curr_b - 1
                
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
            
            st.success("計算完成！")
            st.balloons()
