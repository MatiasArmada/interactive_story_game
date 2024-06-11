import json
from time import sleep
import flet as ft

# Función para cargar la historia desde un archivo JSON
def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Función para actualizar la pantalla con una nueva parte de la historia
def update_story_view(page, story, current_index):
    content = story["content"][current_index]

    # Limpiar la página
    page.controls.clear()

    # Agregar el texto de la historia con el estilo personalizado
    text_control = ft.Text(
        "",
        font_family=story["font"],
        size=20,
        color=ft.colors.WHITE  # Color de las letras blanco
    )
    page.controls.append(text_control)
    page.update()
    # Efecto de tecleo
    for char in content["text"]:
        text_control.value += char
        page.update()
        sleep(0.05)  # Ajusta este valor para cambiar la velocidad de tecleo
    # Agregar las opciones como botones con el estilo personalizado
    for option in content["options"]:
        page.controls.append(ft.ElevatedButton(
            text=option["text"],
            on_click=lambda e, opt=option: on_option_selected(page, story, opt["next"]),
            bgcolor=ft.colors.BLACK,  # Fondo de los botones negro
            color=ft.colors.WHITE     # Texto de los botones blanco
        ))

    # Actualizar el fondo de la página y aplicar el estilo
    page.bgcolor = ft.colors.BLACK  # Fondo de la página negro
    page.update()

# Función para manejar la selección de una opción
def on_option_selected(page, story, next_index):
    update_story_view(page, story, next_index)

# Función principal de la aplicación Flet
def main(page: ft.Page):
    page.title = "Interactive Story Game"
    story = load_story("stories/example_story.json")

    # Configurar el fondo y la fuente según la historia
    page.bgcolor = ft.colors.BLACK  # Fondo de la página negro

    # Iniciar la historia desde el primer índice
    update_story_view(page, story, 0)

# Ejecutar la aplicación Flet
ft.app(target=main)

