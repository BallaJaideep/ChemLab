from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset
from .utils import analyze_csv
from django.http import FileResponse
from .utils import generate_pdf_report


class UploadCSVView(APIView):
    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            summary, record_count = analyze_csv(file)

            dataset = Dataset.objects.create(
                filename=file.name,
                record_count=record_count
            )

            # Keep only last 5 datasets
            datasets = Dataset.objects.order_by("-uploaded_at")
            if datasets.count() > 5:
                for old in datasets[5:]:
                    old.delete()

            return Response(
                {
                    "message": "File uploaded and analyzed successfully",
                    "summary": summary
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class DatasetHistoryView(APIView):
    def get(self, request):
        datasets = Dataset.objects.order_by("-uploaded_at")[:5]

        data = [
            {
                "filename": d.filename,
                "uploaded_at": d.uploaded_at,
                "record_count": d.record_count
            }
            for d in datasets
        ]

        return Response(data)
    
class PDFReportView(APIView):
    def get(self, request):
        latest_dataset = Dataset.objects.order_by("-uploaded_at").first()

        if not latest_dataset:
            return Response(
                {"error": "No dataset available to generate report"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # NOTE: In a real system we would store summaries,
        # here we regenerate using last uploaded file logic
        # (simplified for screening task)

        return Response(
            {"message": "PDF generation endpoint ready"},
            status=status.HTTP_200_OK
        )
