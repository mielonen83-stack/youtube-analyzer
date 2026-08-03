import streamlit as st
from openai import OpenAI

# Sivun asetukset
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# --- KUSTOMOITU CSS ---
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

# OpenAI Client alustus
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# Stripe-maksulinkki
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"

# --- SIVUPALKKI (Sidebar) ---
st.sidebar.markdown("### 🚀 YouTube Pro Suite")
st.sidebar.write("Avaa kaikki tekoälytyökalut ja rajoittamaton haku!")
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Hanki Pro-oikeudet (9 €)</a>', unsafe_allow_html=True)

# Kielen valinta
st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Language / Kieli")
selected_language = st.sidebar.selectbox("Valitse kieli:", [
    "🇫🇮 Suomi", 
    "🇬🇧 English", 
    "🇸🇪 Svenska", 
    "🇪🇸 Español", 
    "🇩🇪 Deutsch", 
    "🇫🇷 Français", 
    "🇯🇵 日本語"
])
lang_code = selected_language.split()[0]

# --- KIELIAVAIMET JA KÄÄNNÖKSET ---
texts = {
    "🇫🇮": {
        "dev_access": "🔐 Kehittäjä / Omistaja",
        "pass_label": "Syötä Pro-salasana:",
        "success_pro": "✅ Pro-oikeudet avattu (Dev Mode)",
        "settings": "⚙️ Sisällöntuottajan Asetukset",
        "v_len": "Videon pituus / Tyyppi",
        "aud": "Kohdeyleisö",
        "paywall": "🔒 **Pro-ominaisuus:** Tarvitset Pro-oikeudet käyttääksesi tätä työkalua.",
        "unlock_all": "🔥 Avaa kaikki työkalut hintaan 9 €",
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
        }
    },
    "🇬🇧": {
        "dev_access": "🔐 Developer / Owner Access",
        "pass_label": "Enter Pro Password:",
        "success_pro": "✅ Pro Access Unlocked (Dev Mode)",
        "settings": "⚙️ Creator Settings",
        "v_len": "Video Length / Type",
        "aud": "Target Audience",
        "paywall": "🔒 **Pro Feature:** You need Pro Access to use this tool.",
        "unlock_all": "🔥 Unlock All Tools for 9 €",
        "nav_title": "🛠️ Tools Navigation",
        "cat_label": "Select category:",
        "cat_basics": "💡 Basics, Ideas & Scripts",
        "cat_advanced": "🚀 Advanced SEO, Growth & Analytics",
        "tool_prompt": "Select tool:",
        "tools_basics": {
            "search": "📊 Basic Search",
            "ideas": "💡 Ideas & Hooks",
            "scripts": "✍️ Scripts & Shorts",
            "thumbnails": "🎯 Thumbnails",
            "seo": "🏷️ SEO & Tags",
            "comments": "💬 Comments",
            "repurpose": "♻️ Repurpose",
            "sponsorship": "🤝 Sponsorship"
        },
        "tools_advanced": {
            "translator": "🌍 Translator",
            "competitor": "🏆 Competitor Audit",
            "bulk": "⚡ Bulk Edit Tools",
            "analytics": "📈 Data & Analytics",
            "branding": "🎨 Channel Branding",
            "timestamps": "⏱️ Timestamp Generator",
            "title_matrix": "🧠 Title A/B Matrix",
            "ai_images": "🎨 AI Image Prompts",
            "voice": "🎙️ Script Voice Optimizer",
            "simulator": "💰 Growth & ROI Simulator"
        }
    }
}.get(lang_code, {
    "dev_access": "🔐 Developer / Owner Access",
    "pass_label": "Enter Pro Password:",
    "success_pro": "✅ Pro Access Unlocked (Dev Mode)",
    "settings": "⚙️ Creator Settings",
    "v_len": "Video Length / Type",
    "aud": "Target Audience",
    "paywall": "🔒 **Pro Feature:** You need Pro Access to use this tool.",
    "unlock_all": "🔥 Unlock All Tools for 9 €",
    "nav_title": "🛠️ Tools Navigation",
    "cat_label": "Select category:",
    "cat_basics": "💡 Basics, Ideas & Scripts",
    "cat_advanced": "🚀 Advanced SEO, Growth & Analytics",
    "tool_prompt": "Select tool:",
    "tools_basics": {
        "search": "📊 Basic Search", "ideas": "💡 Ideas & Hooks", "scripts": "✍️ Scripts & Shorts", 
        "thumbnails": "🎯 Thumbnails", "seo": "🏷️ SEO & Tags", "comments": "💬 Comments", 
        "repurpose": "♻️ Repurpose", "sponsorship": "🤝 Sponsorship"
    },
    "tools_advanced": {
        "translator": "🌍 Translator", "competitor": "🏆 Competitor Audit", "bulk": "⚡ Bulk Edit Tools", 
        "analytics": "📈 Data & Analytics", "branding": "🎨 Channel Branding", "timestamps": "⏱️ Timestamp Generator", 
        "title_matrix": "🧠 Title A/B Matrix", "ai_images": "🎨 AI Image Prompts", "voice": "🎙️ Script Voice Optimizer", 
        "simulator": "💰 Growth & ROI Simulator"
    }
})

