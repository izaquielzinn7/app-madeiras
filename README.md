# Orçamento de Madeiras (Streamlit)

Aplicação simples feita em Python com Streamlit para calcular o valor de materiais de madeira com base na metragem informada.

---

## Funcionalidades

* Seleção de tipos de madeira (Caibro, Ripa, Linha, Pranchão, Barrote)
* Entrada de metragem por produto
* Cálculo automático de subtotal por item
* Exibição de resumo detalhado
* Cálculo do valor total geral

---

## Tecnologias utilizadas

* Python
* Streamlit

---

## Pré-requisitos

* Python 3.x instalado
* Pip instalado

---

## Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/izaquielzinn7/app-madeiras

# Entre na pasta
cd orcamento-madeira

# Instale as dependências
pip install streamlit

# Execute o app
streamlit run app.py
```

---

## Demonstração

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/f49d956a-71e5-482f-8c82-6fc3e729ca60" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d04655be-4d59-4122-910d-3c255963ad4a" />


---

## Estrutura do projeto

```
orcamento-madeira
 ┣ app.py
 ┣ README.md
 ┗ requirements.txt
```

---

## Como funciona

O usuário informa a metragem desejada para cada tipo de madeira, e o sistema:

1. Multiplica a quantidade pelo preço por metro
2. Calcula o subtotal de cada item
3. Soma todos os valores
4. Exibe o total final

---

## Melhorias futuras

* Exportar orçamento em PDF
* Adicionar mais tipos de madeira
* Editar valores antes do cálculo
* Histórico de orçamentos
* Interface mais avançada

---

## Feito por

**Izaquiel Monteiro**
GitHub: https://github.com/izaquielzinn7

---

## Licença

Este projeto está sob a licença MIT.
