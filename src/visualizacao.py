import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def criar_graficos(df: pd.DataFrame) -> str:
    """
    Cria 3 gráficos simples
    1. Histograma do tamanho dos comentários.
    2. Histograma dos comentários com mais de 6 palavras.
    3. Barras dos posts com mais de 20 caracteres.
    E salva como PNG.
    """
    print("Criando gráficos...")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 4))

    # Histograma
    ax1.hist(df['tamanho_corpo'], bins=20, color='skyblue', alpha=0.7)
    ax1.set_title('Tamanho dos Comentários')
    ax1.set_xlabel('Caracteres')
    ax1.grid(True, alpha=0.3)
    
    # Comentarios com mais de 6 palavras
    df_mais_6 = df[df['palavras_corpo'] > 6]
    if not df_mais_6.empty:
        ax2.hist(df_mais_6['palavras_corpo'], bins=20, color='orange', alpha=0.7)
        ax2.set_title('Comentários com Mais de 6 Palavras')
        ax2.set_xlabel('Palavras')
        ax2.grid(True, alpha=0.3)
    
    # Post maiores que 20 caracteres
    df_maiores_20 = df[df['tamanho_corpo'] > 20]
    if not df_maiores_20.empty:
        ax3.bar(range(len(df_maiores_20)), df_maiores_20['tamanho_corpo'], color='purple')
        ax3.set_title('Posts com Mais de 20 Caracteres')
        ax3.set_xlabel('Posts')

    plt.tight_layout()
    arquivo = f"graficos_{datetime.now().strftime('%H%M%S')}.png"
    plt.savefig(arquivo, dpi=150)
    plt.show()
    print(f"Salvo: {arquivo}")
    return arquivo


def salvar_csv(df: pd.DataFrame) -> str | None:
    """
    Salva CSV
    """
    try:
        arquivo = f"dados_{datetime.now().strftime('%H%M%S')}.csv"
        df.to_csv(arquivo, index=False)
        print(f"Salvo: {arquivo}")
        return arquivo
    except PermissionError:
        print("Erro: Sem permissão para escrever no diretório")
        return None
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        return None