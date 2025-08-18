import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
st.set_page_config(
    page_title="開發人員｜Tasksnap",
    page_icon="👥",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes shimmer {
        0% { background-position: -200px 0; }
        100% { background-position: calc(200px + 100%) 0; }
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 54px;
        color: #003366;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 8px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #234;
        margin-bottom: 36px;
        margin-top: 8px;
        font-weight: 500;
        letter-spacing: 1.5px;
    }
    .member {
        text-align: center;
        margin-bottom: 60px;
        border-radius: 25px;
        padding: 40px 20px 30px 20px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        overflow: hidden;
    }
    .member::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        transform: rotate(45deg);
        transition: all 0.6s ease;
        opacity: 0;
    }
    .member:hover::before {
        opacity: 1;
        animation: rotate 2s linear infinite;
    }
    .member:nth-child(1) {
        background: linear-gradient(135deg, #ffffff, #f8fafe, #f5f9ff);
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(0,85,165,0.05);
    }
    .member:nth-child(1)::before {
        background: linear-gradient(45deg, transparent, rgba(0,85,165,0.1), transparent);
    }
    .member:nth-child(1):hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 25px 60px rgba(0,0,0,0.12), 0 10px 25px rgba(0,85,165,0.15), 0 0 30px rgba(0,85,165,0.1);
        border-color: #7ba7d9;
    }
    .member:nth-child(2) {
        background: linear-gradient(135deg, #ffffff, #fffcf8, #fef9f0);
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(255,153,0,0.05);
    }
    .member:nth-child(2)::before {
        background: linear-gradient(45deg, transparent, rgba(255,153,0,0.1), transparent);
    }
    .member:nth-child(2):hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 25px 60px rgba(0,0,0,0.12), 0 10px 25px rgba(255,153,0,0.15), 0 0 30px rgba(255,153,0,0.1);
        border-color: #ffb366;
    }
    .member:nth-child(3) {
        background: linear-gradient(135deg, #ffffff, #f8fef8, #f5fcf5);
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(76,175,80,0.05);
    }
    .member:nth-child(3)::before {
        background: linear-gradient(45deg, transparent, rgba(76,175,80,0.1), transparent);
    }
    .member:nth-child(3):hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 25px 60px rgba(0,0,0,0.12), 0 10px 25px rgba(76,175,80,0.15), 0 0 30px rgba(76,175,80,0.1);
        border-color: #81c784;
    }
    .member:nth-child(4) {
        background: linear-gradient(135deg, #ffffff, #fef8fb, #fdf5f8);
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(233,30,99,0.05);
    }
    .member:nth-child(4)::before {
        background: linear-gradient(45deg, transparent, rgba(233,30,99,0.1), transparent);
    }
    .member:nth-child(4):hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 25px 60px rgba(0,0,0,0.12), 0 10px 25px rgba(233,30,99,0.15), 0 0 30px rgba(233,30,99,0.1);
        border-color: #f06292;
    }
    .member img {
        border-radius: 50%;
        width: 160px;
        height: 160px;
        object-fit: cover;
        border: 5px solid transparent;
        background: linear-gradient(45deg, #0055A5, #FF9900) border-box;
        background-clip: border-box;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15), 0 0 20px rgba(0,85,165,0.3);
        transition: all 0.4s ease;
        position: relative;
        z-index: 2;
    }
    .member:hover img {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2), 0 0 30px rgba(255,153,0,0.4);
        border-color: #FF9900;
    }
    .member-name {
        font-size: 22px;
        margin-top: 8px;
        font-weight: bold;
        color: #003366;
        letter-spacing: 1.5px;
    }
    .member-role {
        font-size: 16px;
        color: #0055A5;
        margin-bottom: 14px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .portfolio-button {
        background: linear-gradient(45deg, #FF9900, #FF6600);
        color: white;
        padding: 12px 28px;
        border: none;
        border-radius: 25px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 20px rgba(255,153,0,0.3), 0 3px 10px rgba(0,0,0,0.1);
        display: inline-block;
        margin-top: 15px;
        position: relative;
        overflow: hidden;
        z-index: 2;
    }
    .portfolio-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.6s;
    }
    .portfolio-button:hover {
        color: #fff;
        text-decoration: none;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 30px rgba(255,153,0,0.4), 0 5px 15px rgba(0,0,0,0.15);
    }
    .portfolio-button:hover::before {
        left: 100%;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 40px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# 標題
# ---------------------
st.markdown("<div class='main-title'>👥 開發人員</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>我們的團隊來自不同領域，致力於打造最值得信賴的接案平台</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------
# 成員卡片
# ---------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="member">
        <img src="https://th.wallhaven.cc/small/96/96r551.jpg" alt="Gary">
        <div class="member-name">Gary</div>
        <div class="member-role">創辦人 / 總企劃</div>
        <a href="https://yourportfolio2.com" target="_blank" class="portfolio-button">前往作品集</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="member">
        <img src="https://images.unsplash.com/photo-1559190394-df5a28aab5c5?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NjB8fHBldHxlbnwwfHwwfHx8MA%3D%3D" alt="Jim">
        <div class="member-name">Jim</div>
        <div class="member-role">開發助理</div>
        <a href="https://yourportfolio2.com" target="_blank" class="portfolio-button">前往作品集</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="member">
        <img src="https://images.unsplash.com/photo-1482434368596-fbd06cae4f89?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fHBldHxlbnwwfHwwfHx8MA%3D%3D" alt="Hawer">
        <div class="member-name">Hawer</div>
        <div class="member-role">開發助理</div>
        <a href="https://yourportfolio3.com" target="_blank" class="portfolio-button">前往作品集</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="member">
        <img src="https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fHBldHxlbnwwfHwwfHx8MA%3D%3D" alt="Zhou">
        <div class="member-name">Zhou</div>
        <div class="member-role">文書處理</div>
        <a href="https://yourportfolio4.com" target="_blank" class="portfolio-button">前往作品集</a>
    </div>
    """, unsafe_allow_html=True)

# ---------------------
# 團隊技能區塊
# ---------------------
st.markdown("<div style='text-align:center; margin-top:48px; margin-bottom:36px;'><h3>🛠️ 團隊技能</h3></div>", unsafe_allow_html=True)
skill1, skill2, skill3 = st.columns(3)
with skill1:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #f0f8ff); padding:25px; border-radius:20px; box-shadow:0 12px 35px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#0055A5; margin-bottom:15px; text-align:center;">💻 前端技術</h4>
        <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
            <span style="background:#e3f2fd; color:#0055A5; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Python Streamlit</span>
            <span style="background:#e3f2fd; color:#0055A5; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Javascript</span>
            <span style="background:#e3f2fd; color:#0055A5; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Html</span>
            <span style="background:#e3f2fd; color:#0055A5; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">CSS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with skill2:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #fff8f0); padding:25px; border-radius:20px; box-shadow:0 12px 35px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#FF9900; margin-bottom:15px; text-align:center;">⚙️ 後端技術</h4>
        <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
            <span style="background:#fff3e0; color:#FF9900; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Python</span>
            <span style="background:#fff3e0; color:#FF9900; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Node.js</span>
            <span style="background:#fff3e0; color:#FF9900; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Firebase</span>
            <span style="background:#fff3e0; color:#FF9900; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">MongoDB</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with skill3:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #f0fff0); padding:25px; border-radius:20px; box-shadow:0 12px 35px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#4CAF50; margin-bottom:15px; text-align:center;">🎨 設計工具</h4>
        <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
            <span style="background:#e8f5e8; color:#4CAF50; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Figma</span>
            <span style="background:#e8f5e8; color:#4CAF50; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Adobe illustrator</span>
            <span style="background:#e8f5e8; color:#4CAF50; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Microsoft Designer</span>
            <span style="background:#e8f5e8; color:#4CAF50; padding:5px 12px; border-radius:15px; font-size:12px; font-weight:600;">Photoshop</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------
# 頁尾
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | 開發團隊</div>",
    unsafe_allow_html=True
)
