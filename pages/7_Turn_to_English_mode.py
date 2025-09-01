import streamlit as st

# Page config
st.set_page_config(page_title="語言切換", page_icon="🌐", layout="centered")

# Custom CSS for styling and button effect
st.markdown(
    """
    <style>
    body {
        font-family: "Helvetica Neue", Arial, sans-serif;
        background: linear-gradient(135deg, #f0f4ff, #dbe7ff);
    }
    .main-title {
        font-size: 4em;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .description {
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 20px;
        color: #34495e;
    }
    .stButton>button {
        align-items: center;
        background-image: linear-gradient(144deg, #af40ff, #5b42f3 50%, #00ddeb);
        border: 0;
        border-radius: 8px;
        box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
        box-sizing: border-box;
        color: #ffffff;
        display: flex;
        font-size: 18px;
        justify-content: center;
        line-height: 1em;
        max-width: 100%;
        min-width: 140px;
        padding: 3px;
        text-decoration: none;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        white-space: nowrap;
        cursor: pointer;
        transition: all 0.3s;
        margin: 0 auto;
        position: relative;
    }
    .stButton>button:active,
    .stButton>button:hover {
        outline: 0;
    }
    .stButton>button > div {
        background-color: rgb(5, 6, 45);
        padding: 16px 24px;
        border-radius: 6px;
        width: 100%;
        height: 100%;
        transition: 300ms;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white !important;
        font-weight: bold;
    }
    .stButton>button:hover > div {
        background: none;
    }
    .stButton>button:active {
        transform: scale(0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown('<div class="main-title">Switch to English</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Click the button below to switch to the English interface of our official website</div>', unsafe_allow_html=True)

# Load local cartoon illustration
_, col2, _ = st.columns(3)
with col2:
    st.image("LETGO.png", caption="", width=600)

# Redirect button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
       st.link_button("Go English Website 🌍", "https://tasksnap-ytmctx95gflwfq9pxzje2z.streamlit.app")
