from flet import Page, app
import flet as ft

from Project.UI.config.general_config import general_config


def main(page: Page):
    general_config(page)

    page.go('/')

app( target=main )
