def journeyform(ctk,pil,content_frame,journey_info,user_info,event_info):


    username = user_info[0][1]
    user_max_hp = user_info[0][4]
    user_current_hp = journey_info[0][3]
    user_strength_value = user_info[0][2]
    user_charism_value = user_info[0][3]
    enemy_current_hp_value = (journey_info[0][4])
    enemy_max_hp_value = (event_info[0][6])
    img_url = (event_info[0][3])

    def testfunc():
        print("test")

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

    button = ctk.CTkButton(content_frame, text=f"Атаковать", command=testfunc)
    button.pack(pady=10)

    button = ctk.CTkButton(content_frame, text=f"Очаровать", command=testfunc)
    button.pack(pady=10)


    player_info = ctk.CTkLabel(content_frame, text=f"{username}\n\n {user_current_hp}/{user_max_hp} Здоровья\n\n {user_strength_value} силы\n\n {user_charism_value} харизмы")
    player_info.pack(side='left')