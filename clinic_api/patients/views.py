from django.shortcuts import render
from .permissions import IsStaffOrReadOnly

from .permissions import IsStaffOrReadOnly
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer




class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsStaffOrReadOnly]   # ✅ ADD THIS LINE

    # search support
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset
# ✅ Task 2.3 — Appointment API with filtering
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # get query params
        status_param = self.request.query_params.get('status')
        patient_id = self.request.query_params.get('patient_id')

        # filter by status
        if status_param:
            queryset = queryset.filter(status=status_param)

        # filter by patient_id
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset

# Task 3.1   
#✅ Task 3.1 — Stats Endpoint
from rest_framework.views import APIView
from django.db.models import Count

class StatsView(APIView):

    def get(self, request):
        total_patients = Patient.objects.count()
        total_appointments = Appointment.objects.count()

        # group by status
        status_counts = Appointment.objects.values('status').annotate(count=Count('id'))

        return Response({
            "success": True,
            "data": {
                "total_patients": total_patients,
                "total_appointments": total_appointments,
                "status_counts": status_counts
            },
            "message": "Stats fetched successfully"
        })
    

#✅ Task 3.2 — Upcoming Appointments
from django.utils import timezone
from datetime import timedelta

class UpcomingAppointmentsView(APIView):

    def get(self, request):
        now = timezone.now()
        next_week = now + timedelta(days=7)

        appointments = Appointment.objects.filter(
            appointment_date__range=[now, next_week]
        ).order_by('appointment_date')

        serializer = AppointmentSerializer(appointments, many=True)

        return Response({
            "success": True,
            "data": serializer.data,
            "message": "Upcoming appointments"
        })
    

# ✅ Task 4.1 — Login API (Token Authentication)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response({
                "success": False,
                "message": "Invalid credentials"
            }, status=400)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "success": True,
            "token": token.key
        })
    
# ✅ Task 4.3
def custom_response(success, data=None, message=""):
    return Response({
        "success": success,
        "data": data,
        "message": message
    })