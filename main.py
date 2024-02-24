# main.py

from number_conversions import integer_binary, binary_complement, hexadecimal_decimal, decimal_hexadecimal

def main():
    print("Bienvenido a tu conversor de binarios, decimales y hexadecimales :)")
    print("Comencemos!")
    try:
        # Integer to 8-bit binary conversion
        number = int(input("Ingresa un decimal en rango de (0-255) para convertirlo en binario de 8 bits:"))
        binary_number = integer_binary(number)
        print(f"Binario de 8 bits: {binary_number}")

        # Binary to two's complement conversion
        binary_input = input("Ingresa un binario de 8 bits para calcular su complemento a dos: ")
        twos_complement = binary_complement(binary_input)
        print(f"Complemento a dos: {twos_complement}")

        # Hexadecimal conversions
        hex_input = input("Ingresa un hexadecimal de 3 numeros para calcular su decimal: ")
        decimal_output = hexadecimal_decimal(hex_input)
        print(f"Decimal: {decimal_output}")

        decimal_input = int(input("Ingresa un decimal entre (0-4095) para convertirlo en hexadecimal: "))
        hex_output = decimal_hexadecimal(decimal_input)
        print(f"Hexadecimal: {hex_output}")

    except ValueError as e:
        print(e)
    
    print("Fin :)")

if __name__ == "__main__":
    main()
