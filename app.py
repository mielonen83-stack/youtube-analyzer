import requests
import streamlit as st
import pandas as pd
from pytrends.request import TrendReq

# Sivun asetukset
st.set_page_config(page_title="YouTube Keyword, Trend & AI Analyzer Pro", page_icon="📺", layout="wide")

# Istunnon tila
if 'search_count' not in st.session_state:
    st.session_state.search_count = 0
if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 1. Autocomplete-haku
def get_youtube_suggestions(query):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()[1]
    except:
        return []
    return []

# 2. Google Trends (YouTube) -haku
def get_youtube_trends(keyword):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe='today 1-m', geo='', gprop='youtube')
        data = pytrends.interest_over_time()
        if not data.empty:
            return data.drop(columns=['isPartial']).reset_index()
    except Exception as e:
        return None
    return None

# Käyttöliittymä
st.title("📺 YouTube Keyword, Trend & AI Analyzer Pro")
st.write("An all-in-one intelligence tool for content creators to find viral video ideas, trends, and AI-generated metadata.")

# Sivupalkki maksupuolelle
st.sidebar.header("Account & Billing")
if st.session_state.is_pro:
    st.sidebar.success("⭐ Pro Account Active")
    if st.sidebar.button("Cancel Pro (Test)"):
        st.session_state.is_pro = False
        st.rerun()
else:
    st.sidebar.info("Free Tier: 2 searches allowed")
    if st.sidebar.button("Upgrade to Pro ($9/mo)"):
        st.session_state.is_pro = True
        st.sidebar.success("Thank you for upgrading!")
        st.rerun()

FREE_LIMIT = 2
if not st.session_state.is_pro and st.session_state.search_count >= FREE_LIMIT:
    st.error("🚨 Free search limit reached!")
    st.warning("You have used all your free searches. Upgrade to **Pro** in the sidebar for unlimited analytics, AI generation, and CSV exports.")
else:
    query = st.text_input("Enter a niche or keyword (e.g., gaming, fitness, python):", "")

    if query:
        if not st.session_state.is_pro:
            st.session_state.search_count += 1
            st.info(f"Free searches left: {FREE_LIMIT - st.session_state.search_count}")

        tab1, tab2, tab3, tab4 = st.tabs([
            "🔍 Search Suggestions", 
            "📈 YouTube Trends", 
            "🏆 Competitor Ideas", 
            "🤖 AI Content & SEO"
        ])

        # Välilehti 1: Autocomplete
        with tab1:
            st.subheader("What people are typing right now (Autocomplete)")
            with st.spinner("Fetching autocomplete data..."):
                suggestions = get_youtube_suggestions(query)
            
            if suggestions:
                st.success(f"Found {len(suggestions)} suggestions!")
                for i, item in enumerate(suggestions, 1):
                    st.markdown(f"**{i}.** {item}")
                
                if st.session_state.is_pro:
                    df_sug = pd.DataFrame({"Suggestion": suggestions})
                    st.download_button("Download Suggestions CSV", df_sug.to_csv(index=False).encode('utf-8'), f"suggestions_{query}.csv", "text/csv")
            else:
                st.warning("No suggestions found.")

        # Välilehti 2: Google Trends (YouTube)
        with tab2:
            st.subheader("YouTube Search Interest (Past 30 Days)")
            with st.spinner("Fetching Google Trends for YouTube..."):
                trend_data = get_youtube_trends(query)
            
            if trend_data is not None and not trend_data.empty:
                st.line_chart(trend_data.set_index('date'))
                st.success("Trend data loaded successfully!")
                
                if st.session_state.is_pro:
                    st.download_button("Download Trend Data CSV", trend_data.to_csv(index=False).encode('utf-8'), f"trends_{query}.csv", "text/csv")
            else:
                st.info("No sufficient trend data available for this specific keyword right now. Try a broader term.")

        # Välilehti 3: Kilpailija-analyysi / Ideat
        with tab3:
            st.subheader("High-Performing Content Angles")
            st.write("Based on common viral video frameworks for this topic:")
            
            angles = [
                f"The Ultimate Beginner's Guide to {query.title()} in 2026",
                f"I Tried {query.title()} For 30 Days (Here's What Happened)",
                f"Top 5 Mistakes People Make With {query.title()}",
                f"Why Most People Fail At {query.title()} (And How To Fix It)"
            ]
            
            for i, angle in enumerate(angles, 1):
                st.markdown(f"🔥 **Video Idea {i}:** {angle}")
            
            if not st.session_state.is_pro:
                st.info("🔒 Upgrade to Pro to unlock advanced API competitor scraping features.")

        # Välilehti 4: AI Content & SEO Generator
        with tab4:
            st.subheader("🤖 AI-Powered Metadata & SEO Generator")
            st.write(f"Generated optimized packaging and strategy for your video about **{query}**:")

            q_cap = query.capitalize()
            
            st.markdown("### ✍️ Catchy Video Titles")
            st.code(f"""1. The Truth About {q_cap} Nobody Is Telling You
2. I Tested {q_cap} For 7 Days Straight (Shocking Results)
3. How to Master {q_cap} in 2026 (Step-by-Step)
4. Stop Making This HUGE Mistake With {q_cap}!""", language="text")

            st.markdown("### 📄 Optimized Video Description")
            st.code(f"""Welcome back to the channel! In today's video, we are diving deep into {query}. Whether you are a beginner or looking to level up your skills, this guide covers everything you need to know about {query} in 2026.

Timestamps:
0:00 - Introduction to {q_cap}
1:30 - The #1 Biggest Mistake
3:45 - Step-by-Step Walkthrough
8:15 - Final Thoughts & Results

If you found this video helpful, make sure to like, subscribe, and drop a comment below with your thoughts!

#shorts #{query.replace(' ', '')} #{q_cap}Guide""", language="text")

            st.markdown("### 🏷️ Recommended Tags")
            st.info(f"{query}, {query} tutorial, how to {query}, best {query} 2026, {query} tips, {query} guide, learn {query}")

            st.markdown("### 🎨 Thumbnail Concept Ideas")
            st.markdown(f"""
- **Visual:** Split screen showing "Before vs. After" or a confused face looking at a bright graph about {query}.
- **Text on thumbnail:** "DON'T DO THIS!" or "Finally Revealed!" in bold yellow/white letters.
- **Color palette:** High contrast dark background with vibrant neon accents (orange or blue).
""")
