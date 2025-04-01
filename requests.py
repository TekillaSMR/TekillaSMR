import requests
import json
from itertools import product

# Diccionario de rutas comunes en APIs
COMMON_ENDPOINTS = [
    "login", "register", "user", "profile", "admin", "api", "data", "search", "posts", "comments"
]

# Payloads de prueba para detectar vulnerabilidades
PAYLOADS = {
    "SQLi": "' OR '1'='1",  # Inyección SQL básica
    "XSS": "<script>alert('XSS')</script>",  # XSS básico
    "SSRF": "http://127.0.0.1:8080"  # Prueba de SSRF
}

def scan_api(base_url):
    vulnerabilities = []
    
    for endpoint in COMMON_ENDPOINTS:
        url = f"{base_url}/{endpoint}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"[+] Encontrado: {url}")
                
                # Probar payloads de ataque
                for vuln_type, payload in PAYLOADS.items():
                    test_response = requests.get(url, params={"input": payload}, timeout=3)
                    if payload in test_response.text:
                        print(f"  [-] Posible {vuln_type} en {url}")
                        vulnerabilities.append({"url": url, "vulnerability": vuln_type})
        except requests.exceptions.RequestException:
            pass
    
    return vulnerabilities

def generate_report(vulnerabilities, output_file="report.json"):
    with open(output_file, "w") as f:
        json.dump(vulnerabilities, f, indent=4)
    print(f"[+] Reporte guardado en {output_file}")

if __name__ == "__main__":
    target_api = input("Introduce la URL de la API objetivo: ")
    vulns = scan_api(target_api)
    generate_report(vulns)
