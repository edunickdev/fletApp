from flet import Column, Text, ElevatedButton, Page

def HomeScreen(page: Page):
    screen = Column(
        spacing= 50,
        controls = [
            Text("Bienvenido a la app de tareas"),
            ElevatedButton(
                text="Ingresar",
                on_click=lambda _: page.go('/new-task')
            )
        ]
    )

    return screen