# http-service-healthcheck
Monitor leve de disponibilidade de rede construído com a biblioteca padrão (urllib), registrando latência, conformidade com códigos RFC de resposta e persistência de relatórios em JSON.
# 🌐 HTTP Service Healthcheck

Um utilitário CLI em Python puro para monitoramento contínuo de disponibilidade, validação de status HTTP e medição de latência em endpoints e APIs REST.

---

### 📌 Sobre o Projeto

Em arquiteturas modernas de microsserviços e consumo de dados, monitorar a saúde dos endpoints externos e internos é crucial para garantir a confiabilidade da aplicação.

O **HTTP Service Healthcheck** executa probes em uma lista de URLs, calcula o tempo de resposta em milissegundos com precisão de alta performance (`time.perf_counter`), trata falhas de rede de forma graciosa e consolida os resultados em um relatório padronizado em JSON.

---

### ⚙️ Funcionalidades

- **Monitoramento de Endpoints:** Varredura em lote de APIs e serviços web.
- **Medição de Latência:** Cálculo do *Round-Trip Time* (RTT) em milissegundos (ms).
- **Tratamento Resiliente de Erros:** Captura e categorização de exceções de rede (`URLError`), erros de protocolo (`HTTPError`) e quedas de conexão sem interromper o fluxo da aplicação.
- **Feedback Visual no Terminal:** Indicadores claros de status via emojis (`🟢` para status 2xx e `🔴` para falhas/erros).
- **Exportação Estruturada:** Geração automática do arquivo `health_report.json` para consumo por ferramentas de auditoria ou dashboards.
- **Zero Dependências Externas:** Construído utilizando exclusivamente a biblioteca padrão do Python (`urllib.request`, `json`, `time`).

---

### 🚀 Como Executar

#### Pré-requisitos
- Python 3.10 ou superior instalado.

#### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/http-service-healthcheck.git](https://github.com/seu-usuario/http-service-healthcheck.git)
   cd http-service-healthcheck