# Salasana-tarkistus (Dev mode)
st.sidebar.markdown("---")
st.sidebar.subheader(texts["dev_access"])
entered_password = st.sidebar.text_input(texts["pass_label"], type="password")
is_pro = (entered_password == "tubepro2026")
if is_pro:
    st.sidebar.success(texts["success_pro"])

# Kanavan asetukset sivupalkissa
st.sidebar.markdown("---")
st.sidebar.header(texts["settings"])
video_length = st.sidebar.selectbox(texts["v_len"], ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox(texts["aud"], ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- PÄÄVALIKKO ---
st.markdown(f"### {texts['nav_title']}")

category_choice = st.radio(texts["cat_label"], [texts["cat_basics"], texts["cat_advanced"]], horizontal=True)

if category_choice == texts["cat_basics"]:
    tool_dict = texts["tools_basics"]
else:
    tool_dict = texts["tools_advanced"]

selected_tool_label = st.selectbox(texts["tool_prompt"], list(tool_dict.values()))
# Muunnetaan valittu teksti takaisin tunnisteeksi (key)
menu_choice = [k for k, v in tool_dict.items() if v == selected_tool_label][0]

st.markdown("---")

def render_paywall():
    st.warning(texts["paywall"])
    st.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">{texts["unlock_all"]}</a>', unsafe_allow_html=True)

# ==========================================
# TYÖKALUJEN LOGIIKKA
# ==========================================

if menu_choice == "search":
    st.title("🎬 Perushaku & Trendit")
    st.markdown("Hae hakusanoja, tutki trendejä ja arvioi ansioita tekoälyn avulla.")
    keyword = st.text_input("🔍 Kirjoita hakusana tai aihe:")
    if st.button("Hae & Analysoi", type="primary"):
        if keyword and client:
            with st.spinner(f"Analysoidaan hakusanaa '{keyword}'..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube analytics expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Provide estimated metrics for keyword '{keyword}': monthly searches, competition level, estimated RPM, and brief strategic insight."}
                    ],
                    temperature=0.7
                )
                st.success("Analyysi valmis:")
                col1, col2, col3 = st.columns(3)
                col1.metric("Haut / kk (AI)", "~45,000", "+10%")
                col2.metric("Kilpailu (AI)", "Keskitaso", "Vakaa")
                col3.metric("Arvioitu RPM (AI)", "$4.50", "+$0.2")
                st.write(res.choices[0].message.content)
        else:
            st.warning("Syötä hakusana.")

