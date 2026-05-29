"""
Detector de Plágio Simples
Autor: DeluxeOfc
Descrição: Compara textos e calcula o grau de similaridade entre eles.
"""

import os
import re
from collections import Counter


def limpar_texto(texto: str) -> str:
    """Remove pontuação, espaços extras e converte para minúsculas."""
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


def tokenizar(texto: str) -> list:
    """Divide o texto em palavras individuais."""
    return limpar_texto(texto).split()


def gerar_ngramas(tokens: list, n: int = 3) -> list:
    """Gera n-gramas a partir de uma lista de tokens."""
    return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


def similaridade_jaccard(conjunto_a: set, conjunto_b: set) -> float:
    """
    Calcula a similaridade de Jaccard entre dois conjuntos.
    Retorna um valor entre 0.0 (nenhuma similaridade) e 1.0 (idênticos).
    """
    if not conjunto_a and not conjunto_b:
        return 1.0
    intersecao = conjunto_a & conjunto_b
    uniao = conjunto_a | conjunto_b
    return len(intersecao) / len(uniao)


def similaridade_cosseno(tokens_a: list, tokens_b: list) -> float:
    """
    Calcula a similaridade cosseno entre dois textos usando frequência de palavras.
    Retorna um valor entre 0.0 e 1.0.
    """
    freq_a = Counter(tokens_a)
    freq_b = Counter(tokens_b)

    palavras = set(freq_a.keys()) | set(freq_b.keys())

    if not palavras:
        return 0.0

    produto_escalar = sum(freq_a[p] * freq_b[p] for p in palavras)
    magnitude_a = sum(v ** 2 for v in freq_a.values()) ** 0.5
    magnitude_b = sum(v ** 2 for v in freq_b.values()) ** 0.5

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return produto_escalar / (magnitude_a * magnitude_b)


def palavras_em_comum(tokens_a: list, tokens_b: list) -> list:
    """Retorna as palavras que aparecem nos dois textos."""
    return sorted(set(tokens_a) & set(tokens_b))


def classificar_similaridade(percentual: float) -> tuple:
    """Classifica o nível de plágio com base no percentual."""
    if percentual >= 80:
        return "🔴 ALTO", "Provável plágio detectado."
    elif percentual >= 50:
        return "🟠 MÉDIO", "Textos com grande semelhança."
    elif percentual >= 25:
        return "🟡 BAIXO", "Alguma semelhança encontrada."
    else:
        return "🟢 NENHUM", "Textos bastante distintos."


def analisar(texto_a: str, texto_b: str, n: int = 3) -> dict:
    """
    Realiza a análise completa de similaridade entre dois textos.
    Retorna um dicionário com todos os resultados.
    """
    tokens_a = tokenizar(texto_a)
    tokens_b = tokenizar(texto_b)

    ngramas_a = set(gerar_ngramas(tokens_a, n))
    ngramas_b = set(gerar_ngramas(tokens_b, n))

    sim_jaccard = similaridade_jaccard(ngramas_a, ngramas_b)
    sim_cosseno = similaridade_cosseno(tokens_a, tokens_b)

    # Média ponderada das duas métricas
    media = (sim_jaccard * 0.5 + sim_cosseno * 0.5) * 100

    nivel, descricao = classificar_similaridade(media)
    comuns = palavras_em_comum(tokens_a, tokens_b)

    return {
        "jaccard": round(sim_jaccard * 100, 2),
        "cosseno": round(sim_cosseno * 100, 2),
        "media": round(media, 2),
        "nivel": nivel,
        "descricao": descricao,
        "palavras_comuns": comuns,
        "total_palavras_a": len(tokens_a),
        "total_palavras_b": len(tokens_b),
    }


def exibir_resultado(resultado: dict, nome_a: str = "Texto A", nome_b: str = "Texto B"):
    """Exibe o resultado da análise de forma formatada no terminal."""
    print("\n" + "=" * 55)
    print("        DETECTOR DE PLÁGIO — RESULTADO")
    print("=" * 55)
    print(f"  📄 {nome_a}: {resultado['total_palavras_a']} palavras")
    print(f"  📄 {nome_b}: {resultado['total_palavras_b']} palavras")
    print("-" * 55)
    print(f"  Similaridade Jaccard (n-gramas): {resultado['jaccard']}%")
    print(f"  Similaridade Cosseno (palavras): {resultado['cosseno']}%")
    print(f"  Índice geral de similaridade:    {resultado['media']}%")
    print("-" * 55)
    print(f"  Nível de plágio: {resultado['nivel']}")
    print(f"  {resultado['descricao']}")

    if resultado['palavras_comuns']:
        print("-" * 55)
        print(f"  Palavras em comum ({len(resultado['palavras_comuns'])}):")
        print("  " + ", ".join(resultado['palavras_comuns'][:20]))
        if len(resultado['palavras_comuns']) > 20:
            print(f"  ... e mais {len(resultado['palavras_comuns']) - 20} palavras.")

    print("=" * 55 + "\n")


def ler_arquivo(caminho: str) -> str:
    """Lê o conteúdo de um arquivo .txt."""
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def menu():
    """Menu interativo para o usuário escolher o modo de uso."""
    print("\n" + "=" * 55)
    print("         🔍 DETECTOR DE PLÁGIO SIMPLES")
    print("=" * 55)
    print("  [1] Comparar dois textos digitados")
    print("  [2] Comparar dois arquivos .txt")
    print("  [0] Sair")
    print("=" * 55)

    opcao = input("  Escolha uma opção: ").strip()

    if opcao == "1":
        print("\nDigite o Texto A (pressione Enter duas vezes para finalizar):")
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)
        texto_a = " ".join(linhas)

        print("\nDigite o Texto B (pressione Enter duas vezes para finalizar):")
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)
        texto_b = " ".join(linhas)

        resultado = analisar(texto_a, texto_b)
        exibir_resultado(resultado, "Texto A", "Texto B")

    elif opcao == "2":
        caminho_a = input("\nCaminho do arquivo A: ").strip()
        caminho_b = input("Caminho do arquivo B: ").strip()
        try:
            texto_a = ler_arquivo(caminho_a)
            texto_b = ler_arquivo(caminho_b)
            resultado = analisar(texto_a, texto_b)
            exibir_resultado(resultado, os.path.basename(caminho_a), os.path.basename(caminho_b))
        except FileNotFoundError as e:
            print(f"\n❌ Erro: {e}")

    elif opcao == "0":
        print("\n  Até logo! 👋\n")
        return False

    else:
        print("\n  ❌ Opção inválida. Tente novamente.")

    return True


if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = menu()
