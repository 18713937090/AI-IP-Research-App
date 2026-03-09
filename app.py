import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# 1. 网页全局配置
st.set_page_config(page_title="AI+IP 调研展示", layout="wide", initial_sidebar_state="collapsed")

# 2. 核心CSS注入：高级渐变背景 + 卡片式UI设计
st.markdown("""
    <style>
    /* 告别纯白：设置温馨且有科技感的全屏渐变背景 */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #f3e7e9 50%, #e3eeff 100%);
    }

    /* 隐藏顶部多余的 Streamlit 默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 卡片式设计：让数据不再干瘪地堆砌在页面上 */
    .glass-card {
        background: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 20px;
    }

    /* 标题与文字颜色优化 */
    h1, h2, h3 {color: #4A4A4A !important; font-family: 'Helvetica Neue', sans-serif;}
    .stMetric label {color: #6c757d !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. 顶部导航栏 (点击跳转模块)
selected = option_menu(
    menu_title=None,
    options=["首页视界", "模块1:链路解码", "模块2:需求洞察", "模块3:受众分层", "模块4:口碑透视"],
    icons=["house-heart", "diagram-3", "bar-chart-line", "people", "chat-quote"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(255,255,255,0.8)", "border-radius": "10px"},
        "icon": {"color": "#FF7F50", "font-size": "18px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#FF7F50"},
    }
)

# ==========================================
# 页面 0: 首页视界 (包含 HTML/CSS 轮播图)
# ==========================================
if selected == "首页视界":
    # 使用纯 HTML/CSS 制作一个炫酷的自动轮播图 (Carousel)
    carousel_html = """
    <style>
    .slider { width: 100%; height: 350px; border-radius: 15px; overflow: hidden; position: relative; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .slides { display: flex; width: 300%; height: 100%; animation: slide 12s infinite; }
    .slide { width: 33.333%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; text-align: center; padding: 20px; }
    /* 三张轮播图的背景色/渐变 */
    .slide1 { background: linear-gradient(120deg, #f6d365 0%, #fda085 100%); }
    .slide2 { background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%); color: #333; }
    .slide3 { background: linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%); color: #333; }

    .slide h1 { font-size: 2.5em; margin-bottom: 10px; text-shadow: 1px 1px 5px rgba(0,0,0,0.2); }
    .slide p { font-size: 1.2em; font-weight: 300; }

    @keyframes slide {
        0% { transform: translateX(0%); }
        25% { transform: translateX(0%); }
        33% { transform: translateX(-33.333%); }
        58% { transform: translateX(-33.333%); }
        66% { transform: translateX(-66.666%); }
        91% { transform: translateX(-66.666%); }
        100% { transform: translateX(0%); }
    }
    </style>
    <div class="slider">
        <div class="slides">
            <div class="slide slide1">
                <h1>AI+IP “共创+陪伴” 模式验证</h1>
                <p>从“符号变现”到“情感共生”，解构Z世代的数字陪伴密码</p>
            </div>
            <div class="slide slide2">
                <h1 style="color:#4A4A4A;">1014份 有效调研样本</h1>
                <p style="color:#4A4A4A;">科学严谨的三角验证法：SEM × K-Means × 演化博弈</p>
            </div>
            <div class="slide slide3">
                <h1 style="color:#4A4A4A;">高达 79.3% 的中介效应</h1>
                <p style="color:#4A4A4A;">情感联结是打破同质化、实现高溢价转化的唯一枢纽</p>
            </div>
        </div>
    </div>
    """
    components.html(carousel_html, height=360)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🏆 大赛项目概览")
    st.write(
        "欢迎来到本项目的可视化数据中心。针对传统IP运营技术适配难、同质化的核心痛点，本研究创新性构建**“技术-行为-情感-消费”**整合分析框架，填补了AI+IP领域情感价值传导机制与长效稳定性的双重实证空白。请通过上方导航栏深入查看四大核心数据模块。")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 页面 1: 链路解码
# ==========================================
elif selected == "模块1:链路解码":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔗 情感如何转化为购买力？")
    st.markdown("💡 **核心发现：** 共创参与是前因，情感联结是桥梁，付费意愿是结果。")

    col1, col2 = st.columns([2, 1])
    with col1:
        fig_sem = go.Figure(data=[go.Sankey(
            node=dict(pad=15, thickness=20, line=dict(color="black", width=0.1),
                      label=["AI感知", "互动共创", "情感感知", "消费行为"],
                      color=["#A1C9F4", "#FFB482", "#FF9F9B", "#8DE5A1"]),
            link=dict(source=[0, 1, 2], target=[1, 2, 3], value=[0.68, 0.71, 0.75],
                      color=["rgba(161, 201, 244, 0.5)", "rgba(255, 180, 130, 0.5)", "rgba(255, 159, 155, 0.8)"])
        )])
        fig_sem.update_layout(height=350, margin=dict(l=0, r=0, t=20, b=0), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_sem, use_container_width=True)
    with col2:
        st.metric(label="情感中介效应占比", value="79.3%", delta="极强正相关")
        st.metric(label="结构方程模型拟合度(RMSEA)", value="0.068", delta="优于0.08标准", delta_color="inverse")
        st.success("实证结论：情感联结承担了近八成的价值转化效能。")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 页面 2: 需求洞察
# ==========================================
elif selected == "模块2:需求洞察":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📊 用户到底在为什么买单？")
    age_group = st.radio("切换受众年龄段查看痛点差异：", ["全体样本", "18岁以下(Z世代)", "31-35岁(职场青年)"],
                         horizontal=True)

    if age_group == "全体样本":
        data_ridit = {'需求维度': ['情感陪伴', '共创参与', '互动体验', '技术性能'], '权重值': [0.62, 0.58, 0.49, 0.38]}
    elif age_group == "18岁以下(Z世代)":
        data_ridit = {'需求维度': ['共创参与', '情感陪伴', '互动体验', '技术性能'], '权重值': [0.61, 0.55, 0.50, 0.40]}
    else:
        data_ridit = {'需求维度': ['情感陪伴', '内容质量', '互动体验', '技术性能'], '权重值': [0.68, 0.55, 0.50, 0.35]}

    fig_ridit = px.bar(pd.DataFrame(data_ridit), x='需求维度', y='权重值', color='权重值',
                       color_continuous_scale='Oranges')
    fig_ridit.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=20))
    st.plotly_chart(fig_ridit, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 页面 3: 受众分层
# ==========================================
elif selected == "模块3:受众分层":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🎯 精准锁定高价值群体")

    col3, col4 = st.columns([1, 1.5])
    with col3:
        st.write("##### 用户画像模拟器")
        sim_age = st.select_slider("年龄段", options=["18岁以下", "19-25岁", "26-30岁", "31-35岁"], value="26-30岁")
        sim_gender = st.radio("性别", ["女", "男"], horizontal=True)
        sim_freq = st.slider("共创频次(次/年)", 0, 10, 4)
    with col4:
        if sim_age == "26-30岁" and sim_gender == "女" and sim_freq >= 3:
            st.error("🔥 AI 判定标签：【情感深度绑定型】 (占38.2%)")
            st.write("核心商业特征：愿意支付20%-30%的情感溢价，**复购率达78.5%**。")
            r_data = [4.8, 4.6, 4.9, 4.8, 4.7]
            color = "rgba(255, 99, 71, 0.7)"
        else:
            st.info("💡 AI 判定标签：【功能体验尝鲜型】 (占45.7%)")
            st.write("核心商业特征：易流失，注重技术性能多于情感联结。")
            r_data = [3.2, 3.0, 3.5, 3.1, 3.0]
            color = "rgba(100, 149, 237, 0.7)"

        fig_radar = go.Figure(
            go.Scatterpolar(r=r_data, theta=['陪伴体验', '情感联结', '共创参与度', '复购倾向', '付费意愿'],
                            fill='toself', fillcolor=color))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, height=300,
                                paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_radar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 页面 4: 口碑透视
# ==========================================
elif selected == "模块4:口碑透视":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("💬 真实反馈与痛点归因")

    col5, col6 = st.columns(2)
    with col5:
        df_pie = pd.DataFrame({'倾向': ['正面(陪伴感强)', '中性', '负面(技术/同质化)'], '占比': [58.7, 26.3, 15.0]})
        fig_pie = px.pie(df_pie, values='占比', names='倾向', hole=0.5,
                         color_discrete_sequence=['#ff9999', '#66b3ff', '#99ff99'])
        fig_pie.update_layout(title="8.7万条文本情感分布", paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=30, b=0))
        st.plotly_chart(fig_pie, use_container_width=True)
    with col6:
        df_pain = pd.DataFrame(
            {'痛点': ['技术适配', '内容同质化', '门槛高', '权益保障'], '占比': [38.2, 29.5, 21.3, 11.0]})
        fig_pain = px.bar(df_pain, x='占比', y='痛点', orientation='h', color='痛点',
                          color_discrete_sequence=px.colors.sequential.Sunset)
        fig_pain.update_layout(title="核心痛点归因拆解", paper_bgcolor="rgba(0,0,0,0)", showlegend=False)
        st.plotly_chart(fig_pain, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)