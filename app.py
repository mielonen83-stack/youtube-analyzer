import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# --- CUSTOM CSS (Visuaalinen parannus) ---
st.markdown("""
    <style>
    h1 {
        color: #FF0000;
        font-weight: 800;
    }
    h2, h3 {
        color: #222222;
    }
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        padding-top: 20px;
    }
    .pro-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF0000;
        margin-bottom: 20px;
    }
    /* Tyylitelty ostonappi sivupalkkiin */
    .buy-button {
        display: block;
        width: 100%;
        background-color: #FF0000;
        color: white !important;
        text-align: center;
        padding: 10px 15px;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: none;
        margin-bottom: 10px;
    }
    .buy-button:hover {
        background-color: #cc0000;
    }
    </style>
""", unsafe_allow_html=True)

# Fetch OpenAI API key securely from Streamlit Secrets
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# --- SIDEBAR: Management & Payments ---
st.sidebar.markdown("### 🚀 YouTube Pro Suite")
st.sidebar.write("Unlock all AI tools and unlimited searches!")

# Stripe-maksulinkki ja hinta euroina
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Buy Pro Access (9 €)</a>', unsafe_allow_html=True)

# Simulated Pro mode check
st.sidebar.markdown("---")
is_pro = st.sidebar.checkbox("I have paid for Pro (Test Mode)")

# --- CREATOR SETTINGS ---
st.sidebar.markdown("---")
st.sidebar.header("⚙️ Creator Settings")
video_length = st.sidebar.selectbox("Video Length / Type", ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox("Target Audience", ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- MAIN MENU (Tabs) ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Basic", 
    "💡 Ideas & Hooks", 
    "✍️ Scripts", 
    "🎯 Thumbnails", 
    "🏷️ SEO & Tags",
    "💬 Comments",
    "♻️ Repurpose",
    "🤝 Sponsorship"
])

