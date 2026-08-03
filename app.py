elif menu_choice == "translator":
    str_module.title(c_texts["translator"]["title"])
    if not is_pro: 
        render_paywall()
    elif client:
        text_to_trans = str_module.text_area(c_texts["translator"]["input"])
        target_lang = str_module.selectbox("Target Language:", ["English", "Finnish", "Swedish", "Spanish", "German", "French", "Japanese"])
        if str_module.button(c_texts["translator"]["btn"], type="primary") and text_to_trans:
            with str_module.spinner(c_texts["translator"]["spinner"]):
                try:
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": f"You are a professional localizer and translator. Respond in {selected_language}."},
                            {"role": "user", "content": f"Translate and localize the following text to {target_lang}: '{text_to_trans}'"}
                        ],
                        temperature=0.7
                    )
                    str_module.success("Done!")
                    str_module.markdown(f'<div class="result-box">{res.choices[0].message.content}</div>', unsafe_allow_html=True)
                except Exception as e:
                    str_module.error(f"Error: {e}")

elif menu_choice in tools_advanced and menu_choice != "translator":
    if not is_pro:
        render_paywall()
    else:
        str_module.title(c_texts.get(menu_choice, {}).get("title", "Advanced Tool"))
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
