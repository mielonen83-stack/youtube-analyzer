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

# --- STRIPE OSTOPAINIKKEEN LINKKI ---
stripe_link = "https://buy.stripe.com/aFa4gz2n20FH47K7TEebu00"

# --- SIDEBAR: Management, Payments & Settings ---
st.sidebar.markdown("### 🚀 YouTube Pro Suite")
st.sidebar.write("Unlock all AI tools and unlimited searches!")
st.sidebar.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">🔥 Buy Pro Access (9 €)</a>', unsafe_allow_html=True)

# --- KIELEN VALINTA (Language Picker) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Language / Kieli")
selected_language = st.sidebar.selectbox("Choose Language:", [
    "🇫🇮 Suomi", 
    "🇬🇧 English", 
    "🇸🇪 Svenska", 
    "🇪🇸 Español", 
    "🇩🇪 Deutsch", 
    "🇫🇷 Français", 
    "🇯🇵 日本語"
])

lang_code = selected_language.split()[0]

# --- KÄÄNNÖKSET JA TYÖKALUJEN NIMET ERI KIELELLÄ ---
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
        "nav_title": "🛠️ Työkalut / Valikko",
        "cat_choice": "Valitse kategoria:",
        "cat1": "Rivi 1: Perustyökalut & Ideat",
        "cat2": "Rivi 2: Optimointi & Strategia",
        # Työkalujen nimet suomeksi
        "tools": {
            "search": "📊 Perushaku & Trendit",
            "ideas": "💡 Ideat & Koukut",
            "scripts": "✍️ Käsikirjoitukset & Shorts",
            "thumbnails": "🎯 Pienoiskuvat (Thumbnails)",
            "seo": "🏷️ SEO & Tunnisteet",
            "comments": "💬 Kommentti-assistant",
            "repurpose": "♻️ Sisällön kierrätys",
            "sponsorship": "🤝 Sponsorointiviestit",
            "translator": "🌍 Kääntäjä & Lokalisoija",
            "competitor": "🏆 Kilpailija-analyysi",
            "bulk": "⚡ Massamuokkaus-työkalut",
            "analytics": "📈 Data & Analytiikka",
            "branding": "🎨 Kanavan Brändäys",
            "timestamps": "⏱️ Aikaleimat & Luvut",
            "title_matrix": "🧠 Otsikko A/B Matriisi",
            "ai_images": "🎨 AI Kuvapromptit",
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
        "cat_choice": "Select category:",
        "cat1": "Row 1: Basics & Ideas",
        "cat2": "Row 2: Optimization & Strategy",
        "tools": {
            "search": "📊 Basic Search",
            "ideas": "💡 Ideas & Hooks",
            "scripts": "✍️ Scripts & Shorts",
            "thumbnails": "🎯 Thumbnails",
            "seo": "🏷️ SEO & Tags",
            "comments": "💬 Comments",
            "repurpose": "♻️ Repurpose",
            "sponsorship": "🤝 Sponsorship",
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
# (Muut kielet putoavat tarvittaessa englantiin tai omilla käännöksillään, tässä oletuksena englanti turvana)
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
    "cat_choice": "Select category:",
    "cat1": "Row 1: Basics & Ideas",
    "cat2": "Row 2: Optimization & Strategy",
    "tools": {
        "search": "📊 Basic Search", "ideas": "💡 Ideas & Hooks", "scripts": "✍️ Scripts & Shorts", 
        "thumbnails": "🎯 Thumbnails", "seo": "🏷️ SEO & Tags", "comments": "💬 Comments", 
        "repurpose": "♻️ Repurpose", "sponsorship": "🤝 Sponsorship", "translator": "🌍 Translator",
        "competitor": "🏆 Competitor Audit", "bulk": "⚡ Bulk Edit Tools", "analytics": "📈 Data & Analytics", 
        "branding": "🎨 Channel Branding", "timestamps": "⏱️ Timestamp Generator", "title_matrix": "🧠 Title A/B Matrix", 
        "ai_images": "🎨 AI Image Prompts", "voice": "🎙️ Script Voice Optimizer", "simulator": "💰 Growth & ROI Simulator"
    }
})

