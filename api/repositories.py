import requests
from rest_framework.response import Response

NIST_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"  # URL de la API del NIST


class NISTRepository:

    @staticmethod
    def get_vulnerabilities() -> dict:
        try:
            response = requests.get(NIST_API_URL, timeout=60)
            if response.status_code == 200:
                return {"error": False, "msg": "Response ok", "status_code": response.status_code,
                        "response": response.json()}
            return {"error": True, "msg": "Response error", "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": True, "msg": str(e), "status_code": response.status_code}

    @staticmethod
    def get_vulnerabilities_by_cveid(cve_id: str) -> dict:
        try:
            response = requests.get(f"{NIST_API_URL}?cveId={cve_id}", timeout=60)
            if response.status_code == 200:
                return {"error": False, "msg": "Response ok", "status_code": response.status_code,
                        "response": response.json()}
            return {"error": True, "msg": "Response error", "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": True, "msg": str(e), "status_code": response.status_code}