elif menu_choice == "ideas":
    st.title("💡 Viraalit Ideat & Koukut")
    if not is_pro: render_paywall()
    elif client:
        sub = st.selectbox("Valitse toiminto:", ["Ideageneraattori", "3 sekunnin koukut"])
        niche = st.text_input("Aihepiiri / Niche:")
        if st.button("Generoi", type="primary") and niche:
            with st.spinner("Generoidaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a top YouTube strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create viral concepts or hooks for niche '{niche}' tailored for {video_length}."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "scripts":
    st.title("✍️ Käsikirjoitukset & Shorts")
    if not is_pro: render_paywall()
    elif client:
        topic = st.text_input("Videon aihe:")
        if st.button("Kirjoita skripti", type="primary") and topic:
            with st.spinner("Kirjoitetaan käsikirjoitusta..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a professional YouTube scriptwriter. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a full video script for {video_length} about '{topic}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "thumbnails":
    st.title("🎯 Pienoiskuvat (Thumbnails)")
    if not is_pro: render_paywall()
    elif client:
        topic = st.text_input("Videon ydinidea:")
        if st.button("Suunnittele pienoiskuva", type="primary") and topic:
            with st.spinner("Suunnitellaan visuaalista reseptiä..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube CTR and design expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 high-CTR thumbnail design concepts for '{topic}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "seo":
    st.title("🏷️ SEO & Tunnisteet")
    if not is_pro: render_paywall()
    elif client:
        topic = st.text_input("Aihe SEO-tunnisteille:")
        if st.button("Generoi tunnisteet", type="primary") and topic:
            with st.spinner("Haetaan optimoituja tunnisteita..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube SEO expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Provide comma-separated SEO tags for '{topic}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "comments":
    st.title("💬 Kommenttiavustaja")
    if not is_pro: render_paywall()
    elif client:
        comment = st.text_area("Katsojan kommentti:")
        if st.button("Kirjoita vastaus", type="primary") and comment:
            with st.spinner("Kirjoitetaan vastausta..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a friendly YouTube creator. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write an engaging reply to: '{comment}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "repurpose":
    st.title("♻️ Sisällön kierrätys")
    if not is_pro: render_paywall()
    elif client:
        content = st.text_area("Videokäsikirjoitus tai teksti:")
        target = st.selectbox("Muunna muotoon:", ["X (Twitter) -ketju", "Yhteisöpostaus", "Uutiskirje"])
        if st.button("Kierrätä", type="primary") and content:
            with st.spinner("Muokataan sisältöä..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a content strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Convert this text into a {target}: '{content}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "sponsorship":
    st.title("🤝 Sponsorointiviestit")
    if not is_pro: render_paywall()
    elif client:
        brand = st.text_input("Brändin nimi:")
        stats = st.text_input("Kanavasi tilastot / niche:")
        if st.button("Kirjoita pitch", type="primary") and brand:
            with st.spinner("Kirjoitetaan sähköpostia..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a talent manager. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a sponsorship pitch email to '{brand}' for channel stats: '{stats}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "translator":
    st.title("🌍 Globaali Kääntäjä & Lokalisoija")
    if not is_pro: render_paywall()
    elif client:
        txt = st.text_area("Käännettävä teksti:")
        t_lang = st.selectbox("Kohdekieli:", ["Englanti", "Espanja", "Saksa", "Ranska", "Japani"])
        if st.button("Käännä", type="primary") and txt:
            with st.spinner("Käännetään..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional localization expert."},
                        {"role": "user", "content": f"Translate and optimize for YouTube in {t_lang}: '{txt}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "competitor":
    st.title("🏆 Kilpailija-analyysi")
    if not is_pro: render_paywall()
    elif client:
        comp_topic = st.text_input("Aihe tai kilpailijoiden tyyli:")
        if st.button("Analysoi aukot", type="primary") and comp_topic:
            with st.spinner("Analysoidaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube growth strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Perform a competitive audit for topic '{comp_topic}' and find a unique angle."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "bulk":
    st.title("⚡ Massamuokkaus-työkalut")
    if not is_pro: render_paywall()
    elif client:
        niche_b = st.text_input("Kanavasi aihe:")
        if st.button("Luo massapohja", type="primary") and niche_b:
            with st.spinner("Luodaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an automation expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create reusable description template and tags strategy for niche '{niche_b}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "analytics":
    st.title("📈 Data & Analytiikka")
    if not is_pro: render_paywall()
    elif client:
        c1, c2 = st.columns(2)
        ctr = c1.text_input("CTR %", "5.0%")
        avd = c2.text_input("Katseluaika", "3:30")
        if st.button("Analysoi mittarit", type="primary"):
            with st.spinner("Analysoidaan tilastoja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube data scientist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Analyze stats: CTR {ctr}, AVD {avd}. Give growth advice."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "branding":
    st.title("🎨 Kanavan Brändäys")
    if not is_pro: render_paywall()
    elif client:
        interests = st.text_input("Intohimosi / aihealue:")
        if st.button("Luo brändäyspaketti", type="primary") and interests:
            with st.spinner("Suunnitellaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a brand director. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create channel names, slogans, and visual ideas for: '{interests}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "timestamps":
    st.title("⏱️ Aikaleimat & Luvut")
    if not is_pro: render_paywall()
    elif client:
        script_txt = st.text_area("Käsikirjoitus:")
        if st.button("Generoi aikaleimat", type="primary") and script_txt:
            with st.spinner("Luodaan lukuja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a video editor. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create timestamp chapters starting at 00:00 for: '{script_txt}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "title_matrix":
    st.title("🧠 Otsikko A/B Matriisi")
    if not is_pro: render_paywall()
    elif client:
        top = st.text_input("Videon aihe / idea:")
        if st.button("Luo otsikkomatriisi", type="primary") and top:
            with st.spinner("Luodaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a copywriting expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 10 psychological angles for titles based on topic '{top}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "ai_images":
    st.title("🎨 Tekoälyn Kuvapromptit")
    if not is_pro: render_paywall()
    elif client:
        img_t = st.text_input("Pienoiskuvan aihe:")
        if st.button("Luo promptit", type="primary") and img_t:
            with st.spinner("Muotoillaan prompteja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an AI prompt engineer. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 image generation prompts for thumbnail about '{img_t}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "voice":
    st.title("🎙️ Puhe- & Ääniohjaus")
    if not is_pro: render_paywall()
    elif client:
        v_txt = st.text_area("Raakateksti:")
        if st.button("Optimoi puheelle", type="primary") and v_txt:
            with st.spinner("Muokataan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a voiceover coach. Respond in {selected_language}."},
                        {"role": "user", "content": f"Rewrite for natural speech delivery with pauses: '{v_txt}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

elif menu_choice == "simulator":
    st.title("💰 Kasvu- & ROI Simulaattori")
    if not is_pro: render_paywall()
    else:
        v_count = st.number_input("Odotetut katselukerrat", value=10000, step=1000)
        rpm_val = st.slider("RPM ($)", 0.5, 30.0, 4.5)
        if st.button("Laske simulaatio", type="primary"):
            earnings = (v_count / 1000) * rpm_val
            st.success("Simulaatio valmis!")
            st.metric("Arvioidut mainostulot", f"${earnings:.2f}")
            if client:
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a growth economist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Give strategic advice for {v_count} views generating ${earnings:.2f}."}
                    ],
                    temperature=0.7
                )
                st.write(res.choices[0].message.content)
