def hubform(controller,ctk,content_frame,players):

    for row in players:
        button = ctk.CTkButton(content_frame, text=f"Персонаж: {row[1]}", command=controller.select_player)
        button.pack(pady=10)

    button = ctk.CTkButton(content_frame, text="Создать нового персонажа", command=controller.create_form,fg_color="green")
    button.pack(pady=10)