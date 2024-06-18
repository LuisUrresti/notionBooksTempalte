import requests
import json

# Tu token de integración de Notion
NOTION_TOKEN = 'secret_5veglVGI6Wip8LKpd8Cqw2Wj7tYzDTM99nAC6NctxgL'
DATABASE_ID = '2450d554-2fa3-49ac-9d38-d9efd7a6d811'  # Reemplaza con tu database_id

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

books = [
    {"title": "Elantris", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El imperio final", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El pozo de la ascensión", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El héroe de las eras", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El aliento de los dioses", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El camino de los reyes", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Aleación de ley", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Palabras radiantes", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Sombras de identidad", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Brazales de duelo", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Juramentada", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El ritmo de la guerra", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "El metal perdido", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Trenza del mar esmeralda", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "Yumi y el pintor de pesadillas", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "El hombre iluminado", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "La esperanza de Elantris", "publisher": "Auto publicado", "author": "Sanderson, Brandon"},
    {"title": "El undécimo metal", "publisher": "Crafty Games", "author": "Sanderson, Brandon"},
    {"title": "El alma del emperador", "publisher": "Tachyon Publications", "author": "Sanderson, Brandon"},
    {"title": "Sombras para el silencio en los bosques del infierno", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Sexto del ocaso", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "Alomante Jak y los Pozos de Eltania", "publisher": "Crafty Games", "author": "Sanderson, Brandon"},
    {"title": "Nacidos de la bruma: historia secreta", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "Arcanun Ilimitado: La colección del Cosmere", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Danzante del Filo", "publisher": "Tor Books", "author": "Sanderson, Brandon"},
    {"title": "Esquirla del Amanecer", "publisher": "Dragonsteel Entertainment", "author": "Sanderson, Brandon"},
    {"title": "Escucha la canción del viento", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Pinball 1973", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "La caza del carnero salvaje", "publisher": "Anagrama", "author": "Murakami, Haruki"},
    {"title": "El fin del mundo y un despiadado país de las maravillas", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Tokio blues (Norwegian Wood)", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Baila, baila, baila", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Al sur de la frontera, al oeste del sol", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Crónica del pájaro que da cuerda al mundo", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Sputnik, mi amor", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Kafka en la orilla", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "After Dark", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "1Q84", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Los años de peregrinación del chico sin color", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "La muerte del comendador", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "La ciudad y sus muros inciertos", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "El elefante desaparece", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Después del terremoto", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Sauce ciego, mujer dormida", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Hombres sin mujeres", "publisher": "Tusquets", "author": "Murakami, Haruki"},
    {"title": "Primera persona del singular", "publisher": "Tusquets", "author": "Murakami, Haruki"}
]



def add_book(title, author, publisher):
    url = 'https://api.notion.com/v1/pages'
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Título": {"title": [{"text": {"content": title}}]},
            "Autor": {"rich_text": [{"text": {"content": author}}]},
            "Editorial": {"rich_text": [{"text": {"content": publisher}}]},
            "Leído": {"checkbox": False}
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Libro '{title}' añadido exitosamente.")
    else:
        print(f"Error al añadir el libro: {response.content}")

for book in books:
    add_book(
        title=book["title"],
        author=book["author"],
        publisher=book["publisher"]
    )