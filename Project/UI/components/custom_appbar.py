import flet as ft

CustomAppBar =  ft.AppBar(
        title=ft.Text("TODO APP"),
        actions=[
            ft.IconButton( icon=ft.icons.MENU ),
            # TODO configurar menú personalizado
            ft.IconButton( icon=ft.icons.SEARCH ),
            # TODO configurar busqueda de tareas por palabras clave
            
            # TODO configurar el cambio de tema según el botón
            # ft.IconButton( icon=ft.icons.SUNNY ),
            ft.IconButton( icon=ft.icons.DARK_MODE ),
        ],
        center_title=True
    )


