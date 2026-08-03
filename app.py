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

# Stripe payment link
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"
st.sidebar.markdown(f"[Buy Pro Access ($9)]({stripe_link})", unsafe_allow_html=True)

# Simulated Pro mode check
is_pro = st.sidebar.checkbox("I have paid for Pro (Test Mode)")

# --- CREATOR SETTINGS ---
st.sidebar.markdown("---")
st.sidebar.header("⚙️ Creator Settings")
video_length = st.sidebar.selectbox("Video Length / Type", ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox("Target Audience", ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- MAIN MENU (Tabs - 5 kpl nyt mukana!) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Basic Searches & Trends", 
    "✨ AI Tools & Ideas", 
    "🎯 Thumbnail Generator", 
    "📄 PDF Analyzer",
    "🏷️ YouTube Tags & SEO"
])

# --- TAB 1: Basic Searches & Trends ---
with tab1:
    st.title("🎬 YouTube Content Creator Tool")
    st.write("Search keywords, explore trends, and estimate earnings for free.")
    
    keyword = st.text_input("Enter a keyword or topic (e.g., gaming, cooking):")
    
    if st.button("Search Data"):
        if keyword:
            st.success(f"Found the following preliminary data for '{keyword}':")
            
            col1, col2, col3 = st.columns(3)
            col1.metric(label="Estimated Searches / mo", value="45,200", delta="+12%")
            col2.metric(label="Competition", value="Medium", delta="-5%", delta_color="inverse")
            col3.metric(label="Average RPM", value="$4.50", delta="$0.2")
            
            st.info("💡 Tip: Go to the 'AI Tools & Ideas' tab to generate AI titles and scripts!")
        else:
            st.warning("Please enter a keyword first.")

    # Lisätty: Myyntiä vauhdittava "How Pro Works" -esittely ilmaispuolelle
    st.markdown("---")
    with st.expander("🚀 Miksi päivittää Pro-versioon? (Katso ominaisuudet)"):
        st.write("""
        Ilmaisversio auttaa sinua alkuun perustietojen ja hakusanojen kanssa, mutta **Pro-versio** avaa täyden arsenaalin sisällöntuotannon tekoälytyökaluja:
        * **Viral Idea Generator:** Luo rajattomasti viraaliideoita kohderyhmällesi.
        * **AI Metadata & Scriptwriter:** Kirjoittaa puolestasi klikkiotsikot, kuvaukset ja aloituskoukut.
        * **Thumbnail Generator:** Antaa tarkat visuaaliset reseptit pikkukuville, jotka pysäyttävät selailun.
        * **PDF Analyzer:** Analysoi käsikirjoitukset ja antaa parannusehdotuksia.
        * **YouTube Tags & SEO:** Generoi valmiit optimoidut hakutagit suoraan YouTubeen sekunneissa!
        """)

# --- TAB 2: AI Tools & Viral Ideas ---
with tab2:
    st.title("🤖 AI-Powered Tools")
    st.write(f"Current Settings: **{video_length}** | Target Audience: **{target_audience}**")
    
    if not client:
        st.error("OpenAI API key is missing! Please set it in Streamlit Cloud Secrets.")
    else:
        # Päivitetty: Lisätty kolmas vaihtoehto valikkoon ("Video Title Improver")
        ai_tool_choice = st.selectbox("Select AI Feature:", [
            "Viral Idea Generator (Idea Machine)", 
            "AI Metadata & Script", 
            "Video Title Improver / Roster"
        ])
        
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
                                    {"role": "user", "content": f"Create 3 click-worthy titles, an engaging description, and a short video introduction (hook) for a {video_length} video about '{video_topic}' targeted at {target_audience}."}
                                ],
                                temperature=0.7
                            )
                            st.success("Metadata and script generated successfully!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")

        else:
            # Uusi ominaisuus: Video Title Improver
            st.subheader("🔥 Video Title Improver & Roster")
            existing_title = st.text_input("Syötä olemassa oleva tai suunnittelemasi otsikko:")
            
            if st.button("Paranna otsikkoa"):
                if not is_pro:
                    st.warning("🔒 Tämä on Pro-ominaisuus. Osta Pro sivupalkista tai kytke testitila päälle!")
                elif not existing_title:
                    st.warning("Syötä ensin jokin otsikko.")
                else:
                    with st.spinner("Analysoidaan ja parannetaan otsikkoa..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "You are a YouTube CTR and headline optimization expert."},
                                    {"role": "user", "content": f"Analyze this YouTube title: '{existing_title}'. Give 3-5 improved, high-CTR alternative versions designed to make it 50% more clickable, and explain briefly why they work better."}
                                ],
                                temperature=0.7
                            )
                            st.success("Otsikkoehdotukset luotu!")
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

# --- TAB 4: PDF Analyzer ---
with tab4:
    st.title("📄 PDF Script & Document Analyzer")
    st.write("Upload a script or outline PDF, and let AI review it for pacing and engagement.")
    
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        if not is_pro:
            st.warning("🔒 PDF analysis is a Pro feature. Unlock it via the sidebar!")
        else:
            st.success("PDF uploaded successfully!")
            if st.button("Analyze Script"):
                st.info("Tähän voidaan kytkeä PDF-tekstin luku ja tekoälyanalyysi.")

# --- TAB 5: YouTube Tags & SEO Generator ---
with tab5:
    st.title("🏷️ YouTube Tags & SEO Generator")
    st.write("Hanki optimoidut hakutagit ja avainsanat videollesi sekunneissa.")
    
    tag_topic = st.text_input("Mistä aiheesta tai videosta haluat luoda tagit?")
    
    if st.button("Generoi tagit"):
        if not is_pro:
            st.warning("🔒 Tagien generointi on Pro-ominaisuus. Osta Pro sivupalkista tai kytke testitila päälle!")
        elif not tag_topic:
            st.warning("Syötä ensin videon aihe.")
        else:
            with st.spinner("Luodaan hakutageja ja SEO-avainsanoja..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a YouTube SEO expert who specializes in keyword tagging and search optimization."},
                            {"role": "user", "content": f"Generate a comprehensive list of high-performing YouTube search tags and comma-separated keywords for a video about: '{tag_topic}'. Provide both broad and long-tail tags that can be copied directly into YouTube Studio."}
                        ],
                        temperature=0.7
                    )
                    st.success("Tagit generoitu onnistuneesti!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
