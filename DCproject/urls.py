from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Step1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Step1.views.home, name='home'),
    path('Step1/', include('Step1.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
