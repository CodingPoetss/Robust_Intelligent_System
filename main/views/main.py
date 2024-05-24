# python learning
# coding time: 2023/8/31 15:53
from django.shortcuts import render, redirect, HttpResponse
from recognition.models import LicensePlateInfo
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from main.utils.Bootstrap import BootStrapModelForm
from datetime import datetime
import os


def main_handle(request):
    image = LicensePlateInfo.objects.filter(id=1).first()
    return render(request, 'main.html', {'image': image})


@csrf_exempt
def main_test(request):
    if request.method == 'POST':  # post方式
        user = "xxx"
        plate_number = "xxx"
        # recognition_time = request.POST.get('recognition_time')
        # 识别日期是当前的时间
        recognition_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_list = request.FILES.get('file')
        print(file_list)

        base_path = os.path.join(settings.MEDIA_ROOT, 'Images')  # 基础路径，使用 settings.MEDIA_ROOT
        if not os.path.exists(base_path):
            os.makedirs(base_path, exist_ok=True)  # 如果文件夹不存在，创建它

        # for rec_file in file_list:  # 每一张图片进行循环
        #     file_path = os.path.join(base_path, "dropzone")  # 加上文件名，构建完整的文件保存路径
        #     with open(file_path, 'wb') as f:
        #         f.write(rec_file.read())
        for k, file_obj in request.FILES.items():  # 获取前端传过来的文件数据
            with open('%s/%s' % (base_path, 'dropzone.png'), "wb") as f:  # 打开文件
                for chunk in file_obj.chunks():
                    f.write(chunk)  # chunk方式写入文件

        # 保存到数据库
        for rec_file in file_list:
            LicensePlateInfo.objects.create(user=user, plate_number=plate_number, recognition_time=recognition_time,
                                            file=rec_file)


    return render(request, 'dropzone_demo.html')