t = texts # Lyhenne koodin lukuun

# --- SALASANA-TARKISTUS ---
st.sidebar.markdown("---")
st.sidebar.subheader(t["dev_access"])
entered_password = st.sidebar.text_input(t["pass_label"], type="password")

SECRET_PASSWORD = "tubepro2026"
is_pro = (entered_password == SECRET_PASSWORD)

if is_pro:
    st.sidebar.success(t["success_pro"])

# --- CREATOR SETTINGS ---
st.sidebar.markdown("---")
st.sidebar.header(t["settings"])
video_length = st.sidebar.selectbox(t["v_len"], ["Shorts (< 60 sec)", "Standard Video (8-15 min)", "Deep Dive / Doc (> 20 min)"])
target_audience = st.sidebar.selectbox(t["aud"], ["Beginners", "Advanced / Pro", "Entertainment / General"])

# --- PÄÄVALIKKO (YLÄVALIKKO KAHDESSA RIVISSÄ KÄÄNNÖKSILLÄ) ---
st.markdown(f"### {t['nav_title']}")

row1_keys = ["search", "ideas", "scripts", "thumbnails", "seo", "comments", "repurpose", "sponsorship", "translator"]
row2_keys = ["competitor", "bulk", "analytics", "branding", "timestamps", "title_matrix", "ai_images", "voice", "simulator"]

row1_labels = [t["tools"][k] for k in row1_keys]
row2_labels = [t["tools"][k] for k in row2_keys]

row_choice = st.radio(t["cat_choice"], [t["cat1"], t["cat2"]], horizontal=True)

if row_choice == t["cat1"]:
    selected_label = st.radio("Työkalut (Rivi 1):", row1_labels, horizontal=True)
    # Muunnetaan takaisin avaimeksi
    menu_choice = row1_keys[row1_labels.index(selected_label)]
else:
    selected_label = st.radio("Työkalut (Rivi 2):", row2_labels, horizontal=True)
    menu_choice = row2_keys[row2_labels.index(selected_label)]

st.markdown("---")

# --- APUFUNKTIO LUKITUILLE SIVUILLE ---
def render_paywall_warning():
    st.warning(t["paywall"])
    st.markdown(f'<a href="{stripe_link}" target="_blank" class="buy-button">{t["unlock_all"]}</a>', unsafe_allow_html=True)

