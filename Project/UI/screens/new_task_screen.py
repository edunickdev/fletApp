import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar

class NewTaskScreen:

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                CustomAppBar(),
                
            ]
        )

    

