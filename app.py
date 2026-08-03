import streamlit as str_module
from openai import OpenAI

# Sivun asetukset
str_module.set_page_config(page_title="YouTube Pro Suite", page_icon="🎬", layout="wide")

# --- KUSTOMOITU ERITTÄIN MODERNI JA HIOTTU CSS ---
str_module.markdown("""
    <style>
    /* Pääalueen tausta ja fontit */
    .main {
        background-color: #f8fafc;
    }
    h1, h2, h3 {
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Sivupalkin tyylittely */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border-right: 1px solid #e2e8f0;
        padding-top: 10px;
    }
    
    /* Pro-kortti sivupalkissa */
    .pro-sidebar-box {
        background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #fecdd3;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(244, 63, 94, 0.1);
    }
    
    /* Tyylikäs Osta-painike */
    .buy-button {
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);
        color: white !important;
        text-align: center;
        padding: 14px 20px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 15px;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(225, 29, 72, 0.3);
        transition: all 0.3s ease;
    }
    .buy-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(225, 29, 72, 0.4);
    }

    /* Streamlit-painikkeiden ja syötteiden hienosäätö */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        transition: all 0.2s ease;
    }
    
    /* Sisältölaatikko tuloksille */
    .result-box {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# OpenAI Client alustus
try:
    openai_api_key = str_module.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# Stripe-maksulinkki (5 euroa)
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"

# --- SIVUPALKKI (Sidebar) ---
str_module.sidebar.markdown("### 🎬 YouTube Pro Suite")
str_module.sidebar.markdown("""
<div class="pro-sidebar-box">
    <div style="font-size: 24px; margin-bottom: 8px;">🚀</div>
    <div style="font-size: 15px; color: #881337; margin-bottom: 14px; font-weight: 600; line-height: 1.4;">Avaa kaikki tekoälytyökalut ja rajaton haku!</div>
    <a href="{}" target="_blank" class="buy-button">🔥 Hanki Pro Access (5 €)</a>
</div>
""".format(stripe_link), unsafe_allow_html=True)

# Kielen valinta (Oletuksena englanti)
str_module.sidebar.markdown("---")
str_module.sidebar.subheader("🌍 Language / Kieli")

languages = ["🇬🇧 English", "🇫🇮 Suomi", "🇸🇪 Svenska", "🇪🇸 Español", "🇩🇪 Deutsch", "🇫🇷 Français", "🇯🇵 日本語"]
if "selected_language" not in str_module.session_state:
    str_module.session_state.selected_language = "🇬🇧 English"

selected_language = str_module.sidebar.selectbox("Select Language:", languages, index=languages.index(str_module.session_state.selected_language), label_visibility="collapsed")
str_module.session_state.selected_language = selected_language
lang_code = selected_language.split()[0]

# --- KAIKKI KÄÄNNÖKSET JA TYÖKALUJEN SISÄLLÖT ---
translations = {
    "🇬🇧": {
        "dev_access": "🔑 Pro License Activation",
        "pass_label": "Enter Pro Password (from receipt):",
        "success_pro": "✅ Pro Access Unlocked!",
        "settings": "⚙️ Creator Settings",
        "v_len": "Video Length / Type",
        "aud": "Target Audience",
        "paywall": "🔒 **Pro Feature:** You need Pro Access to use this tool.",
        "unlock_all": "🔥 Unlock All Tools for 5 €",
        "nav_title": "🛠️ Tools Navigation",
        "cat_label": "Select category:",
        "cat_basics": "💡 Basics, Ideas & Scripts",
        "cat_advanced": "🚀 Advanced SEO, Growth & Analytics",
        "tool_prompt": "Select tool:",
        "tools_basics": {
            "search": "📊 Basic Search & Trends",
            "ideas": "💡 Viral Ideas & Hooks",
            "scripts": "✍️ Scripts & Shorts",
            "thumbnails": "🎯 Thumbnails",
            "seo": "🏷️ SEO & Tags",
            "comments": "💬 Comments Assistant",
            "repurpose": "♻️ Content Repurposer",
            "sponsorship": "🤝 Sponsorship Pitches"
        },
        "tools_advanced": {
            "translator": "🌍 Global Translator",
            "competitor": "🏆 Competitor Audit",
            "bulk": "⚡ Bulk Edit Tools",
            "analytics": "📈 Data & Analytics",
            "branding": "🎨 Channel Branding",
            "timestamps": "⏱️ Timestamp Generator",
            "title_matrix": "🧠 Title A/B Matrix",
            "ai_images": "🎨 AI Image Prompts",
            "voice": "🎙️ Voice Optimizer",
            "simulator": "💰 Growth & ROI Simulator"
        },
        "content": {
            "search": {"title": "📊 Basic Search & Trends", "desc": "Search keywords, explore trends, and estimate earnings using AI.", "input": "🔍 Enter keyword or topic:", "btn": "Search & Analyze", "spinner": "Analyzing keyword '{keyword}' with AI..."},
            "ideas": {"title": "💡 Viral Ideas & Hooks", "input": "Niche / Topic:", "btn": "Generate", "spinner": "Generating..."},
            "scripts": {"title": "✍️ Scripts & Shorts", "input": "Video Topic:", "btn": "Write Script", "spinner": "Writing script..."},
            "thumbnails": {"title": "🎯 Thumbnails", "input": "Core Video Idea:", "btn": "Design Thumbnail", "spinner": "Designing visual concepts..."},
            "seo": {"title": "🏷️ SEO & Tags", "input": "Topic for SEO Tags:", "btn": "Generate Tags", "spinner": "Fetching optimized tags..."},
            "comments": {"title": "💬 Comments Assistant", "input": "Viewer Comment:", "btn": "Write Reply", "spinner": "Writing reply..."},
            "repurpose": {"title": "♻️ Content Repurposer", "input": "Video Script or Text:", "btn": "Repurpose", "spinner": "Adapting content..."},
            "sponsorship": {"title": "🤝 Sponsorship Pitches", "input_brand": "Brand Name:", "input_stats": "Channel Stats / Niche:", "btn": "Write Pitch", "spinner": "Writing email..."},
            "translator": {"title": "🌍 Global Translator & Localizer", "input": "Text to Translate:", "btn": "Translate", "spinner": "Translating..."},
            "competitor": {"title": "🏆 Competitor Audit", "input": "Topic or Competitor Style:", "btn": "Audit Gaps", "spinner": "Analyzing..."},
            "bulk": {"title": "⚡ Bulk Edit Tools", "input": "Channel Niche:", "btn": "Create Bulk Template", "spinner": "Creating..."},
            "analytics": {"title": "📈 Data & Analytics", "btn": "Analyze Metrics", "spinner": "Analyzing stats..."},
            "branding": {"title": "🎨 Channel Branding", "input": "Your Passions / Topic:", "btn": "Create Branding Package", "spinner": "Designing..."},
            "timestamps": {"title": "⏱️ Timestamp Generator", "input": "Script / Content:", "btn": "Generate Timestamps", "spinner": "Creating chapters..."},
            "title_matrix": {"title": "🧠 Title A/B Matrix", "input": "Video Topic / Idea:", "btn": "Create Title Matrix", "spinner": "Creating..."},
            "ai_images": {"title": "🎨 AI Image Prompts", "input": "Thumbnail Subject:", "btn": "Generate Prompts", "spinner": "Formatting prompts..."},
            "voice": {"title": "🎙️ Voice Optimizer", "input": "Raw Text:", "btn": "Optimize for Speech", "spinner": "Adapting..."},
            "simulator": {"title": "💰 Growth & ROI Simulator", "sub1": "Current Subscribers:", "sub2": "Average Views per Video:", "btn": "Simulate Growth", "spinner": "Calculating forecast..."}
        }
    },
    "🇫🇮": {
        "dev_access": "🔑 Pro-käyttöoikeuden aktivointi",
        "pass_label": "Syötä Pro-salasana (saatu kuitista):",
        "success_pro": "✅ Pro-oikeudet aktivoitu!",
        "settings": "⚙️ Sisällöntuottajan Asetukset",
        "v_len": "Videon pituus / Tyyppi",
        "aud": "Kohdeyleisö",
        "paywall": "🔒 **Pro-ominaisuus:** Tarvitset Pro-oikeudet käyttääksesi tätä työkalua.",
        "unlock_all": "🔥 Avaa kaikki työkalut hintaan 5 €",
        "nav_title": "🛠️ Työkalujen Hallinta",
        "cat_label": "Valitse toiminta-alue:",
        "cat_basics": "💡 Perustyökalut, Ideat & Käsikirjoitukset",
        "cat_advanced": "🚀 Edistynyt SEO, Kasvu & Analytiikka",
        "tool_prompt": "Valitse työkalu:",
        "tools_basics": {
            "search": "📊 Perushaku & Trendit",
            "ideas": "💡 Viraali Ideat & Koukut",
            "scripts": "✍️ Käsikirjoitukset & Shorts",
            "thumbnails": "🎯 Pienoiskuvat (Thumbnails)",
            "seo": "🏷️ Tunnisteet & SEO",
            "comments": "💬 Kommenttiavustaja",
            "repurpose": "♻️ Sisällön Kierrättäjä",
            "sponsorship": "🤝 Sponsorointipitchit"
        },
        "tools_advanced": {
            "translator": "🌍 Globaali Kääntäjä",
            "competitor": "🏆 Kilpailija-analyysi",
            "bulk": "⚡ Massamuokkaus",
            "analytics": "📈 Data & Analytiikka",
            "branding": "🎨 Kanavan Brändäys",
            "timestamps": "⏱️ Aikaleimat & Luvut",
            "title_matrix": "🧠 Otsikko A/B Matriisi",
            "ai_images": "🎨 Tekoälyn Kuvapromptit",
            "voice": "🎙️ Puhe- & Ääniohjaus",
            "simulator": "💰 Kasvu- & ROI Simulaattori"
        },
        "content": {
            "search": {"title": "📊 Perushaku & Trendit", "desc": "Hae hakusanoja, tutki trendejä ja arvioi ansioita tekoälyn avulla.", "input": "🔍 Kirjoita hakusana tai aihe:", "btn": "Hae & Analysoi", "spinner": "Analysoidaan hakusanaa '{keyword}' tekoälyn avulla..."},
            "ideas": {"title": "💡 Viraalit Ideat & Koukut", "input": "Aihepiiri / Niche:", "btn": "Generoi", "spinner": "Generoidaan..."},
            "scripts": {"title": "✍️ Käsikirjoitukset & Shorts", "input": "Videon aihe:", "btn": "Kirjoita skripti", "spinner": "Kirjoitetaan käsikirjoitusta..."},
            "thumbnails": {"title": "🎯 Pienoiskuvat (Thumbnails)", "input": "Videon ydinidea:", "btn": "Suunnittele pienoiskuva", "spinner": "Suunnitellaan visuaalista reseptiä..."},
            "seo": {"title": "🏷️ SEO & Tunnisteet", "input": "Aihe SEO-tunnisteille:", "btn": "Generoi tunnisteet", "spinner": "Haetaan optimoituja tunnisteita..."},
            "comments": {"title": "💬 Kommenttiavustaja", "input": "Katsojan kommentti:", "btn": "Kirjoita vastaus", "spinner": "Kirjoitetaan vastausta..."},
            "repurpose": {"title": "♻️ Sisällön kierrätys", "input": "Videokäsikirjoitus tai teksti:", "btn": "Kierrätä", "spinner": "Muokataan sisältöä..."},
            "sponsorship": {"title": "🤝 Sponsorointiviestit", "input_brand": "Brändin nimi:", "input_stats": "Kanavasi tilastot / niche:", "btn": "Kirjoita pitch", "spinner": "Kirjoitetaan sähköpostia..."},
            "translator": {"title": "🌍 Globaali Kääntäjä & Lokalisoija", "input": "Käännettävä teksti:", "btn": "Käännä", "spinner": "Käännetään..."},
            "competitor": {"title": "🏆 Kilpailija-analyysi", "input": "Aihe tai kilpailijoiden tyyli:", "btn": "Analysoi aukot", "spinner": "Analysoidaan..."},
            "bulk": {"title": "⚡ Massamuokkaus-työkalut", "input": "Kanavasi aihe:", "btn": "Luo massapohja", "spinner": "Luodaan..."},
            "analytics": {"title": "📈 Data & Analytiikka", "btn": "Analysoi mittarit", "spinner": "Analysoidaan tilastoja..."},
            "branding": {"title": "🎨 Kanavan Brändäys", "input": "Intohimosi / aihealue:", "btn": "Luo brändäyspaketti", "spinner": "Suunnitellaan..."},
            "timestamps": {"title": "⏱️ Aikaleimat & Luvut", "input": "Käsikirjoitus:", "btn": "Generoi aikaleimat", "spinner": "Luodaan lukuja..."},
            "title_matrix": {"title": "🧠 Otsikko A/B Matriisi", "input": "Videon aihe / idea:", "btn": "Luo otsikkomatriisi", "spinner": "Luodaan..."},
            "ai_images": {"title": "🎨 Tekoälyn Kuvapromptit", "input": "Pienoiskuvan aihe:", "btn": "Luo promptit", "spinner": "Muotoillaan prompteja..."},
            "voice": {"title": "🎙️ Puhe- & Ääniohjaus", "input": "Raakateksti:", "btn": "Optimoi puheelle", "spinner": "Muokataan..."},
            "simulator": {"title": "💰 Kasvu- & ROI Simulaattori", "sub1": "Nykyiset tilaajat:", "sub2": "Keskimääräiset katselukerrat per video:", "btn": "Simuloi kasvu", "spinner": "Lasketaan ennustetta..."}
        }
    }
}

if lang_code not in translations:
    lang_code = "🇬🇧"

texts = translations[lang_code]
c_texts = texts["content"]

# Salasana-tarkistus (Asiakkaat syöttävät tähän kuitista saadun salasanan)
str_module.sidebar.markdown("---")
str_module.sidebar.subheader(texts["dev_access"])
entered_password = str_module.sidebar.text_input(texts["pass_label"], type="password")
is_pro = (entered_password == "tubepro2026")
if is_pro:
    str_module.sidebar.success(texts["success_pro"])

# Kanavan asetukset sivupalkissa
str_module.sidebar.markdown("---")
str_module.sidebar.header(texts["settings"])
video_length = str_module.sidebar.selectbox(texts["v_len"], ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = str_module.sidebar.selectbox(texts["aud"], ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- PÄÄVALIKKO ---
str_module.markdown(f"### {texts['nav_title']}")

category_choice = str_module.radio(texts["cat_label"], [texts["cat_basics"], texts["cat_advanced"]], horizontal=True)

if category_choice == texts["cat_basics"]:
    tool_dict = texts["tools_basics"]
else:
    tool_dict = texts["tools_advanced"]

selected_tool_label = str_module.selectbox(texts["tool_prompt"], list(tool_dict.values()))
menu_choice = [k for k, v in tool_dict.items() if v == selected_tool_label][0]

str_module.markdown("---")

def render_paywall():
    str_module.warning(texts["paywall"])
    str_module.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">{texts["unlock_all"]}</a>', unsafe_allow_html=True)

# ==========================================
# TYÖKALUJEN LOGIIKKA
# ==========================================

if menu_choice == "search":
    str_module.title(c_texts["search"]["title"])
    str_module.markdown(c_texts["search"]["desc"])
    keyword = str_module.text_input(c_texts["search"]["input"])
    
    if str_module.button(c_texts["search"]["btn"], type="primary"):
        if keyword:
            if not client:
                str_module.error("OpenAI API key is missing!")
            else:
                with str_module.spinner(c_texts["search"]["spinner"].format(keyword=keyword)):
                    try:
                        res = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {
                                    "role": "system", 
                                    "content": f"You are a YouTube analytics expert. Respond in {selected_language}. Provide a realistic estimate for the given keyword in this exact format:\nHAUT: [estimated monthly searches, e.g. ~12,000]\nKILPAILU: [competition level, e.g. Low / Medium / High]\nRPM: [estimated RPM, e.g. $3.50]\nANALYysi: [Brief 2-sentence strategic insight about this keyword]"
                                },
                                {
                                    "role": "user", 
                                    "content": f"Analyze keyword: '{keyword}'"
                                }
                            ],
                            temperature=0.7
                        )
                        
                        raw_response = res.choices[0].message.content
                        haut, kilpailu, rpm, analyysi = "~10,000", "Medium", "$3.00", raw_response
                        
                        lines = raw_response.split('\n')
                        for line in lines:
                            if "HAUT:" in line:
                                haut = line.split("HAUT:")[1].strip()
                            elif "KILPAILU:" in line:
                                kilpailu = line.split("KILPAILU:")[1].strip()
                            elif "RPM:" in line:
                                rpm = line.split("RPM:")[1].strip()
                            elif "ANALYysi:" in line or "ANALYYSISI:" in line or "ANALYYSI:" in line:
                                analyysi = line.split(":", 1)[1].strip()

                        str_module.success(f"Results for keyword: **{keyword}**")
                        
                        col1, col2, col3 = str_module.columns(3)
                        col1.metric("🔍 Est. Monthly Searches", haut)
                        col2.metric("⚔️ Competition Level", kilpailu)
                        col3.metric("💵 Estimated RPM", rpm)
                        
                        str_module.markdown("### 💡 Strategic Insight")
                        str_module.info(analyysi)
                        
                    except Exception as e:
                        str_module.error(f"AI Search error: {e}")
        else:
            str_module.warning("Please enter a keyword first.")

elif menu_choice == "ideas":
    str_module.title(c_texts["ideas"]["title"])
    if not is_pro: render_paywall()
    elif client:
        niche = str_module.text_input(c_texts["ideas"]["input"])
        if str_module.button(c_texts["ideas"]["btn"], type="primary") and niche:
            with str_module.spinner(c_texts["ideas"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a top YouTube strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create viral concepts or hooks for niche '{niche}' tailored for {video_length}."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "scripts":
    str_module.title(c_texts["scripts"]["title"])
    if not is_pro: render_paywall()
    elif client:
        topic = str_module.text_input(c_texts["scripts"]["input"])
        if str_module.button(c_texts["scripts"]["btn"], type="primary") and topic:
            with str_module.spinner(c_texts["scripts"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a professional YouTube scriptwriter. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a full video script for {video_length} about '{topic}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "thumbnails":
    str_module.title(c_texts["thumbnails"]["title"])
    if not is_pro: render_paywall()
    elif client:
        topic = str_module.text_input(c_texts["thumbnails"]["input"])
        if str_module.button(c_texts["thumbnails"]["btn"], type="primary") and topic:
            with str_module.spinner(c_texts["thumbnails"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube CTR and design expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 high-CTR thumbnail design concepts for '{topic}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "seo":
    str_module.title(c_texts["seo"]["title"])
    if not is_pro: render_paywall()
    elif client:
        topic = str_module.text_input(c_texts["seo"]["input"])
        if str_module.button(c_texts["seo"]["btn"], type="primary") and topic:
            with str_module.spinner(c_texts["seo"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube SEO expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Provide comma-separated SEO tags for '{topic}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "comments":
    str_module.title(c_texts["comments"]["title"])
    if not is_pro: render_paywall()
    elif client:
        comment = str_module.text_area(c_texts["comments"]["input"])
        if str_module.button(c_texts["comments"]["btn"], type="primary") and comment:
            with str_module.spinner(c_texts["comments"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a friendly YouTube creator. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write an engaging reply to: '{comment}'"}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "repurpose":
    str_module.title(c_texts["repurpose"]["title"])
    if not is_pro: render_paywall()
    elif client:
        content = str_module.text_area(c_texts["repurpose"]["input"])
        target = str_module.selectbox("Convert to format:", ["X (Twitter) Thread", "Community Post", "Newsletter"])
        if str_module.button(c_texts["repurpose"]["btn"], type="primary") and content:
            with str_module.spinner(c_texts["repurpose"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a content strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Convert this text into a {target}: '{content}'"}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "sponsorship":
    str_module.title(c_texts["sponsorship"]["title"])
    if not is_pro: render_paywall()
    elif client:
        brand = str_module.text_input(c_texts["sponsorship"]["input_brand"])
        stats = str_module.text_input(c_texts["sponsorship"]["input_stats"])
        if str_module.button(c_texts["sponsorship"]["btn"], type="primary") and brand:
            with str_module.spinner(c_texts["sponsorship"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a talent manager. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a sponsorship pitch email to '{brand}' for channel stats: '{stats}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "translator":
    str_module.title(c_texts["translator"]["title"])
    if not is_pro: render_paywall()
    elif client:
        txt = str_module.text_area(c_texts["translator"]["input"])
        t_lang = str_module.selectbox("Target Language:", ["English", "Spanish", "German", "French", "Japanese"])
        if str_module.button(c_texts["translator"]["btn"], type="primary") and txt:
            with str_module.spinner(c_texts["translator"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional localization expert."},
                        {"role": "user", "content": f"Translate and optimize for YouTube in {t_lang}: '{txt}'"}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "competitor":
    str_module.title(c_texts["competitor"]["title"])
    if not is_pro: render_paywall()
    elif client:
        comp_topic = str_module.text_input(c_texts["competitor"]["input"])
        if str_module.button(c_texts["competitor"]["btn"], type="primary") and comp_topic:
            with str_module.spinner(c_texts["competitor"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube growth strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Perform a competitive audit for topic '{comp_topic}' and find a unique angle."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "bulk":
    str_module.title(c_texts["bulk"]["title"])
    if not is_pro: render_paywall()
    elif client:
        niche_b = str_module.text_input(c_texts["bulk"]["input"])
        if str_module.button(c_texts["bulk"]["btn"], type="primary") and niche_b:
            with str_module.spinner(c_texts["bulk"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an automation expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create reusable description template and tags strategy for niche '{niche_b}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "analytics":
    str_module.title(c_texts["analytics"]["title"])
    if not is_pro: render_paywall()
    elif client:
        c1, c2 = str_module.columns(2)
        ctr = c1.text_input("CTR %", "5.0%")
        avd = c2.text_input("Average View Duration", "3:30")
        if str_module.button(c_texts["analytics"]["btn"], type="primary"):
            with str_module.spinner(c_texts["analytics"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube data scientist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Analyze stats: CTR {ctr}, AVD {avd}. Give growth advice."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "branding":
    str_module.title(c_texts["branding"]["title"])
    if not is_pro: render_paywall()
    elif client:
        interests = str_module.text_input(c_texts["branding"]["input"])
        if str_module.button(c_texts["branding"]["btn"], type="primary") and interests:
            with str_module.spinner(c_texts["branding"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a brand director. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create channel names, slogans, and visual ideas for: '{interests}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "timestamps":
    str_module.title(c_texts["timestamps"]["title"])
    if not is_pro: render_paywall()
    elif client:
        script_txt = str_module.text_area(c_texts["timestamps"]["input"])
        if str_module.button(c_texts["timestamps"]["btn"], type="primary") and script_txt:
            with str_module.spinner(c_texts["timestamps"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a video editor. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create timestamp chapters starting at 00:00 for: '{script_txt}'"}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "title_matrix":
    str_module.title(c_texts["title_matrix"]["title"])
    if not is_pro: render_paywall()
    elif client:
        top = str_module.text_input(c_texts["title_matrix"]["input"])
        if str_module.button(c_texts["title_matrix"]["btn"], type="primary") and top:
            with str_module.spinner(c_texts["title_matrix"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a copywriting expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 10 psychological angles for titles based on topic '{top}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "ai_images":
    str_module.title(c_texts["ai_images"]["title"])
    if not is_pro: render_paywall()
    elif client:
        img_t = str_module.text_input(c_texts["ai_images"]["input"])
        if str_module.button(c_texts["ai_images"]["btn"], type="primary") and img_t:
            with str_module.spinner(c_texts["ai_images"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an AI prompt engineer. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 image generation prompts for thumbnail about '{img_t}'."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "voice":
    str_module.title(c_texts["voice"]["title"])
    if not is_pro: render_paywall()
    elif client:
        v_txt = str_module.text_area(c_texts["voice"]["input"])
        if str_module.button(c_texts["voice"]["btn"], type="primary") and v_txt:
            with str_module.spinner(c_texts["voice"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a voiceover coach. Respond in {selected_language}."},
                        {"role": "user", "content": f"Rewrite for natural speech delivery with pauses: '{v_txt}'"}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)

elif menu_choice == "simulator":
    str_module.title(c_texts["simulator"]["title"])
    if not is_pro: 
        render_paywall()
    elif client:
        subs = str_module.number_input(c_texts["simulator"]["sub1"], min_value=0, value=1000)
        views = str_module.number_input(c_texts["simulator"]["sub2"], min_value=0, value=5000)
        if str_module.button(c_texts["simulator"]["btn"], type="primary"):
            with str_module.spinner(c_texts["simulator"]["spinner"]):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube financial analyst. Respond in {selected_language}."},
                        {"role": "user", "content": f"Simulate channel growth and estimated revenue for current subs: {subs}, average views: {views}."}
                    ],
                    temperature=0.7
                )
                str_module.success("Done!")
                str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)
