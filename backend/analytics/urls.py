from django.urls import path
from .views import (
    UploadCSVView,
    DatasetHistoryView,
    DatasetDetailView,
    DatasetPDFView,
)

urlpatterns = [
    path("upload/", UploadCSVView.as_view()),
    path("history/", DatasetHistoryView.as_view()),
    path("dataset/<int:dataset_id>/", DatasetDetailView.as_view()),
    path("dataset/<int:dataset_id>/pdf/", DatasetPDFView.as_view()),
]
