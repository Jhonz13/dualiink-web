#!/bin/bash
# Script para iniciar el servidor local HTTPS

if [ ! -f "cert.pem" ] || [ ! -f "key.pem" ]; then
    echo "Certificados no encontrados. Generando nuevos certificados..."
    ./generar_certificados.sh
fi

echo "Iniciando servidor de desarrollo en Python..."
python3 server_tls.py
