elif "ANALYysi:" in line or "ANALYYSISI:" in line or "ANALYYSI:" in line:
                            analyysi = line.split(":", 1)[1].strip()

                    col1, col2, col3 = str_module.columns(3)
                    with col1:
                        str_module.metric("Arvioidut haut / kk", haut)
                    with col2:
                        str_module.metric("Kilpailutaso", kilpailu)
                    with col3:
                        str_module.metric("Arvioitu RPM", rpm)

                    str_module.markdown(f"""
                        <div class="result-box">
                            <h4 style="margin-top: 0; color: #0f172a;">🧠 Strateginen analyysi</h4>
                            <p style="color: #334155; font-size: 16px; margin-bottom: 0;">{analyysi}</p>
                        </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    str_module.error(f"Virhe tekoälypyynnössä: {e}")
        else:
            str_module.warning("Kirjoita hakusana ennen hakua.")

elif menu_choice in tools_basics and menu_choice != "search":
    # Muut perustoiminnot
    str_module.title(c_texts[menu_choice]["title"])
    user_input = str_module.text_input(c_texts[menu_choice]["input"])
    if str_module.button(c_texts[menu_choice]["btn"], type="primary"):
        if user_input:
            if not client:
                str_module.error("OpenAI API key is missing!")
            else:
                with str_module.spinner(c_texts[menu_choice]["spinner"]):
                    try:
                        res = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": f"You are an expert YouTube content creator. Respond in {selected_language}."},
                                {"role": "user", "content": f"Topic: {user_input}, Video length: {video_length}, Target audience: {target_audience}"}
                            ],
                            temperature=0.7
                        )
                        str_module.markdown(f"""
                            <div class="result-box">
                                {res.choices[0].message.content}
                            </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        str_module.error(f"Virhe: {e}")
        else:
            str_module.warning("Täytä vaadittu kenttä.")

elif menu_choice in tools_advanced:
    if not is_pro:
        render_paywall()
    else:
        str_module.title(c_texts[menu_choice]["title"])
        # Esimerkki edistyneestä työkalusta
        user_input = str_module.text_input(c_texts.get(menu_choice, {}).get("input", "Syötä aihe:"))
        btn_text = c_texts.get(menu_choice, {}).get("btn", "Generoi Pro-sisältö")
        spinner_text = c_texts.get(menu_choice, {}).get("spinner", "Generoidaan...")
        
        if str_module.button(btn_text, type="primary"):
            if not client:
                str_module.error("OpenAI API key is missing!")
            else:
                with str_module.spinner(spinner_text):
                    try:
                        res = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": f"You are an elite YouTube growth hacker and strategist. Respond in {selected_language}."},
                                {"role": "user", "content": f"Execute advanced Pro task '{menu_choice}' for topic: {user_input}"}
                            ],
                            temperature=0.7
                        )
                        str_module.markdown(f"""
                            <div class="result-box">
                                {res.choices[0].message.content}
                            </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        str_module.error(f"Virhe: {e}")
