from django import template
import re

register = template.Library()

@register.filter
def format_id(value):
    """
    Formatea CUIT/CUIL/DNI según su longitud.
    Ejemplos:
    - 20301234567 -> 20-30123456-7
    - 30123456 -> 30.123.456
    """
    if not value:
        return "-"
    
    # Eliminar cualquier caracter no numérico
    value = re.sub(r"\D", "", str(value))

    if len(value) == 11:
        # Formato CUIT/CUIL
        return f"{value[:2]}-{value[2:4]}.{value[4:7]}.{value[7:10]}-{value[10:]}"
    elif len(value) == 8:
        # Formato DNI
        return f"{value[:2]}.{value[2:5]}.{value[5:]}"
    else:
        return value
