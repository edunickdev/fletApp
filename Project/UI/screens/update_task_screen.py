from flet import Column, Text, ElevatedButton, Page

from Project.UI.components.custom_appbar import CustomAppBar

def UpdateTaskScreen(page: Page):
    screen = Column(
        controls=[
            Text("Update Task Screen"),
            ElevatedButton(
                text="Go to home screen",
                on_click=lambda _: page.go('/')
            )
        ]
    )

    return screen