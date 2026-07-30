def createform(controller,ctk,content_frame):
    username_input_type = ctk.StringVar()

    def addatr(label_name,freestats_value):
        curent_label = data_inputs[label_name].cget("text")
        results = controller.addatr(curent_label,freestats_value)
        data_inputs[label_name].configure(text=results[0])
        freestats.configure(text=results[1])

    def reduceatr(label_name,freestats_value):
        curent_label = data_inputs[label_name].cget("text")
        results = controller.reduceatr(curent_label,freestats_value)
        data_inputs[label_name].configure(text=results[0])
        freestats.configure(text=results[1])

    input_name = ctk.CTkEntry(
        content_frame,
        textvariable=username_input_type,
        placeholder_text="Введите имя"
    )
    input_name.pack(pady=5)

    inputs = ["str_input", "chr_input", "vit_input"]

    rowstat = ctk.CTkFrame(content_frame)
    rowstat.pack(pady=5)

    labelstats = ctk.CTkLabel(rowstat, text="Доступно для распределения ещё: ")
    labelstats.pack(side='left')
    freestats = ctk.CTkLabel(rowstat, text="20")
    freestats.pack(side='left')
    endstats = ctk.CTkLabel(rowstat, text=" очков")
    endstats.pack(side='left')

    data_inputs = {}

    for label_name in inputs:
        row = ctk.CTkFrame(content_frame)
        row.pack(pady=5)
        reduce = ctk.CTkButton(row, text="-", command=lambda name=label_name: reduceatr(name,freestats.cget("text")), fg_color="green", width=30)
        reduce.pack(side='left')
        data_inputs[label_name] = ctk.CTkLabel(row, text="1")
        data_inputs[label_name].pack(side='left')
        add = ctk.CTkButton(row, text="+", command=lambda name=label_name: addatr(name,freestats.cget("text")), fg_color="green", width=30)
        add.pack(side='left')


    button = ctk.CTkButton(content_frame, text="Создать нового персонажа", command=lambda: controller.createchar(username_input_type.get(),int(data_inputs['str_input'].cget("text")),int(data_inputs['chr_input'].cget("text")),int(data_inputs['vit_input'].cget("text"))), fg_color="green")
    button.pack(pady=15)