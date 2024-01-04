import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar
from Project.UI.components.custom_floating_button import CustomFloatingButton
from Project.UI.components.custom_routing import Router

def general_config(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 900
    page.window_height = 600
    page.window_max_width = 900
    page.window_min_width = 900
    page.window_max_height = 600
    page.window_min_height = 600
    page.window_resizable = False
    page.title = "TODO APP con ChatGPT"
    page.window_center()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = False
    page.floating_action_button = CustomFloatingButton(page)
    page.appbar = CustomAppBar
    page.snack_bar = ft.SnackBar( content=ft.Text("sin mensajes que mostrar"))
    myRoutes = Router(page)
    
    page.on_route_change = myRoutes.route_change
    
    page.add(
        ft.SafeArea(
            myRoutes.body,
        )
    )


