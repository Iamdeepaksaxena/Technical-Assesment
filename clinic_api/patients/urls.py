from django.urls import path, include
from .views import LoginView
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    AppointmentViewSet,
    StatsView,
    UpcomingAppointmentsView,
    LoginView
)


router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', StatsView.as_view()),
    path('appointments/upcoming/', UpcomingAppointmentsView.as_view()),

    # ✅ Task 4.1
    path('auth/login/', LoginView.as_view()),
]