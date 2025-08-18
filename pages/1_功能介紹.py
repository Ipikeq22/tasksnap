import streamlit as st

# ---------------------
# 頁面設定
# ---------------------
st.set_page_config(
    page_title="功能介紹｜Tasksnap",
    page_icon="🛠️",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    @keyframes glow {
        0% { box-shadow: 0 0 10px rgba(0,85,165,0.2); }
        50% { box-shadow: 0 0 25px rgba(0,85,165,0.4), 0 0 35px rgba(255,153,0,0.2); }
        100% { box-shadow: 0 0 10px rgba(0,85,165,0.2); }
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .center-title {
        text-align: center;
        color: #003366;
        font-size: 52px;
        font-weight: 900;
        letter-spacing: 3px;
        margin-bottom: 18px;
        margin-top: 18px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.10);
    }
    .feature-title {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        color: #0055A5;
        margin-bottom: 12px;
        margin-top: 38px;
        letter-spacing: 2px;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .center-section {
        text-align: center;
        font-size: 24px;
        color: #234;
        margin-bottom: 40px;
        margin-top: 20px;
        font-weight: 500;
        line-height: 1.9;
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08), 0 3px 10px rgba(0,85,165,0.1);
        border-left: 5px solid #FF9900;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    .center-img-caption {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 8px;
        width: 100%;
        max-width: 95vw;   /* 改成相對螢幕寬度，響應式 */
    }

    @media (max-width: 600px) {
        .center-img-caption {
            max-width: 100vw; /* 小螢幕時圖片最大寬度跟螢幕一樣 */
            padding: 0 4vw;
        }
        .center-img-caption img {
            max-width: 100%;
            width: 100%;
        }
    }
    .center-img-caption img {
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15), 0 5px 15px rgba(0,85,165,0.2);
        margin-bottom: 12px;
        max-width: 100%;
        width: 100%;
        height: auto;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 3px solid transparent;
        background-clip: padding-box;
    }
    .center-img-caption img:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 25px 60px rgba(0,0,0,0.2), 0 10px 25px rgba(0,85,165,0.3), 0 0 30px rgba(255,153,0,0.2);
        border-color: #FF9900;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .img-caption-text {
        font-size: 18px;
        background: linear-gradient(45deg, #0055A5, #003366);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        margin-top: 8px;
        letter-spacing: 1.5px;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0,85,165,0.2);
    }
    .divider {
        border: none;
        border-top: 2px solid #e0e7ef;
        margin: 40px 0 32px 0;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 48px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# 標題
# ---------------------
st.markdown("<div class='center-title'>🛠️ 功能介紹</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 功能：動態牆
# ---------------------
st.markdown("<div class='feature-title'>📢 動態牆</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
用戶可發布貼文、留言、按讚，像校園版 Dcard/Threads，<br>
即時分享接案心得、討論生活大小事，打造活躍的校園社群交流。
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 重做UI-追蹤主題.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>追蹤中-首頁UI</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 查看匿名貼文.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>查看貼文</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 各主題.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>主題瀏覽</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 功能：小遊戲模組
# ---------------------
st.markdown("<div class='feature-title'>🎮 小遊戲<br>應用商店</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
內建輕鬆好玩的自製小遊戲，讓同學們在課餘時間放鬆之餘，<br>
還能賺取代幣，用於兌換軟體內虛擬物品或合作商家優惠，<br>
提升使用黏著度與互動性！
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("遊戲-主ui.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>遊戲首頁</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("遊戲- intro.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>遊戲介紹</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("代幣兌換首頁.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>代幣兌換區</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 功能：接案 / 提案
# ---------------------
st.markdown("<div class='feature-title'>🤝 接案 / 提案</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
模仿 Uber 模式，平台提供雙向接發案：<br>
接案者能接到官方配對的任務，發案者可發布需求找到合適人才。<br>
並透過身分驗證、違約賠償條款，保障雙方權益。
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("接案者模式 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>接案模式首頁</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("發案者模式已刊登 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>發案模式首頁</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("發案者模式已刊登 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>瀏覽接案者個人資料</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 功能：即時訊息
# ---------------------
st.markdown("<div class='feature-title'>💬 即時訊息<br>聊天室</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
即時聊天室功能，讓接案雙方或好友間能快速溝通，<br>
也提供官方通知頻道，確保每筆交易流程清楚透明，<br>
降低誤會發生，提升使用者信任感。
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息-主ui.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>訊息首頁</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息聊天室(線上).png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>聊天室(在線上)</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息聊天室(未在線上).png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>聊天室(未在線上)</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 技術規格區塊
# ---------------------
st.markdown("<div class='feature-title'>💻 技術規格</div>", unsafe_allow_html=True)
tech1, tech2 = st.columns(2)
with tech1:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #f0f8ff); padding:25px; border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#0055A5; margin-bottom:15px;">📱 支援平台</h4>
        <ul style="color:#234; line-height:1.8;">
            <li>iOS 12.0 以上</li>
            <li>Android 8.0 以上</li>
            <li>Web 版本（所有主流瀏覽器）</li>
            <li>PWA 支援</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with tech2:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #fff8f0); padding:25px; border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#FF9900; margin-bottom:15px;">🔒 安全特色</h4>
        <ul style="color:#234; line-height:1.8;">
            <li>SSL 加密傳輸</li>
            <li>雙因子驗證</li>
            <li>第三方金流保障</li>
            <li>人工審核接案人員</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# 頁尾
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | 功能介紹</div>",
    unsafe_allow_html=True
)
