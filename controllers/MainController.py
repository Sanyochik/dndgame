class MainController:
    def __init__(self,ctk_lib,pil_lib,db_model,users_model,events_model,journey_model,attribute_model,dice_model,hubform_view,createform_view,journeyform_view,content_frame):
        self.ctk_lib = ctk_lib
        self.pil_lib = pil_lib
        self.users_model = users_model
        self.db_model = db_model
        self.events_model = events_model
        self.journey_model = journey_model
        self.attribute_model = attribute_model
        self.dice_model = dice_model
        self.hubform_view = hubform_view
        self.createform_view = createform_view
        self.journeyform_view = journeyform_view
        self.content_frame = content_frame


    def hub_form(self):
        self.cleaner_form()
        self.hubform_view.hubform(self,self.ctk_lib,self.content_frame,self.users_model.getusers())


    def select_player(self,user_id):
        self.cleaner_form()
        active_journey = self.journey_model.getactivejourney(self.users_model.getcurrentuser(user_id),self.events_model.getevents())
        if not active_journey:
            complited = self.journey_model.getcomplitejourney(self.users_model.getcurrentuser(user_id),self.events_model.getevents())
            active_event = self.events_model.getrandomevents(complited)
            active_journey = [self.journey_model.addjourney(self.users_model.getcurrentuser(user_id), active_event)]
            print(active_journey)
        self.journeyform_view.journeyform(self.ctk_lib, self.pil_lib, self.content_frame, active_journey,self.users_model.getcurrentuser(user_id),self.events_model.getcurrentevent(active_journey[0][1]))


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