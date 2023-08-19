import flet as ft
from UI.config.general_config import general_config
from UI.components.custom_appbar import CustomAppBar

def main(page: ft.Page):
    general_config(page)

    page.add(
        CustomAppBar,
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Hola desde el main screen"),
                ]
            )
        ),
    )

ft.app( target=main )
