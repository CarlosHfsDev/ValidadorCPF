🔐 CPF Validator API — FastAPI

API REST desenvolvida em Python para validação completa de CPF com base na regra oficial do módulo 11.

O projeto foi construído com foco em boas práticas de backend, separação de responsabilidade e validação robusta de domínio.

🎯 Objetivo

Demonstrar:

Tradução de regra de negócio em algoritmo determinístico

Validação de entrada (sanitização e consistência)

Estruturação de serviço HTTP com FastAPI

Exposição de lógica como endpoint REST

Organização limpa de código

Este projeto faz parte de uma sequência prática voltada para fortalecimento de fundamentos backend.

🧠 Regra implementada

A validação inclui:

Remoção automática de caracteres não numéricos

Verificação de tamanho (11 dígitos)

Bloqueio de sequências repetidas (ex: 00000000000)

Cálculo dos dois dígitos verificadores via módulo 11

Comparação final com a entrada original

🚀 Stack

Python 3

FastAPI

Uvicorn

🔎 Endpoint
GET /validar-cpf/{cpf}
Exemplo de resposta
{
  "cpf": "41431039071",
  "valido": true
}
▶️ Executando localmente
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
python -m uvicorn teste:app --reload

Acesse a documentação automática em:

http://127.0.0.1:8000/docs
📌 Próximos passos planejados

Implementação de testes automatizados com pytest

Containerização com Docker

Estruturação em camadas (service + router)

Deploy em ambiente cloud
