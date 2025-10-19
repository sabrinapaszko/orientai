# OrientAI - MVP
Plataforma de orientação universitária com IA.

## Estrutura do Projeto
- **frontend/** – Interface (Vue 3 + Axios)  
- **backend/** – API (Flask + SQLAlchemy)  
- **ai/** – Lógica de IA (Hugging Face)  
- **docs/** – Diagramas, fluxos e documentação  

## Como rodar cada parte
Veja os READMEs internos em cada pasta.

## Tecnologias Principais
- **Frontend:** Vue 3 + Axios  
- **Backend:** Flask + SQLAlchemy  
- **Banco de Dados:** SQLite (desenvolvimento) / PostgreSQL (produção)  
- **IA:** Hugging Face API  
- **Deploy:** Render (backend) + Vercel (frontend)


---

# Backend - OrientAI

## Rodar localmente

1. Criar e ativar o ambiente virtual, instalar dependências e rodar o servidor:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

