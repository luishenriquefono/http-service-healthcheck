"""
CLI de Monitoramento e Health Check de Endpoints HTTP.
Executa probes em endpoints, calcula latência e verifica conformidade HTTP.
"""

import json
import time
import urllib.error
import urllib.request

ENDPOINTS = [
    {"nome": "JSONPlaceholder API", "url": "https://jsonplaceholder.typicode.com/posts/1"},
    {"nome": "Open-Meteo Weather API", "url": "https://api.open-meteo.com/v1/forecast?latitude=0&longitude=0"},
    {"nome": "Endpoint Inexistente (Simulação de Erro)", "url": "https://httpstat.us/404"},
]


def testar_endpoint(servico: dict) -> dict:
    url = servico["url"]
    inicio = time.perf_counter()

    resultado = {
        "nome": servico["nome"],
        "url": url,
        "status_code": None,
        "latencia_ms": None,
        "saudavel": False,
        "erro": None,
    }

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "HealthMonitorBot/1.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as resposta:
            duracao = (time.perf_counter() - inicio) * 1000
            resultado["status_code"] = resposta.status
            resultado["latencia_ms"] = round(duracao, 2)
            resultado["saudavel"] = (200 <= resposta.status < 300)
    except urllib.error.HTTPError as err:
        duracao = (time.perf_counter() - inicio) * 1000
        resultado["status_code"] = err.code
        resultado["latencia_ms"] = round(duracao, 2)
        resultado["erro"] = f"HTTP Error {err.code}"
    except urllib.error.URLError as err:
        resultado["erro"] = f"Falha de rede/DNS: {err.reason}"
    except Exception as err:
        resultado["erro"] = str(err)

    return resultado


def executar_monitoramento(alvos: list[dict]) -> None:
    print(f"Iniciando varredura em {len(alvos)} serviços...\n")
    relatorio = []

    for item in alvos:
        res = testar_endpoint(item)
        relatorio.append(res)

        marcador = "🟢" if res["saudavel"] else "🔴"
        latencia_str = f"{res['latencia_ms']} ms" if res['latencia_ms'] else "N/A"
        print(f"{marcador} {res['nome']:<35} | Status: {str(res['status_code']):<5} | Latência: {latencia_str}")

    # Salva o resultado consolidado
    with open("health_report.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4)

    print("\nRelatório exportado para 'health_report.json'.")


if __name__ == "__main__":
    executar_monitoramento(ENDPOINTS)
