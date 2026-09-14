<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Saneamento-Classificador%20de%20Consumo-00A86B?style=for-the-badge&logo=water&logoColor=white" alt="Saneamento">
</p>

<h1 align="center">💧 Classificador de Consumo de Água</h1>

<p align="center">
  Uma aplicação simples em Python para classificar o perfil de consumo de água de imóveis e emitir alertas educativos.
</p>

## 📌 Sobre o projeto

O **Classificador de Consumo de Água** foi desenvolvido para apoiar a campanha de conscientização ambiental da companhia de saneamento da cidade. O sistema solicita ao usuário o tipo de imóvel e o consumo mensal de água, classificando o perfil de consumo e exibindo mensagens educativas para incentivar o uso consciente da água.

O projeto foi criado para praticar entrada de dados, estrutura condicional com `match/case`, lógica de programação e exibição de resultados em Python. 🐍

## 🎯 Objetivo do sistema

- Classificar o consumo de água de diferentes tipos de imóveis.
- Exibir mensagens educativas conforme o perfil de consumo.
- Incentivar práticas de economia de água.
- Praticar conceitos fundamentais de programação em Python.

## 🛠️ Linguagem utilizada

- **Python 3.10+** (uso de `match/case` para estrutura condicional)

## 📋 Regras de classificação

O programa aplica as seguintes regras de negócio:

| Tipo de Imóvel | Consumo (m³) | Mensagem Exibida |
|----------------|--------------|------------------|
| Comercial | Qualquer valor | Tarifa comercial aplicada – consulte o plano corporativo |
| Apartamento | < 10 | Consumo econômico – excelente controle de água! |
| Apartamento ou Casa | ≤ 25 | Consumo moderado – dentro do padrão residencial |
| Outros casos | > 25 | Consumo excessivo – adote medidas de economia e verifique vazamentos |

## ▶️ Como executar

### Pré-requisitos

- Ter o [Python](https://www.python.org/downloads/) 3.10 ou superior instalado.
- Ter acesso a um terminal ou ao Visual Studio Code.

### Execução pelo terminal

1. Clone o repositório:

```bash
git clone [https://github.com/Prada-07/desconto-progressivo.git](https://github.com/Prada-07/desconto-progressivo.git)
```

2. Acesse a pasta do projeto:

```bash
cd desconto-progressivo
```

3. Execute o programa:

```bash
python app.py
```

4. Informe o tipo de imóvel (`comercial`, `casa` ou `apartamento`) e o consumo mensal em metros cúbicos.

## 💻 Exemplo de resultado

```text
Digite seu tipo de imóvel:
-> apartamento
Digite o consumo mensal em metros cúbicos:
-> 8

Consumo econômico - excelente controle de água!
```

## 📁 Estrutura do projeto

```text
desconto-progressivo/
├── app.py       # Código principal do classificador
└── README.md    # Documentação do projeto
```

## ℹ️ Observação

As mensagens exibidas são educativas e têm como objetivo conscientizar o usuário sobre o consumo de água. O programa não realiza cálculos de tarifa ou cobrança, apenas classifica o perfil de consumo.

## 👤 Autor

Desenvolvido por **Leonardo Prada**.

[![GitHub](https://img.shields.io/badge/Leonardo%20Prada-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prada-07)

---

<p align="center">💧 Projeto desenvolvido para fins educacionais.</p>
