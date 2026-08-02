import streamlit as st
from openai import OpenAI

# Sivuston asetukset
st.set_page_config(page_title="YouTube Pro Analyzer", page_icon="🎬", layout="wide")

# Haetaan OpenAI API-avain Streamlitin Secretsistä turvallisesti
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key)
except Exception:
    client = None

# --- SIVUPALKKI: Hallinta & Maksu ---
st.sidebar.header("🚀 Pro-versio")
st.sidebar.write("Avaa kaikki tekoälytyökalut ja rajoittamattomat haut!")

# Stripe-maksulinkki (Vaihda tähän oma oikea Stripe Payment Link -osoitteesi)
stripe_link = "https://buy.stripe.com/test_placeholder"
st.sidebar.markdown(f"[Osta Pro-oikeudet (9€)]({stripe_link})", unsafe_allow_html=True)

# Simuloitu Pro-tilan tarkistus (Käyttäjä voi testata laittamalla rasti)
is_pro = st.sidebar.checkbox("Olen maksanut Pro-version (Testitila)")

# --- PÄÄVALIKKO (Välilehdet) ---
tab1, tab2, tab3 = st.tabs(["📊 Perushaut & Trendit", "✨ AI Työkalut & Ideat", "🎯 Pienoiskuvat (Thumbnails)"])

# --- VÄLILEHTI 1: Perushaut & Trendit ---
with tab1:
    st.title("🎬 YouTube Sisällöntuottajan Työkalu")
    st.write("Hae hakusanoja, tutki trendejä ja arvioi tuottoja ilmaiseksi.")
    
    keyword = st.text_input("Syötä hakusana tai aihe (esim. pelit, keittiö):")
    
    if st.button("Hae tiedot"):
        if keyword:
            st.success(f"Hakusanalle '{keyword}' löytyi seuraavat alustavat tiedot:")
            col1, col2, col3 = st.columns(3)
            col1.metric("Arvioidut haut / kk", "45,200", "+12%")
            col2.metric("Kilpailu", "Keskitaso", "-5%")
            col3.metric("Keskimääräinen RPM", "4.50 €", "0.2 €")
            
            st.info("💡 Vinkki: Siirry 'AI Työkalut' -välilehdelle luodaksesi tekoälyllä otsikoita ja skriptejä!")
        else:
            st.warning("Kirjoita ensin hakusana.")

# --- VÄLILEHTI 2: AI Työkalut & Viraaliideat ---
with tab2:
    st.title("🤖 Tekoälypohjaiset Työkalut")
    
    if not client:
        st.error("OpenAI API-avain puuttuu! Aseta se Streamlit Cloudin Secrets-asetuksiin.")
    else:
        # Alavalinta työkaluille
        ai_tool_choice = st.selectbox("Valitse tekoälytoiminto:", ["Viraaliideoiden Generaattori (Idea Machine)", "AI Metatiedot & Skripti"])
        
        if ai_tool_choice == "Viraaliideoiden Generaattori (Idea Machine)":
            st.subheader("💡 Viraaliideoiden Generaattori")
            niche = st.text_input("Mikä on kanavasi aihepiiri/niche? (esim. Talous, Pelaaminen, Hyvinvointi)")
            
            if st.button("Generoi viraaliideoita"):
                if not is_pro:
                    st.warning("🔒 Tämä on Pro-ominaisuus. Osta Pro-oikeudet sivupalkin kautta tai laita testitila päälle!")
                elif not niche:
                    st.warning("Kirjoita ensin aihepiiri.")
                else:
                    with st.spinner("Tekoäly keittelee viraaliideoita..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "Olet huippuluokan YouTube-strategi."},
                                    {"role": "user", "content": f"Luo 5 erittäin koukuttavaa ja omaperäistä viraaliidea-aihiota aiheelle '{niche}'. Anna jokaiselle idealle catchy otsikko ja lyhyt perustelu miksi se toimisi."}
                                ],
                                temperature=0.7
                            )
                            st.success("Viraaliideat luotu onnistuneesti!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Virhe tekoälypyynnössä: {e}")

        else:
            st.subheader("✍️ AI Metatiedot & Käsikirjoitus")
            video_topic = st.text_input("Videon tarkka aihe:")
            
            if st.button("Luo otsikot ja skripti"):
                if not is_pro:
                    st.warning("🔒 Tämä on Pro-ominaisuus. Osta Pro-oikeudet sivupalkin kautta!")
                elif not video_topic:
                    st.warning("Syötä videon aihe.")
                else:
                    with st.spinner("Kirjoitetaan sisältöä..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[
                                    {"role": "system", "content": "Olet ammattimainen YouTube-käsikirjoittaja."},
                                    {"role": "user", "content": f"Luo videolle '{video_topic}' 3 klikkausystävällistä otsikkoa, houkutteleva kuvaus ja lyhyt videon aloitus (hook)."}
                                ],
                                temperature=0.7
                            )
                            st.success("Metatiedot ja skripti luotu onnistuneesti!")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Virhe: {e}")

# --- VÄLILEHTI 3: Thumbnail-ideoiden kuvailija ---
with tab3:
    st.title("🎯 Pienoiskuva-suunnittelija (Thumbnail Generator)")
    st.write("Saat tekoälyltä tarkan visuaalisen reseptin sille, millainen pikkukuva pysäyttää selaamisen.")
    
    thumb_topic = st.text_input("Mikä on videon pääidea tai yllättävä käänne?")
    thumb_style = st.selectbox("Visuaalinen tyyli", ["Shokeeraava / Yllättävä", "Minimalistinen ja tyylikäs", "Meemi / Hauska", "Vertailu (Ennen vs Jälkeen)"])
    
    if st.button("Generoi Thumbnail-ideat"):
        if not is_pro:
            st.warning("🔒 Tämä vaatii Pro-version!")
        elif not thumb_topic:
            st.warning("Syötä ensin videon idea.")
        elif not client:
            st.error("OpenAI avain puuttuu asetuksista.")
        else:
            with st.spinner("Suunnitellaan klikkausmagneetteja..."):
                try:
                    prompt = f"""
                    Toimi YouTube-pienoiskuva-asiantuntijana. Luo 3 erilaista visuaalista ideaa pikkukuvalle (thumbnail) aiheesta: '{thumb_topic}'.
                    Valittu tyyli: {thumb_style}.
                    Jokaisesta ideasta tulee ilmetä:
                    1. Visuaalinen sommittelu ja tausta
                    2. Teksti kuvassa (maksimissaan 3 sanaa, isot kirjaimet)
                    3. Päävärit
                    """
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "Olet graafinen suunnittelija ja YouTube CTR-ekspertti."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7
                    )
                    tulo = response.choices[0].message.content
                    st.success("Thumbnail-ideat luotu onnistuneesti!")
                    st.write(tulo)
                except Exception as e:
                    st.error(f"Virhe: {e}")
