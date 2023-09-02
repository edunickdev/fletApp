from flet import Page, Column, ListTile, Text, Icon, icons, IconButton, MainAxisAlignment, ScrollMode, Card, Row, ElevatedButton

from Project.sources.connection_firebase_db import get_data

task_list = get_data('task')

my_ListTiles = []
for key, value in task_list.items():
    if value['category'] == 'Personal':
        value['icon'] = icons.TODAY
    elif value['category'] == 'Trabajo':
        value['icon'] = icons.WORK
    elif value['category'] == 'Estudio':
        value['icon'] = icons.BOOK
    elif value['category'] == 'Ócio':
        value['icon'] = icons.WEEKEND
    elif value['category'] == 'Familiar':
        value['icon'] = icons.FAMILY_RESTROOM

    my_ListTiles.append(
        ListTile(
            leading=Icon(value['icon']),
            title=Text(value['title']),
            subtitle=Text(value['description']),
            trailing=IconButton(
                    icon=icons.DELETE,
                    on_click=lambda _: print('delete'),
                    selected_icon_color='red',
                ),
            )
        )


def GeneralScreen(page: Page):
    page.update()
    page.scroll = True
    screen = Card(
        width= 650,
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton( 'Nueva tarea', on_click=lambda _: page.go('/new-task') ),
                Column(
                    scroll=ScrollMode.AUTO,
                    controls=[
                        tile for tile in my_ListTiles
                    ]
                ),
            ]
        )
    )

    
    return screen

# pyinstaller --add-data "Project/sources/bdflet-firebase-adminsdk-mdm4q-0b51280ea8.json;Project/sources/" .\main.py
