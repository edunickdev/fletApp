from flet import Page, Container, alignment

from Project.UI.screens.general_screen import GeneralScreen
from Project.UI.screens.new_task_screen import NewTaskScreen
from Project.UI.screens.update_task_screen import UpdateTaskScreen
from Project.UI.screens.home_screen import HomeScreen

class Router:
    def __init__(self, page: Page):
        self.page = page
        self.routes = {
            '/': HomeScreen(page),
            '/edit-task': UpdateTaskScreen(page),
            '/new-task': NewTaskScreen(page),
            '/principal': GeneralScreen(page),
        }
        self.body = Container(
            alignment= alignment.center,
            content= self.routes['/'],
        )

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
