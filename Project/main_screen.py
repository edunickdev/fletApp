from flet import Page, app

from Project.UI.config.general_config import general_config


def main(page: Page):
    general_config(page)

    page.go('/')
    page.update()

app( target=main )
