def hubform(controller,ctk,content_frame,players):

    for row in players:
        button = ctk.CTkButton(content_frame, text=f"Персонаж: {row[1]}", command=lambda current_id=row[0]: controller.select_player(current_id))
        button.pack(pady=10)

    button = ctk.CTkButton(content_frame, text="Создать нового персонажа", command=controller.create_form,fg_color="green")
    button.pack(pady=10)