import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# Fetch OpenAI API key securely from Streamlit Secrets
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# --- SIDEBAR: Management & Payments ---
st.sidebar.header("🚀 Pro Version")
st.sidebar.write("Unlock all AI tools and unlimited searches!")

# Stripe payment link (Replace with your actual Stripe Payment Link URL)
stripe_link = "https://buy.stripe.com/test_placeholder"
st.sidebar.markdown(f"[Buy Pro Access ($9)]({stripe_link})", unsafe_allow_html=True)

# Simulated Pro mode check (User can test by checking the box)
is_pro = st.sidebar.checkbox("I have paid for Pro (Test Mode)")

# --- MAIN MENU (Tabs) ---
tab1, tab2, tab3 = st.tabs(["📊 Basic Searches & Trends", "✨ AI Tools & Ideas", "🎯 Thumbnail Generator"])

# --- TAB 1: Basic Searches & Trends ---
with tab1:
    st.title("🎬 YouTube Content Creator Tool")
    st.write("Search keywords, explore trends, and estimate earnings for free.")
    
    keyword = st.text_input("Enter a keyword or topic (e.g., gaming, cooking):")
    
    if st.button("Search Data"):
        if keyword:
            st.success(f"Found the following preliminary data for '{keyword}':")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estimated Searches / mo", "45,200", "+12%")
            col2.metric("Competition", "Medium", "-5%")
            col3.metric("Average RPM", "$4.50", "$0.2")
            
            st.info("💡 Tip: Go to the 'AI Tools & Ideas' tab to generate AI titles and scripts!")
        else:
            st.warning("Please enter a keyword first.")

# --- TAB 2: AI Tools & Viral Ideas ---
with tab2:
    st.title("🤖 AI-Powered Tools")
    
    if not client:
        st.error("OpenAI API key is missing! Please set it in Streamlit Cloud Secrets.")
    else:
        # Sub-selection for tools
        ai_tool_choice = st.selectbox("Select AI Feature:", ["Viral Idea Generator (Idea Machine)", "AI Metadata & Script"])
        
        if ai_tool_choice == "Viral Idea Generator (Idea Machine)":
            st.subheader("💡 Viral Idea Generator")
            niche = st.text_input("What is your channel niche/topic? (e.g., Finance, Gaming, Wellness)")
            
            if st.button("Generate Viral Ideas"):
                if not is_pro:
                    st.warning("🔒 This is a Pro feature. Buy Pro access via the sidebar or enable test mode!")
                elif not niche:
                    st.warning("Please enter a niche first.")
                else:
                    with st.spinner("AI is brainstorming viral ideas..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a top-tier YouTube strategist."},
                                    {"role": "user", "content": f"Create 5 highly engaging and original viral video concepts for the niche '{niche}'. Give each idea a catchy title and a short explanation of why it would work."}
                                ],
                                temperature=0.7
                            )
                            st.success("Viral ideas generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error in AI request: {e}")

        else:
            st.subheader("✍️ AI Metadata & Scriptwriter")
            video_topic = st.text_input("Exact video topic:")
            
            if st.button("Generate Titles and Script"):
                if not is_pro:
                    st.warning("🔒 This is a Pro feature. Buy Pro access via the sidebar!")
                elif not video_topic:
                    st.warning("Please enter a video topic.")
                else:
                    with st.spinner("Writing content..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a professional YouTube scriptwriter."},
                                    {"role": "user", "content": f"Create 3 click-worthy titles, an engaging description, and a short video introduction (hook) for the video '{video_topic}'."}
                                ],
                                temperature=0.7
                            )
                            st.success("Metadata and script generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

# --- TAB 3: Thumbnail Concept Generator ---
with tab3:
    st.title("🎯 Thumbnail Concept Generator")
    st.write("Get a precise visual recipe from AI for a thumbnail that stops the scroll.")
    
    thumb_topic = st.text_input("What is the core idea or surprising twist of the video?")
    thumb_style = st.selectbox("Visual Style", ["Shocking / Surprising", "Minimalist & Clean", "Meme / Funny", "Comparison (Before vs After)"])
    
    if st.button("Generate Thumbnail Ideas"):
        if not is_pro:
            st.warning("🔒 This requires a Pro version!")
        elif not thumb_topic:
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
