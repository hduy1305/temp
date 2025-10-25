import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .models import Appointment

class MakeAppointment(APIView):
    def post(self, request):
        data = request.data
        patient_id = data.get("patient_id")
        doctor_id  = data.get("doctor_id")

        # 1. Kiểm tra patient-service qua URL từ settings
        patient_url = f"{settings.PATIENT_SERVICE_URL}/record/{patient_id}"
        patient_resp = requests.get(patient_url)
        if patient_resp.status_code != 200:
            return Response({"error": "Invalid patient"}, status=400)

        # 2. Kiểm tra doctor-service qua URL từ settings
        doctor_url = f"{settings.DOCTOR_SERVICE_URL}/doctor/{doctor_id}"
        doctor_resp = requests.get(doctor_url)
        if doctor_resp.status_code != 200:
            return Response({"error": "Invalid doctor"}, status=400)

        # 3. Validate + lưu appointment vào MongoDB
        serializer = AppointmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        appointment = serializer.save()

        # 4. Trả về kết quả
        return Response(AppointmentSerializer(appointment).data, status=201)
