import requests


def buscar_comentarios():
    """Busca comentários da API"""
    print("Buscando comentários...")
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/comments", timeout=10)
        dados = resp.json()
        print(f"{len(dados)} comentários encontrados!")
        return dados
    except Exception as e:
        print(f"Erro: {e}")
        return None