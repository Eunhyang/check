from django.urls import include, path

app_name = 'check'
urlpatterns = [
    path('note/', include('note.api.urls', namespace='note')),
]
