#!/bin/bash
# Script para generar un certificado autofirmado con OpenSSL

echo "Generando certificados TLS autofirmados para entorno local..."

# Se crea un certificado válido por 365 días sin solicitar interacción al usuario (-subj)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=ES/ST=Local/L=Local/O=DuaLink/OU=Desarrollo/CN=localhost"

if [ $? -eq 0 ]; then
    echo "¡Certificados generados exitosamente! (cert.pem y key.pem)"
else
    echo "Hubo un error al generar los certificados."
    exit 1
fi
