# 🔍 Detector de Plágio Simples

Ferramenta em Python para comparar dois textos e calcular o grau de similaridade entre eles, identificando possíveis plágios.

---

## 📋 Sobre o projeto

O programa utiliza duas métricas clássicas de similaridade textual para analisar se um texto foi copiado ou fortemente baseado em outro.

**Métricas utilizadas:**
- **Similaridade de Jaccard** — compara conjuntos de n-gramas (sequências de palavras) entre os textos
- **Similaridade Cosseno** — compara a frequência de palavras usando vetores matemáticos

**Fórmulas de cálculo:**
```
Jaccard  = |Interseção| ÷ |União| dos n-gramas
Cosseno  = (A · B) ÷ (|A| × |B|)
Índice   = (Jaccard × 50%) + (Cosseno × 50%)
```

**Classificação do resultado:**

| Nível | Faixa | Significado |
|-------|-------|-------------|
| 🟢 NENHUM | < 25% | Textos bastante distintos |
| 🟡 BAIXO | 25–49% | Alguma semelhança encontrada |
| 🟠 MÉDIO | 50–79% | Textos com grande semelhança |
| 🔴 ALTO | ≥ 80% | Provável plágio detectado |

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

- Python 3.8+
- Bibliotecas nativas: `os`, `re`, `collections`
- Testes com `pytest`

---

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/DeluxeOfc/detector-plagio-python.git
cd detector-plagio-python
```

### 2. (Opcional) Instale as dependências para testes
```bash
pip install -r requirements.txt
```

### 3. Execute o programa
```bash
python detector.py
```

### 4. Escolha o modo de uso

**Modo 1 — Digitar os textos diretamente:**
```
[1] Comparar dois textos digitados
```
Cole ou digite os dois textos e pressione Enter duas vezes para finalizar cada um.

**Modo 2 — Comparar arquivos .txt:**
```
[2] Comparar dois arquivos .txt
```
Informe o caminho dos arquivos. Exemplos de teste estão na pasta `textos_exemplo/`.

---

## 🖥️ Exemplo de saída

```
=======================================================
        DETECTOR DE PLÁGIO — RESULTADO
=======================================================
  📄 texto_original.txt: 89 palavras
  📄 texto_plagiado.txt: 85 palavras
-------------------------------------------------------
  Similaridade Jaccard (n-gramas): 42.31%
  Similaridade Cosseno (palavras): 78.54%
  Índice geral de similaridade:    60.42%
-------------------------------------------------------
  Nível de plágio: 🟠 MÉDIO
  Textos com grande semelhança.
-------------------------------------------------------
  Palavras em comum (21):
  aprendizado, área, computação, criar, decisões, ...
=======================================================
```

---

## 🧪 Rodando os testes

```bash
python -m pytest tests.py -v
```

Resultado esperado: **19 testes passando**.

---

## 📁 Estrutura do projeto

```
detector-plagio-python/
│
├── detector.py              # Código principal
├── tests.py                 # 19 testes unitários
├── requirements.txt         # Dependências
├── README.md                # Documentação
├── LICENSE                  # Licença MIT
│
└── textos_exemplo/
    ├── texto_original.txt   # Texto base para teste
    ├── texto_plagiado.txt   # Versão com plágio
    └── texto_diferente.txt  # Texto sem relação
```

---

## 📚 Conceitos aplicados

- Processamento de linguagem natural (NLP) básico
- Algoritmo de similaridade de Jaccard
- Similaridade cosseno com vetores de frequência
- Geração de n-gramas
- Testes unitários com pytest
- Boas práticas de código Python (type hints, docstrings)

---

## 👤 Autor

Feito por **[DeluxeOfc](https://github.com/DeluxeOfc)**

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
