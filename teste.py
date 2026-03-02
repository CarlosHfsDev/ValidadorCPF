from fastapi import FastAPI

app = FastAPI()

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if len(set(cpf)) == 1:
        return False

    base_nove = cpf[:9]
    soma_1 = sum(int(d) * p for d, p in zip(base_nove, range(10, 1, -1)))
    resto_1 = (soma_1 * 10) % 11
    digito_1 = resto_1 if resto_1 < 10 else 0

    base_dez = base_nove + str(digito_1)
    soma_2 = sum(int(d) * p for d, p in zip(base_dez, range(11, 1, -1)))
    resto_2 = (soma_2 * 10) % 11
    digito_2 = resto_2 if resto_2 < 10 else 0

    return cpf[-2:] == f"{digito_1}{digito_2}"

@app.get("/validar-cpf/{cpf}")
def validar(cpf: str):
    return {
        "cpf": cpf,
        "valido": validar_cpf(cpf)
    }