import flet as ft

from Project.UI.screens.new_task_screen import NewTaskScreen

def screens_handler(page: ft.Page):
    return {
        '/': ft.View(
            route='/',
            controls=[
                NewTaskScreen(page)
            ]
        ),
        '/segunda': ft.View(
            route='/segunda',
            controls=[
                ft.Container(
                    content=ft.Text("segunda pagina")
                )
            ]
        ),
    }