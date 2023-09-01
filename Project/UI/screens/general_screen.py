from flet import Page, Column, ListTile, Text, Icon, icons, IconButton, MainAxisAlignment, ScrollMode

from Project.sources.connection_firebase_db import get_data

task_list = get_data('task')
print(task_list)

my_ListTiles = []
for key, value in task_list.items():
    my_ListTiles.append(
        ListTile(
            leading=Icon(icons.TASK),
            title=Text(value['title']),
            subtitle=Text(value['description']),
            trailing=IconButton(
                icon=icons.DELETE,
                on_click=lambda _: print('delete')
            ),
        )
    )

print(my_ListTiles)


def GeneralScreen(page: Page):

    screen = Column(
        scroll=ScrollMode.ALWAYS,
        alignment=MainAxisAlignment.CENTER,   
        controls=[
            tile  for tile in my_ListTiles
        ]
    )
    
    return screen


