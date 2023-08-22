import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar

class HomeScreen:

    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Home Screen"),
                ft.ElevatedButton(
                    on_click=lambda _: self.page.go("/new-task"),
                )
            ],
        )