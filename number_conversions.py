# number_conversions

def integer_binary(number):
    """
    Convierte un número entero a un número binario de 8 bits.
    :param number: int
    :return: Cadena binaria de 8 bits
    """
    if number < 0 or number > 255:
        raise ValueError("El número debe estar en el rango de 0 a 255.")
    return format(number, '08b')

def binary_complement(binary_number):
    """
    Convierte un número binario de 8 bits a su representación en complemento a dos.
    :param binary_number: Cadena binaria de 8 bits
    :return: Cadena binaria de 8 bits en complemento a dos
    """
    if len(binary_number) != 8 or not all(c in '01' for c in binary_number):
        raise ValueError("La entrada debe ser un número binario de 8 bits.")
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_number)
    twos_complement = format((int(inverted, 2) + 1) & 0xFF, '08b')
    return twos_complement

def hexadecimal_decimal(hex_number):
    """
    Convierte un número hexadecimal de 3 dígitos a decimal.
    :param hex_number: Cadena de número hexadecimal de 3 dígitos
    :return: Número decimal
    """
    if len(hex_number) != 3:
        raise ValueError("El número hexadecimal debe ser de 3 dígitos.")
    return int(hex_number, 16)

def decimal_hexadecimal(decimal_number):
    """
    Convierte un número decimal a un hexadecimal de 3 dígitos.
    :param decimal_number: Número decimal
    :return: Cadena hexadecimal de 3 dígitos
    """
    if decimal_number < 0 or decimal_number > 0xFFF:
        raise ValueError("El número debe estar en el rango de 0 a 4095.")
    return format(decimal_number, '03X')
