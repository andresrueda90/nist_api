from django.urls import path

from api.views import VulnerabilityView, VulnerabilityStatusView, UnfixedVulnerabilitiesView, VulnerabilitySummaryView, \
    LoadNISTVulnerabilitiesView

urlpatterns = [
    path('load-nist-vulnerabilities/', LoadNISTVulnerabilitiesView.as_view(), name='load_nist_vulnerabilities'),
    path('vulnerabilities/', VulnerabilityView.as_view(), name='vulnerabilities'),
    path("vulnerabilities/summary/", VulnerabilitySummaryView.as_view(), name="vulnerability-summary"),
    path('vulnerability-status/', VulnerabilityStatusView.as_view(), name='vulnerability_status'),
    path('vulnerability-unfixed/', UnfixedVulnerabilitiesView.as_view(), name='vulnerability_unfixed')
]
