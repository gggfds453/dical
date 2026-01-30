import streamlit as st

st.title("極度平滑稀釋計算機")
st.write(r"輸入原濃度 $a \times 10^b$ &目標濃度 $d \times 10^e$ 體積 $f$")
st.write("請嚴謹使用科學記號 不要亂輸奇怪數字搞它 ")
st.write("自行注意因次與單位 理論上來說濃度中的體積單位和你要操作的液體體積單位可以不一樣")

col_a, col_b = st.columns(2)
with col_a:
    a = st.number_input("a", value=0.00, step=None)
with col_b:
    b = st.number_input("b", value=0, step=1)

col_d, col_e, col_f = st.columns(3)
with col_d:
    d = st.number_input("d", value=0.00, step=None)
with col_e:
    e = st.number_input("e", value=0, step=1)
with col_f:
    f = st.number_input("f", value=0.0, step=None)

if a > 0 and d > 0 and f > 0:
    cNeed = (10**(e-b)) * d * f / a 
    st.divider()
    st.info(f"原液體積最少要{cNeed:.10f} ")
    
    c = st.number_input("你打算用多少原液", value=0.0, step=None, format="%.g")
    
    if st.button("開算"):
        if c < cNeed:
            st.info(f"巧婦難為無米之炊") 
        else:
            aNow, bNow = a, b
            if aNow < d:
                aNow = aNow * 10
                bNow = bNow - 1            
            step = 1
            r1 = aNow / d
            vAdd = c * ( r1 - 1 )
            vTotalAdd = vAdd
            st.subheader(f"第1步，調整係數")
            st.write(f"稀釋 {r1:.3f} 倍")
            st.info(f"取 {c:.3f} 加 {vAdd:.3f}")
            st.caption(f"目前濃度： ${d} \\times 10^{{{int(bNow)}}}$")
                        
            totalSteps = int(bNow - e)
            if totalSteps > 0:
                for i in range(1, totalSteps + 1):
                    step += 1
                    targetV=  c * ((f/c) ** (i / totalSteps))
                    vTake = targetV / 10
                    vAdd = targetV - vTake
                    vTotalAdd += vAdd
                    st.subheader(f"第{step}步，稀釋10倍")
                    st.info(f"取 {vTake:.3f} 加上 {vAdd:.3f}")
                    st.caption(f"目前體積： ${targetV:.3f}$")
                    st.caption(f"目前濃度： ${d} \\times 10^{{{int(bNow - i)}}}$")
            
            st.subheader(f"結束，共用了{vTotalAdd:.3f}的medium(?)")
            
            st.divider()
            st.subheader("🧪 稀釋操作流程圖")
            
          
            dot = """
            digraph G {
                rankdir=LR;
                node [shape=box, style=filled, color="#E1F5FE", fontname="Arial", fontsize=10];
                edge [fontname="Arial", fontsize=9, color="#546E7A"];
            """
            
        
            dot += f'"{0}" [label="原始液\\n{a} * 10^{int(b)}", color="#CFD8DC"];\n'
            
           
            v_after_step1 = c * r1
            dot += f'"{0}" -> "{1}" [label=" 取 {c:.3f}\\n 加 {vAdd:.3f}"];\n'
            dot += f'"{1}" [label="第 1 步\\n{d} * 10^{int(bNow)}"];\n'
            
           
            if totalSteps > 0:
                for i in range(1, totalSteps + 1):
                    
                    targetV_draw = c * r1 * ((f / (c * r1)) ** (i / totalSteps))
                    vTake_draw = targetV_draw / 10
                    vAdd_draw = targetV_draw - vTake_draw
                    
                   
                    dot += f'"{i}" -> "{i+1}" [label=" 取 {vTake_draw:.3f}\\n 加 {vAdd_draw:.3f}"];\n'
                    dot += f'"{i+1}" [label="第 {i+1} 步\\n{d} * 10^{int(bNow - i)}"];\n'
            
            dot += "}"
            st.graphviz_chart(dot)
          
            

