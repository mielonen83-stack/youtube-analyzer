import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# --- CUSTOM CSS ---
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

try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# --- SIDEBAR: Management, Payments & Menu ---
st.sidebar.markdown("### 🚀 YouTube Pro Suite")
st.sidebar.write("Unlock all AI tools and unlimited searches!")

stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Buy Pro Access (9 €)</a>', unsafe_allow_html=True)

# --- SALASANA-TARKISTUS (TESTAUSVAIHE) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Developer / Owner Access")
entered_password = st.sidebar.text_input("Enter Pro Password:", type="password")

# Määritä tästä oma salasanasi (voit vaihtaa sen halutessasi)
SECRET_PASSWORD = "tubepro2026"

# Tarkistetaan onko salasana oikein
is_pro = (entered_password == SECRET_PASSWORD)

if is_pro:
    st.sidebar.success("✅ Pro Access Unlocked (Dev Mode)")

# --- MOBIILIYSTÄVÄLLINEN VALIKKO SIVUPALKISSA ---
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
    "🧠 Title A/B Matrix"
])

# --- CREATOR SETTINGS ---
st.sidebar.markdown("---")
st.sidebar.header("⚙️ Creator Settings")
video_length = st.sidebar.selectbox("Video Length / Type", ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox("Target Audience", ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- TAB 1: Basic Searches & Trends (ILMAINEN) ---
if menu_choice == "📊 Basic Search":
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
            
            st.info("💡 Tip: Unlock Pro to use all 15 advanced AI tools!")
        else:
            st.warning("Please enter a keyword first.")

    st.markdown("---")
    st.markdown("""
        <div class="pro-card">
            <h3>🚀 Unlock the Full Power with Pro (9 €)</h3>
            <p>Upgrading gives you complete access to all 15 advanced AI generators and optimization suites!</p>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: Ideas & Hooks (PRO) ---
elif menu_choice == "💡 Ideas & Hooks":
    st.title("💡 Viral Ideas & Hooks Generator")
    st.markdown("Brainstorm high-CTR concepts and powerful 3-second opening hooks.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "✍️ Scripts & Shorts":
    st.title("✍️ Full Scripts & Shorts Machine")
    st.markdown("Generate full minute-by-minute video scripts or viral short-form scripts.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "🎯 Thumbnails":
    st.title("🎯 Thumbnail Concept Generator")
    st.markdown("Get a precise visual recipe for a high-CTR thumbnail.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "🏷️ SEO & Tags":
    st.title("🏷️ YouTube Tags & SEO Generator")
    st.markdown("Get optimized search tags and keywords ready to copy into YouTube Studio.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "💬 Comments":
    st.title("💬 Comment Reply Assistant")
    st.markdown("Generate engaging, community-building replies to viewer comments.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "♻️ Repurpose":
    st.title("♻️ Content Repurposer")
    st.markdown("Convert your video script into community posts, X (Twitter) threads, or short summaries.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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
elif menu_choice == "🤝 Sponsorship":
    st.title("🤝 Sponsorship Pitch Email Generator")
    st.markdown("Pitch brands professionally to land lucrative sponsorships.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
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

# --- TAB 9: Translator (PRO) ---
elif menu_choice == "🌍 Translator":
    st.title("🌍 Global Translator & Localizer")
    st.markdown("Translate and optimize your video titles, descriptions, and tags for international audiences.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        text_to_translate = st.text_area("Paste text, title or description to localize:")
        target_lang = st.selectbox("Target Language:", ["English", "Spanish", "German", "French", "Japanese", "Swedish"])
        
        if st.button("Translate & Optimize", type="primary") and text_to_translate:
            with st.spinner("Translating and localizing for maximum reach..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional YouTube localization and translation expert. Make the text sound natural, click-worthy, and optimized for local search habits."},
                        {"role": "user", "content": f"Translate and optimize this text into {target_lang} for international YouTube viewers: '{text_to_translate}'"}
                    ],
                    temperature=0.7
                )
                st.success("Done!")
                st.write(res.choices[0].message.content)

# --- TAB 10: Competitor Audit (PRO) ---
elif menu_choice == "🏆 Competitor Audit":
    st.title("🏆 Competitor & Algorithm Audit")
    st.markdown("Analyze a topic or competitor angle to find the gap and make your video stand out.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        audit_topic = st.text_input("Enter the topic or what competitors are currently covering:")
        competitor_style = st.text_input("What is the standard approach everyone else uses? (optional):")
        
        if st.button("Run Strategy Audit", type="primary") and audit_topic:
            with st.spinner("Analyzing competition and algorithm trends..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an elite YouTube growth strategist and algorithm expert."},
                        {"role": "user", "content": f"Perform a strategic competitor audit for a video about '{audit_topic}'. Standard approach to beat: '{competitor_style}'. Provide: 1) What is missing in current videos, 2) A unique angle to outsmart competitors, and 3) Recommendations for higher CTR and retention."}
                    ],
                    temperature=0.7
                )
                st.success("Audit completed!")
                st.write(res.choices[0].message.content)

# --- TAB 11: Bulk Edit Tools (PRO) ---
elif menu_choice == "⚡ Bulk Edit Tools":
    st.title("⚡ Bulk Edit & Optimization Planner")
    st.markdown("Generate mass templates, description disclaimers, or unified tag structures for multiple videos at once.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        bulk_goal = st.selectbox("Bulk Task:", ["Standard Video Description Template", "Channel-wide End Screen & Card Strategy", "Unified Tag & Keyword Template"])
        channel_niche_bulk = st.text_input("Your channel niche or category:")
        
        if st.button("Generate Bulk Template", type="primary") and channel_niche_bulk:
            with st.spinner("Creating bulk template..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a YouTube operations and automation expert."},
                        {"role": "user", "content": f"Create a comprehensive, reusable {bulk_goal} optimized for a creator in the '{channel_niche_bulk}' niche to apply across multiple videos efficiently."}
                    ],
                    temperature=0.7
                )
                st.success("Template generated!")
                st.write(res.choices[0].message.content)

# --- TAB 12: Data & Analytics (PRO) ---
elif menu_choice == "📈 Data & Analytics":
    st.title("📈 Data & Analytics Health Check")
    st.markdown("Get strategic guidance on how to interpret your CTR, retention rates, and channel analytics.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        st.markdown("Input your video's current metrics to get an AI diagnostic report:")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            ctr_val = st.text_input("Click-Through Rate (CTR %)", value="4.5%")
            avd_val = st.text_input("Average View Duration (Retention)", value="3 min 20 sec")
        with col_m2:
            views_val = st.text_input("View Count / 48h", value="1,200")
            sub_rate = st.text_input("Subscribers Gained from Video", value="15")
            
        if st.button("Analyze Channel Metrics", type="primary"):
            with st.spinner("Analyzing performance data..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a YouTube algorithm data scientist."},
                        {"role": "user", "content": f"Analyze these video stats: CTR {ctr_val}, AVD {avd_val}, Views {views_val}, Subs gained {sub_rate}. Explain what is working, what is failing based on YouTube benchmarks, and give 3 actionable steps to improve performance."}
                    ],
                    temperature=0.7
                )
                st.success("Analytics Diagnostic Ready!")
                st.write(res.choices[0].message.content)

# --- TAB 13: Channel Branding (PRO) ---
elif menu_choice == "🎨 Channel Branding":
    st.title("🎨 AI Channel Name & Branding Generator")
    st.markdown("Input your interests and audience to generate a full visual and verbal branding package.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        brand_interests = st.text_input("Your passions, skills, or niche topics:")
        brand_audience = st.text_input("Who is your target viewer?")
        
        if st.button("Generate Complete Branding Package", type="primary") and brand_interests:
            with st.spinner("Designing brand identity..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an elite YouTube brand strategist and creative director."},
                        {"role": "user", "content": f"Create a full YouTube channel branding package based on interests: '{brand_interests}' targeting '{brand_audience}'. Include: 1) 5 Catchy Channel Names, 2) A powerful channel Slogan, 3) Profile picture visual concept, 4) Banner visual concept and color scheme, and 5) A compelling 'About' section description."}
                    ],
                    temperature=0.7
                )
                st.success("Branding Package Ready!")
                st.write(res.choices[0].message.content)

# --- TAB 14: Timestamp Generator (PRO) ---
elif menu_choice == "⏱️ Timestamp Generator":
    st.title("⏱️ Video Chapter & Timestamp Generator")
    st.markdown("Paste your video script or rough notes to instantly generate SEO-friendly timestamps.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        script_input = st.text_area("Paste your video script, outline, or breakdown notes here:")
        
        if st.button("Generate Timestamps", type="primary") and script_input:
            with st.spinner("Structuring chapters and timestamps..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a YouTube video editor and chapter optimization expert."},
                        {"role": "user", "content": f"Analyze this script/outline and create professional, search-friendly video chapters with precise timestamps format (e.g. 00:00 Introduction). Ensure the first timestamp starts at 00:00. Text: '{script_input}'"}
                    ],
                    temperature=0.7
                )
                st.success("Timestamps Generated!")
                st.write(res.choices[0].message.content)

# --- TAB 15: Title A/B Matrix (PRO) ---
elif menu_choice == "🧠 Title A/B Matrix":
    st.title("🧠 Title A/B Testing Matrix")
    st.markdown("Generate 10 psychologically optimized video title angles to maximize CTR.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** Please purchase Pro Access from the sidebar or enter your developer password.")
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        base_topic = st.text_input("Enter your core video topic or raw idea:")
        
        if st.button("Generate Title Matrix", type="primary") and base_topic:
            with st.spinner("Applying psychological triggers and title formulas..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an expert in YouTube click psychology, CTR optimization, and copywriting."},
                        {"role": "user", "content": f"Create 10 distinct video titles for the topic '{base_topic}', each using a different psychological angle (e.g., Curiosity Gap, Fear of Missing Out, Quick Hack/Shortcut, Contrast/Controversy, Authority, Question, Negative/Warning, Numbers/List, Simplicity, Storytelling). Clearly label the angle for each."}
                    ],
                    temperature=0.7
                )
                st.success("Title Matrix Generated!")
                st.write(res.choices[0].message.content)
