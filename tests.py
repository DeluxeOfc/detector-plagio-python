"""
Testes unitários para o Detector de Plágio Simples.
Execute com: python -m pytest tests.py -v
"""

import pytest
from detector import (
    limpar_texto,
    tokenizar,
    gerar_ngramas,
    similaridade_jaccard,
    similaridade_cosseno,
    classificar_similaridade,
    analisar,
)


class TestLimparTexto:
    def test_remove_pontuacao(self):
        assert limpar_texto("Olá, mundo!") == "olá mundo"

    def test_converte_minusculas(self):
        assert limpar_texto("PYTHON") == "python"

    def test_remove_espacos_extras(self):
        assert limpar_texto("texto   com   espaços") == "texto com espaços"


class TestTokenizar:
    def test_divide_em_palavras(self):
        assert tokenizar("olá mundo") == ["olá", "mundo"]

    def test_texto_vazio(self):
        assert tokenizar("") == []


class TestNgramas:
    def test_bigramas(self):
        tokens = ["a", "b", "c", "d"]
        resultado = gerar_ngramas(tokens, n=2)
        assert resultado == [("a", "b"), ("b", "c"), ("c", "d")]

    def test_tokens_insuficientes(self):
        tokens = ["a", "b"]
        assert gerar_ngramas(tokens, n=3) == []


class TestSimilaridadeJaccard:
    def test_conjuntos_identicos(self):
        a = {("a", "b"), ("b", "c")}
        assert similaridade_jaccard(a, a) == 1.0

    def test_conjuntos_sem_intersecao(self):
        a = {("a", "b")}
        b = {("c", "d")}
        assert similaridade_jaccard(a, b) == 0.0

    def test_conjuntos_vazios(self):
        assert similaridade_jaccard(set(), set()) == 1.0


class TestSimilaridadeCosseno:
    def test_textos_identicos(self):
        tokens = ["python", "é", "incrível"]
        assert round(similaridade_cosseno(tokens, tokens), 2) == 1.0

    def test_textos_sem_palavras_comuns(self):
        a = ["gato", "cachorro"]
        b = ["avião", "navio"]
        assert similaridade_cosseno(a, b) == 0.0


class TestClassificarSimilaridade:
    def test_alto(self):
        nivel, _ = classificar_similaridade(85)
        assert "ALTO" in nivel

    def test_medio(self):
        nivel, _ = classificar_similaridade(60)
        assert "MÉDIO" in nivel

    def test_baixo(self):
        nivel, _ = classificar_similaridade(30)
        assert "BAIXO" in nivel

    def test_nenhum(self):
        nivel, _ = classificar_similaridade(10)
        assert "NENHUM" in nivel


class TestAnalisar:
    def test_textos_iguais_retorna_alto(self):
        texto = "Python é uma linguagem de programação muito popular no mundo"
        resultado = analisar(texto, texto)
        assert resultado["media"] > 80

    def test_textos_diferentes_retorna_baixo(self):
        a = "O gato dormia tranquilamente sobre o sofá azul"
        b = "A nave espacial decolou rapidamente em direção às estrelas"
        resultado = analisar(a, b)
        assert resultado["media"] < 30

    def test_resultado_tem_campos_obrigatorios(self):
        resultado = analisar("texto um", "texto dois")
        campos = ["jaccard", "cosseno", "media", "nivel", "descricao", "palavras_comuns"]
        for campo in campos:
            assert campo in resultado
