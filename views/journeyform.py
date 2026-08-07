def journeyform(ctk,pil,content_frame,controller,journey_info,user_info,event_info):


    username = user_info[0][1]
    user_max_hp = user_info[0][4]
    user_current_hp = journey_info[0][3]
    user_strength_value = user_info[0][2]
    user_charism_value = user_info[0][3]
    enemy_current_hp_value = (journey_info[0][4])
    enemy_max_hp_value = (event_info[0][6])
    enemy_dmg = (event_info[0][9])
    enemy_strength_def = (event_info[0][4])
    enemy_charism_def = (event_info[0][5])
    img_url = (event_info[0][3])

    def atack():
        atack_result = controller.atackenemy(user_strength_value,enemy_dmg,enemy_strength_def,user_current_hp,enemy_current_hp_value)
        print(atack_result)
    def charm():
        controller.charmenemy(user_charism_value,enemy_dmg,enemy_charism_def,user_current_hp,enemy_current_hp_value)
    enemy_img =ctk.CTkImage(
        light_image=pil.open(img_url),
        size=(200,200)
    )

    image_div = ctk.CTkLabel(
        content_frame,
        image=enemy_img,
        text="",
    )

    image_div.pack(pady="20",side='top')

    enemy_hp = ctk.CTkLabel(content_frame, text=f"{enemy_current_hp_value}/{enemy_max_hp_value}")
    enemy_hp.pack(pady="20")

    button = ctk.CTkButton(content_frame, text=f"Атаковать", command=atack)
    button.pack(pady=10)

    button = ctk.CTkButton(content_frame, text=f"Очаровать", command=charm)
    button.pack(pady=10)


    player_info = ctk.CTkLabel(content_frame, text=f"{username}\n\n {user_current_hp}/{user_max_hp} Здоровья\n\n {user_strength_value} силы\n\n {user_charism_value} харизмы")
    player_info.pack(side='left')