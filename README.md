# 🚀 FastAPI Posts API

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-05998b?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-green?style=for-the-badge&logo=pydantic)](https://docs.pydantic.dev/)

Uma API RESTful simples para gestão de posts, desenvolvida com **FastAPI**. Este projeto foi estruturado em camadas (Controller/Router, Schemas/Views) para demonstrar:

* **Roteamento Modular** (`APIRouter`).
* **Validação de Dados** (`Pydantic`).
* **Mecanismos de Paginação e Filtragem** por *query parameters*.
* **Manipulação de Headers e Cookies**.
* **Separação de Responsabilidades** (MVC simplificado).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework web de alta performance.
* **Pydantic**: Biblioteca para *data parsing* e validação.
* **Uvicorn**: Servidor ASGI utilizado em produção.

---