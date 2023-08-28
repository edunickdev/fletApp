import flet as ft

def change_theme(self):
    if self.page.theme_mode == ft.ThemeMode.LIGHT:
        iconTheme.icon = ft.icons.DARK_MODE
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()
    else:
        iconTheme.icon = ft.icons.SUNNY
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

iconTheme = ft.IconButton(icon=ft.icons.DARK_MODE, on_click=change_theme)

CustomAppBar =  ft.AppBar(
        title=ft.Text("TODO APP"),
        actions=[
            # ft.IconButton( icon=ft.icons.MENU ),
            # TODO configurar menú personalizado
            # ft.IconButton( icon=ft.icons.SEARCH ),
            # TODO configurar busqueda de tareas por palabras clave
            iconTheme
        ],
        center_title=True
    )


