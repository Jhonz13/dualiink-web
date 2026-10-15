#!/usr/bin/env python3
import http.server
import ssl
import sys
import os

PORT = 4443

# Comprobamos que existan los certificados
if not os.path.exists("cert.pem") or not os.path.exists("key.pem"):
    print("Error: No se encontraron cert.pem o key.pem.")
    print("Por favor, ejecuta primero './generar_certificados.sh'")
    sys.exit(1)

server_address = ('localhost', PORT)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Envolvemos el socket del servidor con SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Servidor HTTPS ejecutándose en https://localhost:{PORT}")
print("Presiona Ctrl+C para detenerlo.")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nDeteniendo servidor...")
    httpd.server_close()
