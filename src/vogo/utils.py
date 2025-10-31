import re
from typing import List

def contar_ocurrencias(texto: str, patron: str) -> int:

    try:
        return len(re.findall(patron, texto))
    except re.error:
        raise ValueError(f"Patrón regex inválido: {patron}")


def buscar_elemento(elementos: List[str], elemento: str) -> bool:

    return elemento.lower() in [e.lower() for e in elementos]
