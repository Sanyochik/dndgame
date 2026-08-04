def journeyform(ctk,pil,content_frame):

    def testfunc():
        print("test")

    enemy_img =ctk.CTkImage(
        light_image=pil.open('img/bandit.png'),
        size=(200,200)
    )

    image_div = ctk.CTkLabel(
        content_frame,
        image=enemy_img,
    )

    image_div.pack(pady="20",side='top')

    enemy_hp = ctk.CTkLabel(content_frame, text="10/30")
    enemy_hp.pack(pady="20")

    button = ctk.CTkButton(content_frame, text=f"Атаковать", command=testfunc)
    button.pack(pady=10)

    button = ctk.CTkButton(content_frame, text=f"Очаровать", command=testfunc)
    button.pack(pady=10)


    player_info = ctk.CTkLabel(content_frame, text="Саурон\n\n 10/30 Здоровья\n\n 20 силы\n\n 14 харизмы")
    player_info.pack(side='left')