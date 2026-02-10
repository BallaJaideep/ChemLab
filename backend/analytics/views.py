from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse   # ✅ REQUIRED IMPORT

from .models import Dataset
from .utils import analyze_csv, generate_pdf_report


# =========================
# UPLOAD CSV
# =========================
class UploadCSVView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            summary, preview = analyze_csv(file)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        dataset = Dataset.objects.create(
            user=request.user,
            filename=file.name,
            summary=summary,
            preview=preview,
        )

        return Response(
            {
                "id": dataset.id,
                "message": "Upload successful",
                "summary": summary,
                "preview": preview,
            },
            status=status.HTTP_201_CREATED,
        )


# =========================
# HISTORY (LAST 5)
# =========================
class DatasetHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = (
            Dataset.objects
            .filter(user=request.user)
            .order_by("-uploaded_at")[:5]
        )

        data = [
            {
                "id": d.id,
                "filename": d.filename,
                "uploaded_at": d.uploaded_at,
            }
            for d in datasets
        ]

        return Response(data, status=status.HTTP_200_OK)


# =========================
# DATASET DETAIL
# =========================
class DatasetDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        dataset = get_object_or_404(
            Dataset,
            id=dataset_id,
            user=request.user,
        )

        return Response(
            {
                "id": dataset.id,
                "filename": dataset.filename,
                "uploaded_at": dataset.uploaded_at,
                "summary": dataset.summary,
                "preview": dataset.preview,
            },
            status=status.HTTP_200_OK,
        )


# =========================
# PDF DOWNLOAD
# =========================
class DatasetPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        dataset = get_object_or_404(
            Dataset,
            id=dataset_id,
            user=request.user,
        )

        pdf_buffer = generate_pdf_report(
            dataset.filename,
            dataset.summary,
        )

        response = HttpResponse(
            pdf_buffer.getvalue(),
            content_type="application/pdf",
        )

        response["Content-Disposition"] = (
            f'attachment; filename="{dataset.filename}_report.pdf"'
        )

        return response
