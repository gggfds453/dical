import streamlit as st

st.title("dilCal")
st.write(r"輸入原濃度 $a \times 10^b$ &目標濃度 $d \times 10^e$ 體積 $f$")
st.write("請嚴謹使用科學記號 不要亂輸奇怪數字搞它 ")
st.write("自行注意因次與單位 理論上來說濃度中的體積單位和你要操作的液體體積單位可以不一樣")

col_a, col_b = st.columns(2)
with col_a:
    a = st.number_input("a", value=0.0, step=None)
with col_b:
    b = st.number_input("b", value=0.0, step=None)

col_d, col_e, col_f = st.columns(3)
with col_d:
    d = st.number_input("d", value=0.0, step=None)
with col_e:
    e = st.number_input("e", value=0.0, step=None)
with col_f:
    f = st.number_input("f", value=0.0, step=None)

if a > 0 and d > 0 and f > 0:
    required_c = (d * f * (10**e)) / (a * (10**b))
    st.divider()
    st.warning(f"根據目標，你最少需要準備 {required_c:.4f} 的原始液體 c")
    
    c = st.number_input("請確認並輸入你擁有的原始體積 c", value=0.0, step=None, format="%.g")
    
    if st.button("開始計算步驟"):
        if c < required_c:
            st.error(f"量不夠！")
        else:
            curr_a, curr_b = a, b
            if curr_a < d:
                curr_a = curr_a * 10
                curr_b = curr_b - 1
            
            # 第一步：調整係數
            step = 1
            r1 = curr_a / d
            v_add1 = c * (-1 + r1)
            st.subheader(f"步驟 {step} (調整係數)")
            st.write(f"稀釋 {r1:.2f} 倍")
            st.info(f"操作：取 {c:.2f} 加上 {v_add1:.2f}")
            st.caption(f"當前濃度: {d} * 10^{int(curr_b)}")
            
            # 剩餘平滑稀釋邏輯
            total_steps = int(curr_b - e)
            if total_steps > 0:
                for i in range(1, total_steps + 1):
                    step += 1
                    # 公式：f/c 的 (i/total_steps) 次方 
                    # 這裡的目的是計算每一階段的「目標總體積」
                    target_v = c * ((f/c) ** (i / total_steps))
                    
                    # 每一階段固定稀釋 10 倍 (因為冪次每次降 1)
                    # 為了達成 target_v，我們計算需要取多少前一階的液體
                    v_take = target_v / 10
                    v_add = target_v - v_take
                    
                    st.subheader(f"步驟 {step}")
                    st.write("稀釋 10.00 倍")
                    st.info(f"操作：取 {v_take:.2f} 加上 {v_add:.2f}")
                    st.caption(f"當前體積：{target_v:.2f} | 當前濃度: {d} * 10^{int(curr_b - i)}")
            
            st.success(f"計算完成，最後一步體積剛好為 {f}")




