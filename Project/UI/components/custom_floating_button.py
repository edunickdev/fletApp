import flet as ft

def CustomFloatingButton(page: ft.Page):
    
    customFloatingButtong = ft.FloatingActionButton(
        mini=True,
        icon= ft.icons.ARROW_BACK,
        on_click= lambda _: page.go('/'),
    )

    return customFloatingButtong
