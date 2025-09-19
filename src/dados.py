import pandas as pd

def processar_dados(dados):
    """Converte para DataFrame e adiciona colunas"""
    print("Processando...")
    df = pd.DataFrame(dados)
    df['tamanho_nome'] = df['name'].str.len()
    df['tamanho_corpo'] = df['body'].str.len()
    df['palavras_corpo'] = df['body'].str.split().str.len()
    print(f"{df.shape[0]} linhas processadas")
    return df


def calcular_estatisticas(df):
    """Calcula estatísticas básicas"""
    print("Calculando estatísticas...")
    return {
        'total': len(df),
        'posts_unicos': df['postId'].nunique(),
        'tamanho_medio': df['tamanho_corpo'].mean(),
        'palavras_media': df['palavras_corpo'].mean(),
        'maior_comentario': df['tamanho_corpo'].max(),
        'menor_comentario': df['tamanho_corpo'].min()
    }


def exibir_resultados(stats):
    """Mostra resultados"""
    print("\n" + "="*40)
    print("RESULTADOS")
    print("="*40)
    print(f"Total: {stats['total']} comentários")
    print(f"Posts únicos: {stats['posts_unicos']}")
    print(f"Tamanho médio: {stats['tamanho_medio']:.1f} caracteres")
    print(f"Palavras por comentário: {stats['palavras_media']:.1f}")
    print(f"Maior comentário: {stats['maior_comentario']} caracteres")
    print(f"Menor comentário: {stats['menor_comentario']} caracteres")
