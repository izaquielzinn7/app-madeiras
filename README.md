Orçamento de Madeiras (Streamlit)

> Aplicação simples feita em Python com Streamlit para calcular o orçamento de materiais de madeira com base na metragem informada.


Funcionalidades

• Seleção de tipos de madeira (Caibro, Ripa, Linha, Pranchão, Barrote).
• Entrada de metragem por produto.
• Cálculo automático de subtotal por item.
• Exibição de resumo detalhado.
• Cálculo do valor total geral.


Tecnologias utilizadas

Python
Streamlit


Pré-requisitos

Python 3.x instalado
Pip instalado


Rodando o projeto

```bash id="run123"
Clone o repositório
git clone https://github.com/izaquielzinn7/app-madeiras

Entre na pasta
cd orcamento-madeira

Instale as dependências
pip install streamlit

Execute o app
streamlit run app.py
```


Demonstração

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3f6f81e4-6b33-45e0-a74a-3908c7c2b329"/>
<img width="1366" height="768" alt="Captura de tela 2026-04-02 131959" src="https://github.com/user-attachments/assets/86664932-6b82-4570-a167-66fb887730ef" />




Estrutura

```id="struct456"
orcamento-madeira
 main.py
 README.md
 requirements.txt
```


Como funciona
O usuário informa a metragem desejada para cada tipo de madeira, e o sistema:

1. Multiplica a quantidade pelo preço por metro
2. Calcula o subtotal de cada item
3. Soma tudo automaticamente
4. Exibe o total final


Melhorias futuras

Exportar orçamento em PDF
Adicionar mais tipos de madeira
Editar preço das madeiras
Histórico de orçamentos
Interface mais avançada

Feito por
Izaquiel Monteiro
GitHub: https://github.com/izaquielzinn7


Licença
Este projeto está sob a licença MIT.
