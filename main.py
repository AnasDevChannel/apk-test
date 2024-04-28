import flet as ft
from flet import *

body = Container(
    Stack([
        #BG
        Image(
            src="assets/BG.png"
        ),
        #Godot Logo
        Container(
            alignment=alignment.center,
            margin=margin.only(0,25,0,0),
            border_radius=100,
            bgcolor='#a6f0ff',
            content=ft.Image(
                src="assets/godotlogo2.png",
                width=170,
            ),
        ),
        #TXT1
        Container(
            alignment=alignment.center,
            margin=margin.only(0,300,0,0),
            border=ft.border.only(left=border.BorderSide(10, "#150000")),
            border_radius=50,
            bgcolor='#3838ff',
            content=ft.Text(
                value="!أهلا بيك في كورس تعلم جودوت",
                size=25,
                font_family="Arial",
            )
        ),
        #BTN1
        Container(
            alignment=alignment.center,
            margin=margin.only(0,450,0,0),
            content=ElevatedButton(
                icon="GOLF_COURSE_OUTLINED",
                text="ابدأ الان",
                scale=2,
            )
        ),
        #Icon
        Container(
            alignment=alignment.center,
            margin=margin.only(0,520,0,0),
            content=Icon(
                icons.VIDEOGAME_ASSET_ROUNDED,
                size=80,
                rotate=Rotate(3.0),
                opacity=0.5,
            )
        ),
        #Copy
        Container(
            alignment=alignment.bottom_left,
            margin=margin.only(10,610,0,0),
            content= Text(
                value="Copyrights @AnasDev",
                color='#0a04b8',
                size=15
            )
        ),
    ])
)

def main(page: ft.Page):
    page.title = "كورس تعلم جودوت"
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.add(
        body
    )


ft.app(main)
