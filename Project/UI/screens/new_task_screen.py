import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar

class NewTaskScreen:

    def __init__(self, page):
        super().__init__()
        self.page = page
        
        
    categories = [
        "Work",
        "Study",
        "Personal",
        "Leisure",
    ]    
    
    # primera screen a construir

    def build(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                "Agrega una nueva Tarea"
            ],
        )
    

