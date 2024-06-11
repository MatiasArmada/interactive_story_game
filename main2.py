import json
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
        content["text"],
        font_family=story["font"],
        size=20,
        color=ft.colors.WHITE,  # Color de las letras blanco
        alignment=ft.Alignment.CENTER  # Centrar el texto horizontalmente
    )
    page.controls.append(text_control)

    # Configurar el contenedor de los botones con una animación de aparición suave
    button_container = ft.Container(
        layout=ft.FlexLayout(direction=ft.FlexDirection.COLUMN, align_items=ft.Align.CENTER),  # Centrar los botones verticalmente
        width="100%",  # Ancho del contenedor igual al ancho de la página
        margin="10px 0",  # Margen superior e inferior de 10px
        animations=[ft.Animation(opacity=1, duration=0.5)]  # Animación de opacidad que hace que los botones aparezcan suavemente en 0.5 segundos
    )

    # Agregar las opciones como botones con el estilo personalizado
    for option in content["options"]:
        button = ft.ElevatedButton(
            text=option["text"],
            on_click=lambda e, opt=option: on_option_selected(page, story, opt["next"]),
            bgcolor=ft.colors.BLACK,  # Fondo de los botones negro
            color=ft.colors.WHITE     # Texto de los botones blanco
        )
        button_container.add(button)

    page.controls.append(button_container)

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
