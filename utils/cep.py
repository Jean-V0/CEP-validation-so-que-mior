CEP_RANGES = (
    ("SP", 1000000, 19999999),
    ("RJ", 20000000, 28999999),
    ("ES", 29000000, 29999999),
    ("MG", 30000000, 39999999),
    ("BA", 40000000, 48999999),
    ("SE", 49000000, 49999999),
    ("PE", 50000000, 56999999),
    ("AL", 57000000, 57999999),
    ("PB", 58000000, 58999999),
    ("RN", 59000000, 59999999),
    ("CE", 60000000, 63999999),
    ("PI", 64000000, 64999999),
    ("MA", 65000000, 65999999),
    ("PA", 66000000, 68899999),
    ("AP", 68900000, 68999999),
    ("AM", 69000000, 69899999),
    ("RR", 69300000, 69399999),
    ("AC", 69900000, 69999999),
    ("DF", 70000000, 72799999),
    ("DF", 73000000, 73699999),
    ("GO", 72800000, 72999999),
    ("GO", 73700000, 76799999),
    ("RO", 76800000, 76999999),
    ("TO", 77000000, 77999999),
    ("MT", 78000000, 78899999),
    ("MS", 79000000, 79999999),
    ("PR", 80000000, 87999999),
    ("SC", 88000000, 89999999),
    ("RS", 90000000, 99999999),
)

async def _normalize_cep(cep: str) -> str:
    return cep.strip().replace("-", "").replace(".", "").replace(" ", "").zfill(8)


async def if_cep_is_number(cep: str) -> bool:
    """
    Valida CEP (8 digitos, apenas numeros).
    Retorna True/False.
    """
    cep = await _normalize_cep(cep)
    return len(cep) == 8 and cep.isdigit()


async def if_cep_has_state(cep: str) -> bool:
    """
    Valida se o CEP pertence a alguma faixa de CEP do Brasil.
    """
    cep = await _normalize_cep(cep)
    if not await if_cep_is_number(cep):
        return False

    cep_numero = int(cep)
    return any(inicio <= cep_numero <= fim for _, inicio, fim in CEP_RANGES)


async def validar_cep(cep: str):
    cep = await _normalize_cep(cep)
    if not await if_cep_is_number(cep):
        return False
    if not await if_cep_has_state(cep):
        return False
    ## TODO: Validar CEP via API (BrasilAPI, ViaCEP, OpenCEP)
    #if not await consultar_api(cep):
        return False
    return True
