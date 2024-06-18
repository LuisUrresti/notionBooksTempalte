import requests
import json

# Tu token de integración de Notion
NOTION_TOKEN = 'secret_5veglVGI6Wip8LKpd8Cqw2Wj7tYzDTM99nAC6NctxgL'
PAGE_ID = '6642f8d91e04418ca9a4ff640ccb39af'  # Reemplaza con tu database_id

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Crear la base de datos de libros
def create_database():
    url = 'https://api.notion.com/v1/databases'
    data = {
        "parent": {"type": "page_id", "page_id": PAGE_ID},
        "title": [
            {
                "type": "text",
                "text": {
                    "content": "Lista de Libros"
                }
            }
        ],
        "properties": {
            "Título": {"title": {}},
            "Autor": {"rich_text": {}},
            "Editorial": {"rich_text": {}},
            "Fecha de Lectura": {"date": {}},
            "Leído": {"checkbox": {}}
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        database_id = response.json().get('id')
        print("Base de datos creada exitosamente.")
        return database_id
    else:
        print(f"Error al crear la base de datos: {response.content}")



print(create_database())


