import pandas as pd
import time
from unittest.mock import patch
from src.dados import calcular_estatisticas, processar_dados
from src.api import buscar_comentarios

def medir_tempo(func):
    """Decorator para medir tempo"""
    def wrapper(*args):
        inicio = time.time()
        resultado = func(*args)
        fim = time.time()
        print(f"Tempo: {fim - inicio:.2f}s")
        return resultado

    return wrapper


def executar_testes():
    """Testes básicos dos módulos"""
    print("EXECUTANDO TESTES")

    # Teste 1: Processar dados
    dados_teste = [
        {"postId": 1, "name": "Teste", "body": "Comentário teste"},
        {"postId": 2, "name": "Outro", "body": "Segundo comentário"},
    ]
    
    df = processar_dados(dados_teste)
    assert len(df) == 2, "Erro: dados não processados"
    assert "tamanho_corpo" in df.columns, "Erro: coluna não criada"
    print("Teste processamento: OK")

    # Teste 2: Estatísticas
    stats = calcular_estatisticas(df)
    assert stats["total"] == 2, "Erro: contagem incorreta"
    assert stats["posts_unicos"] == 2, "Erro: posts únicos"
    print("Teste estatísticas: OK")
    
    # Teste 3: Mock API
    with patch("src.api.buscar_comentarios") as mock_api:
        mock_api.return_value = [
            {"postId": 1, "name": "Mock", "body": "Mock comment"}
        ]
        
        dados = buscar_comentarios()
        
        assert dados is not None and len(dados) == 500
        assert dados is not None and dados[0]['postId'] == 1
        print("Teste API mock: OK")
        
    print("Todos os testes passaram!")
