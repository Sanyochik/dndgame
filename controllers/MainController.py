class MainController:
    def __init__(self,ctk_lib,db_model,users_model,events_model,attribute_model,dice_model,hubform_view,createform_view,content_frame):
        self.ctk_lib = ctk_lib
        self.users_model = users_model
        self.db_model = db_model
        self.events_model = events_model
        self.attribute_model = attribute_model
        self.dice_model = dice_model
        self.hubform_view = hubform_view
        self.createform_view = createform_view
        self.content_frame = content_frame


    def hub_form(self):
        self.cleaner_form()
        self.hubform_view.hubform(self,self.ctk_lib,self.content_frame,self.users_model.getusers())


    def select_player(self):
        print(self.events_model.getrandomevents())


    def create_form(self):
        self.cleaner_form()
        self.createform_view.createform(self, self.ctk_lib, self.content_frame)


    def cleaner_form(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def createchar(self,username,strength,charism,vitality):
        self.users_model.adduser(username,strength,charism,vitality)
        self.cleaner_form()
        self.hubform_view.hubform(self, self.ctk_lib, self.content_frame, self.users_model.getusers())

    def addatr(self,curent_label,freestats_value):
        return self.attribute_model.add(curent_label,freestats_value)

    def reduceatr(self,curent_label,freestats_value):
        return self.attribute_model.reduce(curent_label,freestats_value)