# --- TAB 1: Basic Searches & Trends (ILMAINEN) ---
with tab1:
    st.title("🎬 YouTube Creator Hub")
    st.markdown("Search keywords, explore trends, and estimate earnings for free.")
    
    keyword = st.text_input("🔍 Enter a keyword or topic (e.g., gaming, cooking):")
    
    if st.button("Search Data", type="primary"):
        if keyword:
            st.success(f"Found preliminary data for '{keyword}':")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Estimated Searches / mo", value="45,200", delta="+12%")
            with col2:
                st.metric(label="Competition", value="Medium", delta="-5%", delta_color="inverse")
            with col3:
                st.metric(label="Average RPM", value="$4.50", delta="$0.2")
            
            st.info("💡 Tip: Unlock Pro to use all advanced AI tools!")
        else:
            st.warning("Please enter a keyword first.")

    st.markdown("---")
    
    st.markdown("""
        <div class="pro-card">
            <h3>🚀 Unlock the Full Power with Pro (9 €)</h3>
            <p>Upgrading gives you complete access to 8 advanced AI generators:</p>
            <ul>
                <b>Viral Ideas & 3-Second Hooks</b><br>
                <b>Full Scripts & Shorts Machine</b><br>
                <b>Thumbnail Recipes & SEO Tags</b><br>
                <b>Comment Assistant & Sponsorship Pitch Emails</b>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: Ideas & Hooks (PRO) ---
with tab2:
    st.title("💡 Viral Ideas & Hooks Generator")
    st.markdown("Brainstorm high-CTR concepts and powerful 3-second opening hooks.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        sub_tool = st.radio("Choose tool:", ["Viral Idea Generator", "3-Second Retention Hooks", "Channel Niche & Name Ideas"])
        
        if sub_tool == "Viral Idea Generator":
            niche = st.text_input("Channel niche or topic (e.g., Finance, Gaming):")
            if st.button("Generate Ideas", type="primary") and niche:
                with st.spinner("Brainstorming..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a top YouTube strategist."},
                            {"role": "user", "content": f"Create 5 viral video concepts for niche '{niche}' tailored for {video_length} targeting {target_audience}."}
                        ],
                        temperature=0.7
                    )
                    st.success("Done!")
                    st.write(res.choices[0].message.content)
                    
        elif sub_tool == "3-Second Retention Hooks":
            hook_topic = st.text_input("Video topic:")
            if st.button("Generate Hooks", type="primary") and hook_topic:
                with st.spinner("Crafting hooks..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a retention psychology expert."},
                            {"role": "user", "content": f"Create 3 powerful opening hooks (first 3-5 seconds) for a video about '{hook_topic}'."}
                        ],
                        temperature=0.7
                    )
                    st.success("Done!")
                    st.write(res.choices[0].message.content)
                    
        else:
            passion = st.text_input("What are your interests or skills?")
            if st.button("Generate Channel Concepts", type="primary") and passion:
                with st.spinner("Generating channel ideas..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a YouTube branding expert."},
                            {"role": "user", "content": f"Create 3 catchy channel names and content strategies based on interests: '{passion}'."}
                        ],
                        temperature=0.7
                    )
                    st.success("Done!")
                    st.write(res.choices[0].message.content)

# --- TAB 3: Scripts & Shorts (PRO) ---
with tab3:
    st.title("✍️ Full Scripts & Shorts Machine")
    st.markdown("Generate full minute-by-minute video scripts or viral short-form scripts.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        script_type = st.radio("Script Type:", ["Full Video Script (Minute-by-Minute)", "YouTube Short / TikTok Script (< 60s)"])
        script_topic = st.text_input("Exact video topic or title:")
        
        if st.button("Generate Script", type="primary") and script_topic:
            with st.spinner("Writing script..."):
                prompt = f"Create a full minute-by-minute script for a {video_length} video about '{script_topic}'." if "Full" in script_type else f"Create a punchy, fast-paced under-60-second vertical video script with a twist for: '{script_topic}'."
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional YouTube scriptwriter."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                st.success("Script generated!")
                st.write(res.choices[0].message.content)

# --- TAB 4: Thumbnails (PRO) ---
with tab4:
    st.title("🎯 Thumbnail Concept Generator")
    st.markdown("Get a precise visual recipe for a high-CTR thumbnail.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        thumb_topic = st.text_input("Core idea or twist of the video:")
        thumb_style = st.selectbox("Visual Style", ["Shocking / Surprising", "Minimalist & Clean", "Meme / Funny", "Before vs After"])
        
        if st.button("Generate Thumbnail Recipe", type="primary") and thumb_topic:
            with st.spinner("Designing..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a YouTube CTR and graphic design expert."},
                        {"role": "user", "content": f"Create 3 visual concepts for a thumbnail about '{thumb_topic}' in style '{thumb_style}'. Include background, text (max 3 words), and colors."}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)

# --- TAB 5: SEO & Tags (PRO) ---
with tab5:
    st.title("🏷️ YouTube Tags & SEO Generator")
    st.markdown("Get optimized search tags and keywords ready to copy into YouTube Studio.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        tag_topic = st.text_input("Video topic for SEO tags:")
        if st.button("Generate Tags", type="primary") and tag_topic:
            with st.spinner("Generating SEO tags..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a YouTube SEO expert."},
                        {"role": "user", "content": f"Provide comma-separated high-performing search tags and long-tail keywords for a video about: '{tag_topic}'."}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)

# --- TAB 6: Comments (PRO) ---
with tab6:
    st.title("💬 Comment Reply Assistant")
    st.markdown("Generate engaging, community-building replies to viewer comments.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        viewer_comment = st.text_area("Paste viewer comment here:")
        tone = st.selectbox("Tone:", ["Friendly & Appreciative", "Funny & Witty", "Expert & Informative"])
        
        if st.button("Generate Reply", type="primary") and viewer_comment:
            with st.spinner("Writing reply..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a helpful YouTube creator responding in a {tone} tone."},
                        {"role": "user", "content": f"Write a great reply to this comment: '{viewer_comment}'"}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)

# --- TAB 7: Repurpose (PRO) ---
with tab7:
    st.title("♻️ Content Repurposer")
    st.markdown("Convert your video script into community posts, X (Twitter) threads, or short summaries.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        long_content = st.text_area("Paste your video script or core concept:")
        repurpose_target = st.selectbox("Format:", ["X (Twitter) Thread", "Community Tab Post & Poll", "Newsletter Summary"])
        
        if st.button("Repurpose Content", type="primary") and long_content:
            with st.spinner("Adapting content..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a multi-platform content strategist."},
                        {"role": "user", "content": f"Convert this text into a {repurpose_target}: '{long_content}'"}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)

# --- TAB 8: Sponsorship (PRO) ---
with tab8:
    st.title("🤝 Sponsorship Pitch Email Generator")
    st.markdown("Pitch brands professionally to land lucrative sponsorships.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Requires Pro access or Test Mode!")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        brand_name = st.text_input("Brand name:")
        channel_stats = st.text_input("Your channel niche and viewer stats:")
        
        if st.button("Generate Pitch Email", type="primary") and brand_name and channel_stats:
            with st.spinner("Writing pitch..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional talent manager."},
                        {"role": "user", "content": f"Write a high-converting sponsorship pitch email to '{brand_name}' highlighting my channel background: '{channel_stats}'."}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)
