import flet as ft
from Project.UI.components.custom_routing import screens_handler
from Project.UI.config.general_config import general_config
# from Project.UI.components.custom_appbar import CustomAppBar

def main(page: ft.Page):
    general_config(page)

    def route_changer(route):
        page.views.clear()
        page.views.append(
            screens_handler(page)[page.route]
        )

    page.on_route_change = route_changer
    page.go("/")


ft.app( target=main )
