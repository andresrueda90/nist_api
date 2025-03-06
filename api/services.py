import logging

from .repositories import NISTRepository
from .models import VulnerabilityModel


class NISTService:
    @staticmethod
    def fetch_and_store_vulnerabilities():
        data = NISTRepository.get_vulnerabilities()

        if data["error"]:
            return {"error": data["error"]}

        vulnerabilities = data.get("response", []).get("vulnerabilities", [])

        count = 0
        for vuln in vulnerabilities:
            cve_id = vuln["cve"]["id"]
            base_severity = vuln["cve"].get("metrics", {}).get("cvssMetricV2", [{}])[0].get("baseSeverity", "Unknown")

            if not VulnerabilityModel.objects.filter(cve_id=cve_id).exists():
                count += 1
                VulnerabilityModel.objects.create(cve_id=cve_id, base_severity=base_severity)

        return {"msg": f"Saved {count} vulnerabilities"}

    @staticmethod
    def fetch_and_store_vulnerabilities_by_cveid(cve_id: str):
        data = NISTRepository.get_vulnerabilities_by_cveid(cve_id)

        if data["error"]:
            return {"error": data["error"]}

        vulnerabilities = data.get("response", []).get("vulnerabilities", [])

        count = 0
        for vuln in vulnerabilities:
            cve_id = vuln["cve"]["id"]
            base_severity = vuln["cve"].get("metrics", {}).get("cvssMetricV2", [{}])[0].get("baseSeverity", "Unknown")

            if not VulnerabilityModel.objects.filter(cve_id=cve_id).exists():
                count += 1
                VulnerabilityModel.objects.create(cve_id=cve_id, base_severity=base_severity)

        return {"msg": f"Saved {count} vulnerabilities"}
