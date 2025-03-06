import logging

from django.db import connection
from django.db.models import Exists, OuterRef, Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import VulnerabilityModel, VulnerabilityStatus
from api.response import response_ok_200, response_error_400, response_ok_201, response_error_500
from api.serializers import VulnerabilitySerializer, VulnerabilityStatusSerializer
from api.services import NISTService

# Create your views here.
logger = logging.getLogger("my_app")


class VulnerabilityView(APIView):

    def get(self, request):
        try:
            vulnerabilities = VulnerabilityModel.objects.all()
            serializer = VulnerabilitySerializer(vulnerabilities, many=True)
            return response_ok_200(serializer.data)

        except Exception as e:
            logger.error(e)
            return response_error_500()

    def post(self, request):
        try:
            cve_id = request.data.get("cve_id")
            if not cve_id:
                return response_error_400({"error": "cve_id required"})

            if not VulnerabilityModel.objects.filter(cve_id=cve_id).exists():
                NISTService.fetch_and_store_vulnerabilities_by_cveid(cve_id)

            serializer = VulnerabilitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response_ok_201(serializer.data)

            return response_error_400(serializer.errors)

        except Exception as e:
            logger.error(e)
            return response_error_500()


class VulnerabilityStatusView(APIView):
    STATUS = "fixed"

    def get(self, request):
        statuses = VulnerabilityStatus.objects.all()
        serializer = VulnerabilityStatusSerializer(statuses, many=True)
        return response_ok_200(serializer.data)

    def post(self, request):
        try:
            cve_id = request.data.get("cve_id")
            fix_status = VulnerabilityStatusView.STATUS

            if not cve_id:
                return response_error_400({"error": "cve_id required"})

            vulnerability_status, created = VulnerabilityStatus.objects.update_or_create(
                cve_id=cve_id,
                defaults={"fix_status": fix_status}
            )

            serializer = VulnerabilityStatusSerializer(vulnerability_status)

            if created:
                return response_ok_201(serializer.data)
            else:
                return response_ok_200(serializer.data)

        except Exception as e:
            logger.error(e)
            return response_error_500()


class UnfixedVulnerabilitiesView(APIView):

    def get(self, request):
        try:
            unfixed_vulnerabilities = VulnerabilityModel.objects.annotate(
                has_fix=Exists(VulnerabilityStatus.objects.filter(cve_id=OuterRef('cve_id')))
            ).filter(has_fix=False)

            serializer = VulnerabilitySerializer(unfixed_vulnerabilities, many=True)
            return response_ok_200(serializer.data)

        except Exception as e:
            logger.error(e)
            return response_error_500()


class VulnerabilitySummaryView(APIView):
    def get(self, request):
        try:
            query = """
                SELECT vm.base_severity, COUNT(vm.id) as count
                FROM api_vulnerabilitymodel vm
                LEFT JOIN api_vulnerabilitystatus vs ON vm.cve_id = vs.cve_id
                WHERE vs.cve_id IS NULL
                GROUP BY vm.base_severity
                ORDER BY count DESC
            """

            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

            summary = [{"base_severity": row[0], "count": row[1]} for row in results]

            return response_ok_200(summary)
        except Exception as e:
            logger.error(e)
            return response_error_500()


class LoadNISTVulnerabilitiesView(APIView):

    def post(self, request):
        try:
            result = NISTService.fetch_and_store_vulnerabilities()
            if "error" in result:
                return response_error_500(result)
            return response_ok_201(result)
        except Exception as e:
            logger.error(e)
            return response_error_500()
