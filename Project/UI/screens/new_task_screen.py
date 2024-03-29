import time
from flet import Page, Column, TextField, icons, MainAxisAlignment, Row, CrossAxisAlignment, ElevatedButton, Text, Dropdown, dropdown, SnackBar, IconButton

from Project.ChatGPT.conexion import sugerencias_chatGPT
from Project.sources.connection_firebase_db import add_data
from Project.sources.models.task import Task


categories = ["Trabajo", "Estudio", "Ócio", "Familiar", "Personal"]
new_task = Task( "", "", "", "", "", "" )
inputTitulo = TextField( prefix_icon=icons.TASK, width=340, label="Título de la tarea" )
fechaInicial = TextField( prefix_icon=icons.DATE_RANGE, width=165, label="Fecha inicial", hint_text="DD/MM/AAAA" )
fechaFinal = TextField( prefix_icon=icons.DATE_RANGE, width=165, label="Fecha final", hint_text="DD/MM/AAAA" )
inputDescripcion = TextField( width=400, max_length=140, border_radius=10, prefix_icon=icons.DESCRIPTION, label="Objetivo de la tarea", max_lines=4 )
GPT_sugerencias = Text( value="Generar sugerencias de ChatGPT 3.5", size=14, max_lines=7, overflow="ellipsis", width=390 )

def generarSugerencias(self):
     if not inputDescripcion.value:
          GPT_sugerencias.value = "Para poder generar sugerencias con ChatGPT, el campo objetivo de la tarea no puede estar vacio"
          self.page.update()
          time.sleep(8)
          GPT_sugerencias.value = "Generar sugerencias de ChatGPT 3.5"
          self.page.update()
     else:
          GPT_sugerencias.value = sugerencias_chatGPT(inputDescripcion.value)
          self.page.update()

dropdownCategory = Dropdown(
     width=340,
     label="Categoría de la tarea", 
     prefix_icon=icons.CATEGORY,
     options=[
               dropdown.Option(category) for category in categories
          ]
     )


def NewTaskScreen(page: Page):

     def save_task(self):
          
          if not inputTitulo.value:
               inputTitulo.error_text = "Este campo no puede ir vacio"
          else:
               new_task.title = inputTitulo.value
          if not fechaInicial.value:
               fechaInicial.error_text = "Este campo no puede ir vacio"
          else:
               new_task.start = fechaInicial.value
          if not fechaFinal.value:
               fechaFinal.error_text = "Este campo no puede ir vacio"
          else:
               new_task.end = fechaFinal.value
          if not inputDescripcion.value:
               inputDescripcion.error_text = "Este campo no puede ir vacio"
          else:     
               new_task.description = inputDescripcion.value
          if not dropdownCategory.value:
               dropdownCategory.error_text = "Este campo no puede ir vacio"
          else:
               new_task.category = dropdownCategory.value
               if new_task.suggestGPT != "Generar sugerencias de ChatGPT 3.5" or new_task.suggestGPT != "Para poder generar sugerencias con ChatGPT, el campo objetivo de la tarea no puede estar vacio":
                    new_task.suggestGPT = GPT_sugerencias.value
               else:
                    new_task["suggestGPT"] = "El usuario no genero sugerencias con ChatGPT"

          if inputTitulo.error_text or fechaInicial.error_text or fechaFinal.error_text or inputDescripcion.error_text or dropdownCategory.error_text:
               clearFields()
               self.page.update()
               clearErrors()
               self.page.update()
               return
          else:
               add_data('task', new_task.to_dict())
               clearFields()
               self.page.update()
               self.page.snack_bar = SnackBar( content=Text("Tarea guardada con éxito"), duration= 6000 )
               self.page.snack_bar.open = True
               self.page.update()
               self.page.go("/principal")
               return


     def clearFields():
          inputTitulo.value = ""
          fechaInicial.value = ""
          fechaFinal.value = ""
          inputDescripcion.value = ""
          dropdownCategory.value = ""
          GPT_sugerencias.value = "Generar sugerencias de ChatGPT 3.5"

     def clearErrors():
          time.sleep(3)
          inputTitulo.error_text = None
          fechaInicial.error_text = None
          fechaFinal.error_text = None
          inputDescripcion.error_text = None
          dropdownCategory.error_text = None


     screen = Column(
               spacing=70,
               controls=[
                    Row(
                         alignment=MainAxisAlignment.CENTER,
                         vertical_alignment=CrossAxisAlignment.START,
                         controls=[
                              Text(
                                   "Nueva Tarea",
                                   size= 50,
                                   text_align= "center",
                              ),
                         ]
                    ),
                    Row(
                         alignment=MainAxisAlignment.CENTER,
                         vertical_alignment=CrossAxisAlignment.START,
                         controls=[
                              Column(
                                   spacing=20,
                                   width=350,
                                   controls=[
                                        Row(
                                             alignment = MainAxisAlignment.CENTER,
                                             controls=[
                                                  inputTitulo
                                             ]
                                        ),
                                        Row(
                                             alignment = MainAxisAlignment.CENTER,
                                             controls=[
                                                  dropdownCategory
                                             ]
                                        ),
                                        Row(
                                             alignment = MainAxisAlignment.CENTER,
                                             vertical_alignment = CrossAxisAlignment.CENTER,
                                             controls=[
                                                  fechaInicial,
                                                  fechaFinal
                                             ]
                                        ),
                                   ]
                              ),
                              Column(
                                   width=520,
                                   controls=[
                                        Row(
                                             alignment = MainAxisAlignment.CENTER,
                                             vertical_alignment = CrossAxisAlignment.CENTER,
                                             controls=[
                                                  inputDescripcion,
                                                  IconButton( icon=icons.CONFIRMATION_NUM, on_click=generarSugerencias )
                                             ]
                                        ),
                                        Row(
                                             alignment = MainAxisAlignment.CENTER,
                                             controls=[
                                                  GPT_sugerencias,
                                             ]
                                        )
                                   ]
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
                                   on_click = save_task
                              ),
                         ]
                    ),
               ]
          )

     return screen
