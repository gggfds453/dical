import streamlit as st

st.title("序列稀釋計算機",'/',a)
a = st.number_input("原始係數 a", value=1.5)
N = st.number_input("原始冪次 N", value=9)
b = st.number_input("目標係數 b", value=2.0)
K = st.number_input("目標冪次 K", value=3)

initial_conc = a * (10**N)
target_conc = b * (10**K)

if st.button("計算稀釋步驟"):
    current = initial_conc
    step = 1
    while current > target_conc:
        ratio = min(10.0, current / target_conc)
        current /= ratio
        st.write(f"步驟 {step}: 稀釋 {ratio:.2f} 倍 -> 當前濃度: {current:.2e}")

        step += 1