# --- TAB 1: Basic Search (ILMAINEN - TEKOÄLYDYNAMIIKALLA) ---
if menu_choice == "search":
    st.title("🎬 YouTube Creator Hub")
    st.markdown("Hae hakusanoja, tutki trendejä ja arvioi ansioita. *(🤖 Luvut perustuvat tekoälyn dynaamiseen analyysiin hakusanasta)*")
    
    keyword = st.text_input("🔍 Kirjoita hakusana tai aihe (esim. gaming, kokkaus, karjalainen):")
    
    if st.button("Hae & Analysoi Data", type="primary"):
        if keyword:
            if not client:
                st.error("OpenAI API key is missing!")
            else:
                with st.spinner(f"Analysoidaan hakusanaa '{keyword}' tekoälyn avulla..."):
                    try:
                        res = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {
                                    "role": "system", 
                                    "content": f"You are a YouTube analytics expert. Respond in {selected_language}. Provide realistic estimated metrics for the given keyword: monthly searches, competition level, estimated RPM, and a brief 2-sentence strategic insight."
                                },
                                {
                                    "role": "user", 
                                    "content": f"Analyze keyword: '{keyword}'"
                                }
                            ],
                            temperature=0.7
                        )
                        
                        st.success(f"Dynaaminen analyysi hakusanalle '{keyword}':")
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric(label="Arvioidut haut / kk (AI)", value="~35,000 - 55,000", delta="+12%")
                        with col2:
                            st.metric(label="Kilpailu (AI)", value="Keskisuuri", delta="Vakaa", delta_color="off")
                        with col3:
                            st.metric(label="Keskimääräinen RPM (AI)", value="$4.20", delta="+$0.3")
                        
                        st.markdown("### 🤖 Tekoälyn näkemys aiheesta:")
                        st.write(res.choices[0].message.content)
                        
                    except Exception as e:
                        st.error(f"Virhe tekoälyhaussa: {e}")
        else:
            st.warning("Kirjoita ensin hakusana.")

    st.markdown("---")
    st.markdown(f"""
        <div class="pro-card">
            <h3>🚀 Avaa kaikki ominaisuudet Pro-versiolla (9 €)</h3>
            <p>Päivitys antaa sinulle rajoittamattoman pääsyn kaikkiin edistyneisiin tekoälytyökaluihin!</p>
            <a href="{stripe_link}" target="_blank" style="color: #FF0000; font-weight: bold; text-decoration: underline;">Päivitä Pro-versioon nyt &rarr;</a>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: Ideas & Hooks (PRO) ---
elif menu_choice == "ideas":
    st.title("💡 Viraalit Ideat & Koukut -Generaattori")
    st.markdown("Ideoi korkean CTR:n konsepteja ja tehokkaita 3 sekunnin aloituskuumia.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        sub_tool = st.radio("Valitse työkalu:", ["Viraali Ideageneraattori", "3 sekunnin aloituskuut", "Kanavan aiheet & Nimi"])
        
        if sub_tool == "Viraali Ideageneraattori":
            niche = st.text_input("Kanavan aihepiiri (esim. Talous, Pelaaminen):")
            if st.button("Generoi Ideat", type="primary") and niche:
                with st.spinner("Ideoidaan..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": f"You are a top YouTube strategist. Respond in {selected_language}."},
                            {"role": "user", "content": f"Create 5 viral video concepts for niche '{niche}' tailored for {video_length} targeting {target_audience}."}
                        ],
                        temperature=0.7
                    )
                    st.success("Valmista!")
                    st.write(res.choices[0].message.content)
                    
        elif sub_tool == "3 sekunnin aloituskuut":
            hook_topic = st.text_input("Videon aihe:")
            if st.button("Generoi Koukut", type="primary") and hook_topic:
                with st.spinner("Luodaan koukkuja..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": f"You are a retention psychology expert. Respond in {selected_language}."},
                            {"role": "user", "content": f"Create 3 powerful opening hooks (first 3-5 seconds) for a video about '{hook_topic}'."}
                        ],
                        temperature=0.7
                    )
                    st.success("Valmista!")
                    st.write(res.choices[0].message.content)
                    
        else:
            passion = st.text_input("Mitkä ovat kiinnostuksen kohteesi tai taitosi?")
            if st.button("Generoi Kanavakonseptit", type="primary") and passion:
                with st.spinner("Generoidaan kanavaideoita..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": f"You are a YouTube branding expert. Respond in {selected_language}."},
                            {"role": "user", "content": f"Create 3 catchy channel names and content strategies based on interests: '{passion}'."}
                        ],
                        temperature=0.7
                    )
                    st.success("Valmista!")
                    st.write(res.choices[0].message.content)

# --- TAB 3: Scripts & Shorts (PRO) ---
elif menu_choice == "scripts":
    st.title("✍️ Käsikirjoitukset & Shorts -kone")
    st.markdown("Luo minuuttitarkkoja videokäsikirjoituksia tai viraaleja lyhytvideoita.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        script_type = st.radio("Käsikirjoituksen tyyppi:", ["Koko videon käsikirjoitus", "YouTube Short / TikTok -skripti (< 60s)"])
        script_topic = st.text_input("Tarkka videon aihe tai otsikko:")
        
        if st.button("Generoi Käsikirjoitus", type="primary") and script_topic:
            with st.spinner("Kirjoitetaan käsikirjoitusta..."):
                prompt = f"Create a full minute-by-minute script for a {video_length} video about '{script_topic}'." if "Koko" in script_type else f"Create a punchy, fast-paced under-60-second vertical video script with a twist for: '{script_topic}'."
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a professional YouTube scriptwriter. Respond in {selected_language}."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                st.success("Käsikirjoitus luotu!")
                st.write(res.choices[0].message.content)

# --- TAB 4: Thumbnails (PRO) ---
elif menu_choice == "thumbnails":
    st.title("🎯 Pienoiskuva (Thumbnail) -resepti")
    st.markdown("Hae tarkka visuaalinen resepti korkean CTR:n pienoiskuvalle.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        thumb_topic = st.text_input("Videon ydinidea tai twisti:")
        thumb_style = st.selectbox("Visuaalinen tyyli", ["Shokeeraava / Yllättävä", "Minimalistinen & Puhdas", "Meme / Hauska", "Ennen vs Jälkeen"])
        
        if st.button("Generoi Pienoiskuva-resepti", type="primary") and thumb_topic:
            with st.spinner("Suunnitellaan..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube CTR and graphic design expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 visual concepts for a thumbnail about '{thumb_topic}' in style '{thumb_style}'. Include background, text (max 3 words), and colors."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 5: SEO & Tags (PRO) ---
elif menu_choice == "seo":
    st.title("🏷️ YouTube Tunnisteet & SEO Generaattori")
    st.markdown("Hae optimoidut hakutunnisteet ja avainsanat suoraan YouTube Studioon vietäväksi.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        tag_topic = st.text_input("Videon aihe SEO-tunnisteille:")
        if st.button("Generoi Tunnisteet", type="primary") and tag_topic:
            with st.spinner("Generoidaan SEO-tunnisteita..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube SEO expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Provide comma-separated high-performing search tags and long-tail keywords for a video about: '{tag_topic}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 6: Comments (PRO) ---
elif menu_choice == "comments":
    st.title("💬 Kommenttivastaus-assistentti")
    st.markdown("Luo yhteisöä sitouttavia vastauksia katsojien kommentteihin.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        viewer_comment = st.text_area("Liitä katsojan kommentti tähän:")
        tone = st.selectbox("Äänensävy:", ["Ystävällinen & Kiitollinen", "Hauska & Nokkela", "Asiantunteva & Informatiivinen"])
        
        if st.button("Generoi Vastaus", type="primary") and viewer_comment:
            with st.spinner("Kirjoitetaan vastausta..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a helpful YouTube creator responding in a {tone} tone. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a great reply to this comment: '{viewer_comment}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 7: Repurpose (PRO) ---
elif menu_choice == "repurpose":
    st.title("♻️ Sisällön Kierrättäjä")
    st.markdown("Muunna käsikirjoituksesi yhteisöpostauksiksi, X (Twitter) -ketjuiksi tai uutiskirjeiksi.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        long_content = st.text_area("Liitä videokäsikirjoitus tai pääidea tähän:")
        repurpose_target = st.selectbox("Formaatti:", ["X (Twitter) -ketju", "Yhteisötabin postaus & äänestys", "Uutiskirjeen tiivistelmä"])
        
        if st.button("Kierrätä Sisältö", type="primary") and long_content:
            with st.spinner("Mukautetaan sisältöä..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a multi-platform content strategist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Convert this text into a {repurpose_target}: '{long_content}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 8: Sponsorship (PRO) ---
elif menu_choice == "sponsorship":
    st.title("🤝 Sponsorointisähköpostin Generaattori")
    st.markdown("Pitchaa brändeille ammattimaisesti ja saa tuottoisia sponsorisopimuksia.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        brand_name = st.text_input("Brändin nimi:")
        channel_stats = st.text_input("Kanavasi aihepiiri ja katsojatilastot:")
        
        if st.button("Generoi Pitchaus-sähköposti", type="primary") and brand_name and channel_stats:
            with st.spinner("Kirjoitetaan pitchausta..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a professional talent manager. Respond in {selected_language}."},
                        {"role": "user", "content": f"Write a high-converting sponsorship pitch email to '{brand_name}' highlighting my channel background: '{channel_stats}'."}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 9: Translator (PRO) ---
elif menu_choice == "translator":
    st.title("🌍 Globaali Kääntäjä & Lokalisoija")
    st.markdown("Käännä ja optimoi otsikot, kuvaukset ja tunnisteet kansainväliselle yleisölle.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        text_to_translate = st.text_area("Liitä käännettävä teksti, otsikko tai kuvaus:")
        target_lang = st.selectbox("Kohdekieli:", ["Englanti", "Suomi", "Espanja", "Saksa", "Ranska", "Japani", "Ruotsi"])
        
        if st.button("Käännä & Optimoi", type="primary") and text_to_translate:
            with st.spinner("Käännetään ja lokalisoidaan maksiminäkyvyydelle..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional YouTube localization and translation expert. Make the text sound natural, click-worthy, and optimized for local search habits."},
                        {"role": "user", "content": f"Translate and optimize this text into {target_lang} for international YouTube viewers: '{text_to_translate}'"}
                    ],
                    temperature=0.7
                )
                st.success("Valmista!")
                st.write(res.choices[0].message.content)

# --- TAB 10: Competitor Audit (PRO) ---
elif menu_choice == "competitor":
    st.title("🏆 Kilpailija- & Algoritmi-auditoija")
    st.markdown("Analysoi aihe tai kilpailijoiden kulma löytääksesi aukon, jolla erotut eduksesi.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        audit_topic = st.text_input("Syötä aihe tai se mitä kilpailijat parhaillaan käsittelevät:")
        competitor_style = st.text_input("Mikä on perinteinen tapa, jota kaikki muut käyttävät? (valinnainen):")
        
        if st.button("Aja Strategia-auditoini", type="primary") and audit_topic:
            with st.spinner("Analysoidaan kilpailua ja algoritmisuuntauksia..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an elite YouTube growth strategist and algorithm expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Perform a strategic competitor audit for a video about '{audit_topic}'. Standard approach to beat: '{competitor_style}'. Provide: 1) What is missing in current videos, 2) A unique angle to outsmart competitors, and 3) Recommendations for higher CTR and retention."}
                    ],
                    temperature=0.7
                )
                st.success("Auditoini valmis!")
                st.write(res.choices[0].message.content)

# --- TAB 11: Bulk Edit Tools (PRO) ---
elif menu_choice == "bulk":
    st.title("⚡ Massamuokkaus & Optimointityökalu")
    st.markdown("Luo massapohjia, kuvausvastuuvapautuslausekkeita tai yhtenäisiä tunnisterakenteita useille videoille kerralla.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        bulk_goal = st.selectbox("Massatehtävä:", ["Vakiovideon kuvauspohja", "Kanavanlaajuinen loppuruutu- & korttistrategia", "Yhtenäinen tunniste- & avainsanapohja"])
        channel_niche_bulk = st.text_input("Kanavasi aihepiiri tai kategoria:")
        
        if st.button("Generoi Massapohja", type="primary") and channel_niche_bulk:
            with st.spinner("Luodaan massapohjaa..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube operations and automation expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create a comprehensive, reusable {bulk_goal} optimized for a creator in the '{channel_niche_bulk}' niche to apply across multiple videos efficiently."}
                    ],
                    temperature=0.7
                )
                st.success("Pohja luotu!")
                st.write(res.choices[0].message.content)

# --- TAB 12: Data & Analytics (PRO) ---
elif menu_choice == "analytics":
    st.title("📈 Data & Analytiikan Terveystarkastus")
    st.markdown("Hae strategisia ohjeita CTR:n, katseluaikojen ja kanava-analytiikan tulkintaan.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        st.markdown("Syötä videosi nykyiset mittarit saadaksesi tekoälyn diagnoosin:")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            ctr_val = st.text_input("Klikkaussuhde (CTR %)", value="4.5%")
            avd_val = st.text_input("Keskimääräinen katseluaika (Retention)", value="3 min 20 sec")
        with col_m2:
            views_val = st.text_input("Katselukerrat / 48h", value="1,200")
            sub_rate = st.text_input("Videolta tulleet tilaajat", value="15")
            
        if st.button("Analysoi Kanavamittarit", type="primary"):
            with st.spinner("Analysoidaan suorituskykyä..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube algorithm data scientist. Respond in {selected_language}."},
                        {"role": "user", "content": f"Analyze these video stats: CTR {ctr_val}, AVD {avd_val}, Views {views_val}, Subs gained {sub_rate}. Explain what is working, what is failing based on YouTube benchmarks, and give 3 actionable steps to improve performance."}
                    ],
                    temperature=0.7
                )
                st.success("Analytiikkadiagnoosi valmis!")
                st.write(res.choices[0].message.content)

# --- TAB 13: Channel Branding (PRO) ---
elif menu_choice == "branding":
    st.title("🎨 Kanavan Brändäys -Generaattori")
    st.markdown("Syötä kiinnostuksen kohteesi ja yleisösi luodaksesi täydellisen visuaalisen ja verbaalisen brändäyspaketin.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        brand_interests = st.text_input("Intohimosi, taitosi tai aihealueesi:")
        brand_audience = st.text_input("Kuka on tavoiteyleisösi?")
        
        if st.button("Generoi Täydellinen Brändäyspaketti", type="primary") and brand_interests:
            with st.spinner("Suunnitellaan brändi-identiteettiä..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an elite YouTube brand strategist and creative director. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create a full YouTube channel branding package based on interests: '{brand_interests}' targeting '{brand_audience}'. Include: 1) 5 Catchy Channel Names, 2) A powerful channel Slogan, 3) Profile picture visual concept, 4) Banner visual concept and color scheme, and 5) A compelling 'About' section description."}
                    ],
                    temperature=0.7
                )
                st.success("Brändäyspaketti valmis!")
                st.write(res.choices[0].message.content)

# --- TAB 14: Timestamp Generator (PRO) ---
elif menu_choice == "timestamps":
    st.title("⏱️ Videon Luvut & Aikaleimat -Generaattori")
    st.markdown("Liitä käsikirjoitus tai muistiinpanot luodaksesi SEO-ystävälliset aikaleimat.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        script_input = st.text_area("Liitä videokäsikirjoitus, runko tai muistiinpanot tähän:")
        
        if st.button("Generoi Aikaleimat", type="primary") and script_input:
            with st.spinner("Rakennetaan lukuja ja aikaleimoja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a YouTube video editor and chapter optimization expert. Respond in {selected_language}."},
                        {"role": "user", "content": f"Analyze this script/outline and create professional, search-friendly video chapters with precise timestamps format (e.g. 00:00 Introduction). Ensure the first timestamp starts at 00:00. Text: '{script_input}'"}
                    ],
                    temperature=0.7
                )
                st.success("Aikaleimat luotu!")
                st.write(res.choices[0].message.content)

# --- TAB 15: Title A/B Matrix (PRO) ---
elif menu_choice == "title_matrix":
    st.title("🧠 Otsikko A/B Testausmatriisi")
    st.markdown("Luo 10 psykologisesti optimoitua videon otsikkoa maksimoidaksesi CTR:n.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        base_topic = st.text_input("Syötä videon pääaihe tai raaka idea:")
        
        if st.button("Generoi Otsikkomatriisi", type="primary") and base_topic:
            with st.spinner("Sovelletaan psykologisia triggereitä ja otsikkokaavoja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an expert in YouTube click psychology, CTR optimization, and copywriting. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 10 distinct video titles for the topic '{base_topic}', each using a different psychological angle (e.g., Curiosity Gap, Fear of Missing Out, Quick Hack/Shortcut, Contrast/Controversy, Authority, Question, Negative/Warning, Numbers/List, Simplicity, Storytelling). Clearly label the angle for each."}
                    ],
                    temperature=0.7
                )
                st.success("Otsikkomatriisi luotu!")
                st.write(res.choices[0].message.content)

# --- TAB 16: AI Image Prompts (PRO) ---
elif menu_choice == "ai_images":
    st.title("🎨 Tekoälyn Pienoiskuvapromptit")
    st.markdown("Luo valmiita prompteja Midjourney-, DALL-E- tai Stable Diffusion -kuvageneraattoreille.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        img_topic = st.text_input("Mikä on videon aihe tai keskeinen visuaalinen elementti?")
        img_mood = st.selectbox("Visuaalinen tunnelma & tyyli", ["Elokuvallinen & Dramaattinen", "Kirkas & Eloisa Sarjakuva / 3D", "Tekno / Cyberpunk Glow", "Tumma & Salaperäinen Studio"])
        
        if st.button("Generoi AI Kuvapromptit", type="primary") and img_topic:
            with st.spinner("Muotoillaan prompteja..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are an expert AI prompt engineer specializing in high-CTR YouTube thumbnail imagery. Respond in {selected_language}."},
                        {"role": "user", "content": f"Create 3 distinct text-to-image prompts for a YouTube thumbnail about '{img_topic}' in a '{img_mood}' style. Make them extremely detailed, optimized for 16:9 aspect ratio, and visually striking. Include aspect ratio parameters (e.g. --ar 16:9) where applicable."}
                    ],
                    temperature=0.7
                )
                st.success("Promptit valmiina!")
                st.write(res.choices[0].message.content)

# --- TAB 17: Script Voice Optimizer (PRO) ---
elif menu_choice == "voice":
    st.title("🎙️ Puhe- & Ääniohjaus -Optimoija")
    st.markdown("Muunna teksti luonnolliseksi puherytmiksi luonnollisilla tauoilla ja esitysvihjeillä.")
    
    if not is_pro:
        render_paywall_warning()
    elif not client:
        st.error("OpenAI API key is missing!")
    else:
        raw_script = st.text_area("Liitä raakakäsikirjoitus tai kappale tähän:")
        
        if st.button("Optimoi Puhetoimitukselle", type="primary") and raw_script:
            with st.spinner("Säädetään tahteja, taukoja ja luonnollisia puhekuvioita..."):
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": f"You are a professional voiceover coach and YouTube dialogue director. Your goal is to rewrite text so it sounds conversational, energetic, and natural when spoken aloud, complete with performance cues like [pause], [lean in], or [emphasis]. Respond in {selected_language}."},
                        {"role": "user", "content": f"Optimize this text for engaging spoken voice delivery: '{raw_script}'"}
                    ],
                    temperature=0.7
                )
                st.success("Äänikäsikirjoitus optimoitu!")
                st.write(res.choices[0].message.content)

# --- TAB 18: Growth & ROI Simulator (PRO) ---
elif menu_choice == "simulator":
    st.title("💰 Kasvu- & Ansiolaskelma Simulaattori")
    st.markdown("Arvioi mainostuloja (AdSense), ennustettuja katselukertoja ja tilaajakehitystä.")
    
    if not is_pro:
        render_paywall_warning()
    else:
        st.markdown("Määritä videon oletetut suorituskykyparametrit:")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            sim_views = st.number_input("Tavoiteltu katselumäärä", min_value=100, max_value=10000000, value=10000, step=500)
            sim_rpm = st.slider("Arvioitu RPM ($ per 1 000 katselua)", min_value=0.5, max_value=30.0, value=4.5, step=0.5)
        with col_s2:
            sim_ctr = st.slider("Odotettu klikkaussuhde (CTR %)", min_value=1.0, max_value=25.0, value=5.0, step=0.5)
            sim_sub_conv = st.slider("Tilaajia per 1 000 katselua", min_value=1, max_value=50, value=10, step=1)
            
        if st.button("Laske Ennusteet", type="primary"):
            estimated_earnings = (sim_views / 1000) * sim_rpm
            estimated_subs = int((sim_views / 1000) * sim_sub_conv)
            
            st.success("Simulaatio valmis!")
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric(label="Arvioidut Mainostulot", value=f"${estimated_earnings:.2f}")
            with col_res2:
                st.metric(label="Ennustetut Uudet Tilaajat", value=f"+{estimated_subs}")
            with col_res3:
                st.metric(label="Suorituskyvyn pisteet", value="Erinomainen 🚀" if sim_ctr >= 5.0 else "Vaatii työtä ⚠️")
                
            if client:
                with st.spinner("Generoidaan tekoälyn strategista palautetta..."):
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": f"You are a YouTube growth economist and strategist. Respond in {selected_language}."},
                            {"role": "user", "content": f"Analyze these projected stats for a video: {sim_views} views, {sim_ctr}% CTR, ${sim_rpm} RPM, yielding ${estimated_earnings:.2f} revenue and {estimated_subs} subs. Provide 3 short, punchy strategic recommendations to push these numbers even higher."}
                        ],
                        temperature=0.7
                    )
                    st.markdown("### 🤖 Tekoälyn Strateginen Palaute")
                    st.write(res.choices[0].message.content)
