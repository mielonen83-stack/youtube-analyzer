if menu_choice == "search":
    st.title("📊 Perushaku & Trendit")
    st.markdown("Hae hakusanoja, tutki trendejä ja arvioi ansioita tekoälyn avulla.")
    keyword = st.text_input("🔍 Kirjoita hakusana tai aihe:")
    
    if st.button("Hae & Analysoi", type="primary"):
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
                                    "content": f"You are a YouTube analytics expert. Respond in {selected_language}. Provide a realistic estimate for the given keyword in this exact format:\nHAUT: [estimated monthly searches, e.g. ~12,000]\nKILPAILU: [competition level, e.g. Matala / Keskitaso / Korkea]\nRPM: [estimated RPM, e.g. $3.50]\nANALYysi: [Brief 2-sentence strategic insight about this keyword]"
                                },
                                {
                                    "role": "user", 
                                    "content": f"Analyze keyword: '{keyword}'"
                                }
                            ],
                            temperature=0.7
                        )
                        
                        raw_response = res.choices[0].message.content
                        
                        # Yksinkertainen parsaus rivien mukaan
                        lines = raw_response.split('\n')
                        haut, kilpailu, rpm, analyysi = "~10,000", "Keskitaso", "$3.00", raw_response
                        
                        for line in lines:
                            if "HAUT:" in line:
                                haut = line.split("HAUT:")[1].strip()
                            elif "KILPAILU:" in line:
                                kilpailu = line.split("KILPAILU:")[1].strip()
                            elif "RPM:" in line:
                                rpm = line.split("RPM:")[1].strip()
                            elif "ANALYysi:" in line or "ANALYYSISI:" in line or "ANALYYSI:" in line:
                                analyysi = line.split(":", 1)[1].strip()

                        st.success(f"Tulokset hakusanalle: **{keyword}**")
                        
                        # Siistit visuaaliset mittarit (Metrics)
                        col1, col2, col3 = st.columns(3)
                        col1.metric("🔍 Arvioidut haut / kk", haut)
                        col2.metric("⚔️ Kilpailutaso", kilpailu)
                        col3.metric("💵 Arvioitu RPM", rpm)
                        
                        # Strateginen analyysi nätissä laatikossa
                        st.markdown("### 💡 Strateginen näkemys")
                        st.info(analyysi)
                        
                    except Exception as e:
                        st.error(f"Virhe tekoälyhaussa: {e}")
        else:
            st.warning("Syötä ensin hakusana.")
