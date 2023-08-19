import flet as ft

def general_config(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 600
    page.window_height = 600
    page.window_max_width = 600
    page.window_min_width = 600
    page.window_max_height = 600
    page.window_min_height = 600
    page.title = "TODO APP"
    page.window_center()

