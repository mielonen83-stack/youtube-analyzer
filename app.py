import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# --- MOBIILIYSTÄVÄLLINEN & RESPONSIIVINEN CSS ---
st.markdown("""
    <style>
    /* Pienennetään otsikoita hieman mobiiliystävällisemmiksi */
    @media (max-width: 768px) {
        h1 { font-size: 1.8rem !important; }
        h2 { font-size: 1.4rem !important; }
        h3 { font-size: 1.1rem !important; }
        .stButton button { width: 100% !important; } /* Napit koko leveydelle puhelimessa */
    }
    
    h1 {
        color: #FF0000;
        font-weight: 800;
    }
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        padding-top: 10px;
    }
    .pro-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FF0000;
        margin-bottom: 15px;
    }
    .buy-button {
        display: block;
        width: 100%;
        background-color: #FF0000;
        color: white !important;
        text-align: center;
        padding: 12px 15px;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .buy-button:hover {
        background-color: #cc0000;
    }
    </style>
""", unsafe_allow_html=True)

try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"

# --- SIDEBAR ---
st.sidebar.markdown("### 🚀 YouTube Pro Suite")
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Buy Pro Access (9 €)</a>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Access Control")
entered_password = st.sidebar.text_input("Enter Pro Password:", type="password")

SECRET_PASSWORD = "tubepro2026"
is_pro = (entered_password == SECRET_PASSWORD)

if is_pro:
    st.sidebar.success("✅ Pro Unlocked")

st.sidebar.markdown("---")
st.sidebar.header("📱 Navigation Menu")
menu_choice = st.sidebar.selectbox("Choose Tool:", [
    "📊 Basic Search", 
    "💡 Ideas & Hooks", 
    "✍️ Scripts & Shorts", 
    "🎯 Thumbnails", 
    "🏷️ SEO & Tags",
    "💬 Comments",
    "♻️ Repurpose",
    "🤝 Sponsorship",
    "🌍 Translator",
    "🏆 Competitor Audit",
    "⚡ Bulk Edit Tools",
    "📈 Data & Analytics",
    "🎨 Channel Branding",
    "⏱️ Timestamp Generator",
    "🧠 Title A/B Matrix",
    "🎨 AI Image Prompts",
    "🎙️ Script Voice Optimizer",
    "💰 Growth & ROI Simulator"
])

st.sidebar.markdown("---")
st.sidebar.header("⚙️ Settings")
video_length = st.sidebar.selectbox("Video Length", ["Shorts (< 60 sec)", "Standard (8-15 min)", "Deep Dive (> 20 min)"])
target_audience = st.sidebar.selectbox("Audience", ["Beginners", "Advanced / Pro", "General"])

def render_paywall_warning():
    st.warning("🔒 **Pro Feature:** Unlock all tools to use this.")
    st.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Unlock All 18 Tools for 9 €</a>', unsafe_allow_html=True)

# --- TAB 1: Basic Search ---
if menu_choice == "📊 Basic Search":
    st.title("🎬 YouTube Creator Hub")
    st.markdown("Search keywords and explore trends for free.")
    
    keyword = st.text_input("🔍 Enter keyword/topic:")
    
    if st.button("Search Data", type="primary"):
        if keyword:
            st.success(f"Preliminary data for '{keyword}':")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Searches", "45k", "+12%")
            with col2:
                st.metric("Competition", "Medium")
            with col3:
                st.metric("RPM", "$4.50")
        else:
            st.warning("Enter a keyword first.")

    st.markdown("---")
    st.markdown(f"""
        <div class="pro-card">
            <h3>🚀 Unlock Full Pro (9 €)</h3>
            <p>Get instant access to all 18 AI generators!</p>
            <a href="{stripe_link}" target="_blank" style="color: #FF0000; font-weight: bold; text-decoration: underline;">Upgrade Now &rarr;</a>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: Ideas & Hooks ---
elif menu_choice == "💡 Ideas & Hooks":
    st.title("💡 Viral Ideas & Hooks")
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("API key missing!")
    else:
        sub_tool = st.radio("Tool:", ["Viral Ideas", "Retention Hooks", "Channel Niche"])
        if sub_tool == "Viral Ideas":
            niche = st.text_input("Niche:")
            if st.button("Generate", type="primary") and niche:
                res = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"Create 5 viral video concepts for niche '{niche}'."}])
                st.write(res.choices[0].message.content)
        elif sub_tool == "Retention Hooks":
            topic = st.text_input("Topic:")
            if st.button("Generate", type="primary") and topic:
                res = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"Create 3 retention hooks for '{topic}'."}])
                st.write(res.choices[0].message.content)
        else:
            passions = st.text_input("Interests:")
            if st.button("Generate", type="primary") and passions:
                res = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"Create 3 channel concepts for '{passions}'."}])
                st.write(res.choices[0].message.content)

# (Muut tabit pysyvät logiikaltaan ennallaan, mutta hyödyntävät mobiiliystävällistä muotoilua)
elif menu_choice == "✍️ Scripts & Shorts":
    st.title("✍️ Scripts & Shorts")
    if not is_pro: render_paywall_warning()
    else:
        topic = st.text_input("Topic:")
        if st.button("Generate Script", type="primary") and topic and client:
            res = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"Write a script about '{topic}'"}])
            st.write(res.choices[0].message.content)

elif menu_choice == "💰 Growth & ROI Simulator":
    st.title("💰 Growth & ROI Simulator")
    if not is_pro:
        render_paywall_warning()
    else:
        sim_views = st.number_input("Views", value=10000)
        sim_rpm = st.slider("RPM ($)", 0.5, 30.0, 4.5)
        if st.button("Calculate", type="primary"):
            earn = (sim_views / 1000) * sim_rpm
            st.metric("Estimated Revenue", f"${earn:.2f}")

# (Voit lisätä muutkin välilehdet tarpeen mukaan vanhasta koodista tähän väliin)
