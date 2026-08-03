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

# Päivitetty Oikea Stripe-linkki
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Buy Pro Access ($9)</a>', unsafe_allow_html=True)

# Simulated Pro mode check
st.sidebar.markdown("---")
is_pro = st.sidebar.checkbox("I have paid for Pro (Test Mode)")

# --- CREATOR SETTINGS ---
st.sidebar.markdown("---")
st.sidebar.header("⚙️ Creator Settings")
video_length = st.sidebar.selectbox("Video Length / Type", ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox("Target Audience", ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- MAIN MENU (Tabs) ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Basic Searches", 
    "✨ AI Tools", 
    "🎯 Thumbnails", 
    "📄 PDF Analyzer",
    "🏷️ Tags & SEO",
    "🔥 Pro Toolkit"
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
            
            st.info("💡 Tip: Go to the 'AI Tools' tab to generate AI titles and scripts!")
        else:
            st.warning("Please enter a keyword first.")

    st.markdown("---")
    
    st.markdown("""
        <div class="pro-card">
            <h3>🚀 Unlock the Full Power with Pro ($9)</h3>
            <p>The free version includes basic keyword searches. Upgrading to Pro gives you complete access to:</p>
            <ul>
                <b>Viral Idea Generator & 3-Second Hooks</b><br>
                <b>AI Metadata, Descriptions & Scripts</b><br>
                <b>Scroll-stopping Thumbnail Recipes</b><br>
                <b>PDF Script & Pacing Analyzer</b><br>
                <b>YouTube Tags & SEO Generator</b><br>
                <b>Community Posts & Sponsorship Pitch Emails</b>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: AI Tools & Viral Ideas (PRO) ---
with tab2:
    st.title("🤖 AI-Powered Tools")
    st.markdown(f"Current Settings: **{video_length}** | Target Audience: **{target_audience}**")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** This section requires Pro access. Buy Pro via the sidebar or enable test mode!")
    elif not client:
        st.error("OpenAI API key is missing! Please set it in Streamlit Cloud Secrets.")
    else:
        ai_tool_choice = st.selectbox("Select AI Feature:", [
            "Viral Idea Generator (Idea Machine)", 
            "AI Metadata & Script", 
            "Video Title Improver / Roster"
        ])
        
        if ai_tool_choice == "Viral Idea Generator (Idea Machine)":
            st.subheader("💡 Viral Idea Generator")
            niche = st.text_input("What is your channel niche/topic? (e.g., Finance, Gaming, Wellness)")
            
            if st.button("Generate Viral Ideas", type="primary"):
                if not niche:
                    st.warning("Please enter a niche first.")
                else:
                    with st.spinner("AI is brainstorming viral ideas..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a top-tier YouTube strategist."},
                                    {"role": "user", "content": f"Create 5 highly engaging viral video concepts for the niche '{niche}' tailored for a {video_length} video targeting {target_audience}. Give each idea a catchy title and a short explanation."}
                                ],
                                temperature=0.7
                            )
                            st.success("Viral ideas generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error in AI request: {e}")

        elif ai_tool_choice == "AI Metadata & Script":
            st.subheader("✍️ AI Metadata & Scriptwriter")
            video_topic = st.text_input("Exact video topic:")
            
            if st.button("Generate Titles and Script", type="primary"):
                if not video_topic:
                    st.warning("Please enter a video topic.")
                else:
                    with st.spinner("Writing content..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a professional YouTube scriptwriter."},
                                    {"role": "user", "content": f"Create 3 click-worthy titles, an engaging description, and a short video introduction (hook) for a {video_length} video about '{video_topic}' targeted at {target_audience}."}
                                ],
                                temperature=0.7
                            )
                            st.success("Metadata and script generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

        else:
            st.subheader("🔥 Video Title Improver & Roster")
            existing_title = st.text_input("Enter your existing or planned video title:")
            
            if st.button("Improve Title", type="primary"):
                if not existing_title:
                    st.warning("Please enter a title first.")
                else:
                    with st.spinner("Analyzing and improving title..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a YouTube CTR and headline optimization expert."},
                                    {"role": "user", "content": f"Analyze this YouTube title: '{existing_title}'. Give 3-5 improved, high-CTR alternative versions designed to make it 50% more clickable, and explain briefly why they work better."}
                                ],
                                temperature=0.7
                            )
                            st.success("Title suggestions generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

# --- TAB 3: Thumbnail Concept Generator (PRO) ---
with tab3:
    st.title("🎯 Thumbnail Concept Generator")
    st.markdown("Get a precise visual recipe from AI for a thumbnail that stops the scroll.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** This section requires Pro access. Buy Pro via the sidebar or enable test mode!")
    else:
        thumb_topic = st.text_input("What is the core idea or surprising twist of the video?")
        thumb_style = st.selectbox("Visual Style", ["Shocking / Surprising", "Minimalist & Clean", "Meme / Funny", "Comparison (Before vs After)"])
        
        if st.button("Generate Thumbnail Ideas", type="primary"):
            if not thumb_topic:
                st.warning("Please enter your video idea first.")
            elif not client:
                st.error("OpenAI key is missing from settings.")
            else:
                with st.spinner("Designing click magnets..."):
                    try:
                        prompt = f"""
                        Act as a YouTube thumbnail expert. Create 3 different visual ideas for a thumbnail based on the topic: '{thumb_topic}'.
                        Selected style: {thumb_style}.
                        Each idea must specify:
                        1. Visual composition and background
                        2. Text on image (maximum 3 words, all caps)
                        3. Primary colors
                        """
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "You are a graphic designer and YouTube CTR expert."},
                                {"role": "user", "content": prompt}
                            ],
                            temperature=0.7
                        )
                        tulo = response.choices[0].message.content
                        st.success("Thumbnail ideas generated successfully!")
                        st.write(tulo)
                    except Exception as e:
                        st.error(f"Error: {e}")

# --- TAB 4: PDF Analyzer (PRO) ---
with tab4:
    st.title("📄 PDF Script Analyzer")
    st.markdown("Upload a script or outline PDF, and let AI review it for pacing and engagement.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** This section requires Pro access. Buy Pro via the sidebar or enable test mode!")
    else:
        uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])
        
        if uploaded_file is not None:
            st.success("PDF uploaded successfully!")
            if st.button("Analyze Script", type="primary"):
                st.info("PDF text reading and AI analysis integration point.")

# --- TAB 5: YouTube Tags & SEO Generator (PRO) ---
with tab5:
    st.title("🏷️ YouTube Tags & SEO Generator")
    st.markdown("Get optimized search tags and keywords for your video in seconds.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** This section requires Pro access. Buy Pro via the sidebar or enable test mode!")
    else:
        tag_topic = st.text_input("What topic or video do you want to generate tags for?")
        
        if st.button("Generate Tags", type="primary"):
            if not tag_topic:
                st.warning("Please enter a video topic first.")
            else:
                with st.spinner("Generating search tags and SEO keywords..."):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "You are a YouTube SEO expert who specializes in keyword tagging and search optimization."},
                                {"role": "user", "content": f"Generate a comprehensive list of high-performing YouTube search tags and comma-separated keywords for a video about: '{tag_topic}'. Provide both broad and long-tail tags that can be copied directly into YouTube Studio."}
                            ],
                            temperature=0.7
                        )
                        st.success("Tags generated successfully!")
                        st.write(response.choices[0].message.content)
                    except Exception as e:
                        st.error(f"Error: {e}")

# --- TAB 6: Pro Creator Toolkit (PRO) ---
with tab6:
    st.title("🔥 Pro Creator Advanced Toolkit")
    st.markdown("Advanced tools to skyrocket retention, community engagement, and monetization.")
    
    if not is_pro:
        st.warning("🔒 **Pro Feature:** This section requires Pro access. Buy Pro via the sidebar or enable test mode!")
    else:
        pro_tool = st.selectbox("Select Advanced Tool:", [
            "1. Retention Hook Generator", 
            "2. Community Post & Poll Generator", 
            "3. Content Repurposer (Shorts / X Thread)", 
            "4. Sponsorship Pitch Email Generator"
        ])
        
        if pro_tool == "1. Retention Hook Generator":
            st.subheader("🎣 3-Second Retention Hook Generator")
            hook_topic = st.text_input("What is your video about?")
            
            if st.button("Generate Hooks", type="primary"):
                if not hook_topic:
                    st.warning("Please enter your video topic.")
                else:
                    with st.spinner("Crafting retention hooks..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are an expert in YouTube audience retention and viewer psychology."},
                                    {"role": "user", "content": f"Create 3 powerful opening hooks (first 3-5 seconds) for a YouTube video about '{hook_topic}'. Make them punchy, curiosity-driven, and designed to stop viewers from clicking away."}
                                ],
                                temperature=0.7
                            )
                            st.success("Hooks generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

        elif pro_tool == "2. Community Post & Poll Generator":
            st.subheader("💬 Community Tab Post & Poll Generator")
            comm_topic = st.text_input("What do you want to post or ask your audience about?")
            
            if st.button("Generate Community Post", type="primary"):
                if not comm_topic:
                    st.warning("Please enter a topic.")
                else:
                    with st.spinner("Generating community engagement post..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a community manager specialized in maximizing YouTube Community tab engagement."},
                                    {"role": "user", "content": f"Create a high-engagement YouTube Community tab post based on: '{comm_topic}'. Include a catchy text teaser and a multi-choice poll option to drive comments and votes."}
                                ],
                                temperature=0.7
                            )
                            st.success("Community post generated!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

        elif pro_tool == "3. Content Repurposer (Shorts / X Thread)":
            st.subheader("♻️ Content Repurposer")
            long_content = st.text_area("Paste your video script, description, or core idea here:")
            
            if st.button("Repurpose Content", type="primary"):
                if not long_content:
                    st.warning("Please paste some content first.")
                else:
                    with st.spinner("Repurposing content for multi-platform..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a social media repurposing expert."},
                                    {"role": "user", "content": f"Take this YouTube content/script and convert it into: 1) A punchy TikTok/Shorts script, and 2) A 4-part X (Twitter) thread. Source material: '{long_content}'"}
                                ],
                                temperature=0.7
                            )
                            st.success("Content successfully repurposed!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

        else:
            st.subheader("🤝 Sponsorship Pitch Email Generator")
            brand_info = st.text_input("What is the brand name / product you want to pitch to?")
            channel_niche = st.text_input("Briefly describe your channel/niche and viewer stats:")
            
            if st.button("Generate Pitch Email", type="primary"):
                if not brand_info or not channel_niche:
                    st.warning("Please fill in both fields.")
                else:
                    with st.spinner("Writing professional sponsorship pitch..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a professional talent manager and sponsorship closer."},
                                    {"role": "user", "content": f"Write a professional, high-converting sponsorship pitch email to a brand named '{brand_info}'. My channel background: '{channel_niche}'. Highlight the value proposition and why partnering with my channel benefits them."}
                                ],
                                temperature=0.7
                            )
                            st.success("Pitch email generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")
