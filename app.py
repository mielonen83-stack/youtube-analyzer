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
        # Korjatut, selkeämmät kategoriat:
        "cat1": "💡 Perustyökalut & Ideat",
        "cat2": "🚀 Edistynyt Optimointi & Strategia",
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
        "cat1": "💡 Basics & Ideas",
        "cat2": "🚀 Advanced Optimization",
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
}.get(selected_language.split()[0], {
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
    "cat1": "💡 Basics & Ideas",
    "cat2": "🚀 Advanced Optimization",
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
