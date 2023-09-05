"""
URL configuration for Robust_Intelligent_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from Robust_Intelligent_System import settings
from django.urls import path
from main.views import main
from recognition.views import image


urlpatterns = [
    # 主操作界面
    path('test/', main.main_test),
    path('drop/test/', main.main_test_2),
    path('', main.main_handle),

    # 导入视频流识别界面

    # 导入图片识别界面
    path('image/upload/', image.image_upload),

    # 历史识别查询及搜索界面 or 数据可视化界面
    path('image/display/', image.image_display),
    path('image/download/<int:image_id>/', image.image_download),
    path('image/delete/', image.image_delete),
    path('image/edit/find/', image.image_edit_find),
    path('image/edit/', image.image_edit),
    # 设置界面

    # 跳转界面
]

# 应当导入from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
