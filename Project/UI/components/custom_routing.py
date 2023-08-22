import flet as ft

from Project.UI.components.custom_appbar import CustomAppBar
from Project.UI.screens.new_task_screen import NewTaskScreen
from Project.UI.screens.update_task_screen import UpdateTaskScreen
from Project.UI.screens.home_screen import HomeScreen


def screens_handler(page):
    return {
        '/': ft.View(
            route='/',
            appbar=CustomAppBar,
            controls=[
                HomeScreen(page).build(),
            ]
        ),
        '/new-task': ft.View(
            route='/new-task',
            appbar=CustomAppBar,
            controls=[
                NewTaskScreen(page).build(),
            ]
        ),
        '/update-task': ft.View(
            route='/update-task',
            appbar=CustomAppBar,
            controls=[
                UpdateTaskScreen(page).build(),
            ]
        ),
    }