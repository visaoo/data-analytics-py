from src.api import buscar_comentarios
from src.dados import processar_dados, calcular_estatisticas, exibir_resultados
from src.visualizacao import criar_graficos, salvar_csv
from src.utils import medir_tempo, executar_testes

@medir_tempo
def analise_completa():
    """
    Fazendo busca na api, processamento, estatísticas e visualização
    """
    print("ANÁLISE COMPLETA")
    print("=" * 45)
    try:
        dados = buscar_comentarios()
        if not dados:
            return

        df = processar_dados(dados)
        stats = calcular_estatisticas(df)
        exibir_resultados(stats)

        arquivo_grafico = criar_graficos(df)
        arquivo_csv = salvar_csv(df)
        print(f"\nConcluído!")
        print(f"Arquivos: {arquivo_grafico}, {arquivo_csv}")
    except Exception as e:
        print(f"Erro durante a análise: {e}")
        print("Tente executar: python main.py teste")


def analise_rapida():
    """Análise rápida"""
    print("ANÁLISE RÁPIDA")
    print("=" * 35)

    dados = buscar_comentarios()
    if dados:
        df = processar_dados(dados)
        stats = calcular_estatisticas(df)
        print(f"\n{stats['total']} comentários de {stats['posts_unicos']} posts")
        print(f"Média: {stats['tamanho_medio']:.0f} caracteres")
        print(f"Palavras: {stats['palavras_media']:.1f} por comentário")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "rapido":
            analise_rapida()
        elif sys.argv[1] == "teste":
            executar_testes()
        else:
            print("Uso: python main.py [rapido|teste]")
    else:
        analise_completa()
