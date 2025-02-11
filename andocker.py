import socket
import re

def enviar_mensaje_udp(ip, puerto, mensaje):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(mensaje.encode("utf-8"), (ip, puerto))
    except Exception as e:
        mostrar_popup("Error de Ejecución", str(e))

def mostrar_popup(titulo, mensaje):
    print(f"[{titulo}] {mensaje}")

def validar_ip_puerto(ip, puerto):
    try:
        socket.inet_aton(ip)
        if not (0 <= puerto <= 65535):
            raise ValueError("El puerto debe estar entre 0 y 65535.")
    except Exception as e:
        raise ValueError(f"IP o puerto inválido: {e}")


def iniciar_escaneo_automatico(ip, puerto):
    validar_ip_puerto(ip, puerto)
    print("Presiona 'ENTER' para enviar el código o 'ESC' para salir.")
    codigo = ""
    
    while True:
        try:
            # Usamos input() para capturar la entrada del usuario
            codigo = input("Escanea el código: ")  # Espera por una línea de entrada

            if codigo.lower() == "salir":  # Detecta 'esc' como una entrada
                print("Finalizando programa.")
                break
                
            elif codigo:  # Verifica si la longitud del código es válida
                enviar_mensaje_udp(ip, puerto, codigo)  # Envía el código
                print(f"Enviado: {codigo}")
            
        except Exception as e:
            mostrar_popup("Error de Lectura", str(e))

# Dirección IP y puerto de destino
ip = "192.168.12.2"  # Cambia a la IP de destino
puerto = 8000   # Cambia al puerto de destino

# Iniciar el escaneo y envío automático
iniciar_escaneo_automatico(ip, puerto)