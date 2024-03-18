import psutil
import time

def medir_trafego_rede(intervalo_segundos=1):
    # Loop infinito para medir continuamente o tráfego de rede
    while True:
        # Obtém estatísticas de rede
        estatisticas_rede = psutil.net_io_counters(pernic=True)

        # Exibe as estatísticas de cada interface de rede
        for interface, estatisticas in estatisticas_rede.items():
            print(f"Interface: {interface}")
            print(f"  Bytes Recebidos: {estatisticas.bytes_recv}")
            print(f"  Bytes Enviados: {estatisticas.bytes_sent}")

        # Aguarda o intervalo especificado antes de medir novamente
        time.sleep(intervalo_segundos)

# Inicializa a medição do tráfego de rede
medir_trafego_rede()
