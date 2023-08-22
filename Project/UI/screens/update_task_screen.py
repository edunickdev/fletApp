import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar

class UpdateTaskScreen:

    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Update Task Screen"),
            ],
        )