from flet import Page, Column, TextField, Icon, icons, MainAxisAlignment, Row, CrossAxisAlignment, ElevatedButton, SafeArea, Text

from Project.UI.components.custom_appbar import CustomAppBar

def NewTaskScreen(page: Page):

     screen = SafeArea(
          content=Column(
               alignment= MainAxisAlignment.CENTER,
               horizontal_alignment= CrossAxisAlignment.CENTER,
               controls=[
                    Text(
                         "Nueva Tarea",
                         size= 30,
                         text_align= "center",
                    ),
                    Row(
                         alignment = MainAxisAlignment.CENTER,
                         controls=[
                              TextField(
                                   prefix_icon=Icon(icons.TASK),
                                   width=550,
                                   label="Título de la tarea",
                              ),
                         ]
                    ),
                    Row(
                         alignment = MainAxisAlignment.CENTER,
                         vertical_alignment = CrossAxisAlignment.CENTER,
                         controls=[
                              TextField(
                                   prefix_icon=Icon(icons.WEEKEND),
                                   width=270,
                                   label="Fecha de inicio de la tarea",
                                   hint_text="DD/MM/AAAA",
                              ),
                              TextField(
                                   prefix_icon=Icon(icons.WEEKEND),
                                   width=270,
                                   label="Fecha de final de la tarea",
                                   hint_text="DD/MM/AAAA",
                              ),
                         ]
                    ),
                    Row(
                         alignment = MainAxisAlignment.CENTER,
                         controls=[
                              TextField(
                                   width=550,
                                   max_length=200,
                                   border_radius=10,
                                   prefix_icon=Icon(icons.DESCRIPTION),
                                   label="Descripción de la tarea",
                                   max_lines=5,
                              ),
                         ]
                    ),
                    Row(
                         alignment = MainAxisAlignment.CENTER,
                         controls=[
                              ElevatedButton(
                                   icon=icons.SAVE,
                                   text="Guardar",
                                   width=220,
                              ),
                         ]
                    ),
               ]
          )
     ) 

     return screen
