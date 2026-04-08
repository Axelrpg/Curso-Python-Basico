# Codificacion UTF-8

cadena = "Hola Mundo"
cadena_utf8 = cadena.encode("utf-8")
print(cadena_utf8)

cadena_decodificada = cadena_utf8.decode("utf-8")
print(cadena_decodificada)

# Cadena con caracteres especiales y emojis
cadena_especial = "¡Hola, Mundo!, ¿Como están? 👋"
cadena_especial_utf8 = cadena_especial.encode("utf-8")
print(cadena_especial_utf8)

cadena_especial_decodificada = cadena_especial_utf8.decode("utf-8")
print(cadena_especial_decodificada)

# Obtener el codigo de punto unicode del emoji
emoji = "👋"
codigo_punto = ord(emoji)
print(f"El código de punto Unicode del emoji '{emoji}' es: U+{codigo_punto:X}")