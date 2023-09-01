from flet import Column, Text, ElevatedButton, Page, MainAxisAlignment, CrossAxisAlignment

def HomeScreen(page: Page):
    screen = Column(
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing= 30,
        controls = [
            Text(
                "Bienvenido \n app gestor de tareas",
                size= 30,
                text_align= "center",
                overflow= "ellipsis",
                max_lines= 2,
            ),
            ElevatedButton(
                text="Ingresar",
                on_click=lambda _: page.go('/principal'),
                width= 200,
            )
        ]
    )

    return screen