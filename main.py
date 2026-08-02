import os
from dotenv import load_dotenv
import customtkinter as ctk_lib
import psycopg as psycopg
import random as random
from controllers.MainController import MainController
from models.db import DB
from models.users import Users
from models.events import Events
from models import  attribute as attribute_model
import views.hubform as hubform_view
import views.createform as createform_view

load_dotenv()

ctk_lib.set_appearance_mode("dark")
ctk_lib.set_default_color_theme("blue")

root = ctk_lib.CTk()
root.title("Выбор персонажа")
root.geometry("600x600")

content_frame = ctk_lib.CTkFrame(root)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

DB = DB(psycopg,os)
Users = Users(DB)
Events = Events(DB,random,Users)

controller = MainController(
    ctk_lib = ctk_lib,
    db_model=DB,
    users_model=Users,
    events_model=Events,
    attribute_model = attribute_model,
    hubform_view=hubform_view,
    createform_view=createform_view,
    content_frame = content_frame

)
controller.hub_form()

root.mainloop()