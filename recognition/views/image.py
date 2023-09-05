# python learning
# coding time: 2023/8/31 20:50
from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
from django.shortcuts import render, HttpResponse
from recognition.models import LicensePlateInfo
from accounts.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
import os
from datetime import datetime
from django.http import JsonResponse


@csrf_exempt
def image_upload(request):
    if request.method == 'GET':
        return render(request, 'image_upload.html')

    # 获取POST表单
    # user = request.POST.get('user')
    # plate_number = request.POST.get('plate_number')
    user = "xxx"
    plate_number = "xxx"
    # recognition_time = request.POST.get('recognition_time')
    # 识别日期是当前的时间
    recognition_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_list = request.FILES.get('file')
    print(file_list)

    base_path = os.path.join(settings.MEDIA_ROOT, 'Images')  # 基础路径，使用 settings.MEDIA_ROOT
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # 如果文件夹不存在，创建它

    for rec_file in file_list:  # 每一张图片进行循环
        file_path = os.path.join(base_path, rec_file.name)  # 加上文件名，构建完整的文件保存路径
        with open(file_path, 'wb') as f:
            f.write(rec_file.read())

    # 保存到数据库
    for rec_file in file_list:
        LicensePlateInfo.objects.create(user=user, plate_number=plate_number, recognition_time=recognition_time,
                                        file=rec_file)

    return JsonResponse({'status': True})


def image_display(request):
    model_objects = LicensePlateInfo.objects
    # search_contains = "plate_number__contains"
    search_contains = "user__contains"
    from main.utils.pagination import Pagination
    page_object = Pagination(request, model_objects, search_contains)
    context = {'data_list': page_object.data_list,
               'search_data': page_object.search_data,
               'page_string': page_object.page_string,
               }
    return render(request, 'image_display.html', context)


def image_download(request, image_id):
    image = LicensePlateInfo.objects.get(pk=image_id)
    file_path = image.file.path
    print(file_path)

    # 获取文件的MIME类型
    content_type, encoding = mimetypes.guess_type(file_path)
    print(content_type)
    print(image.file.name)

    if not content_type or not content_type.startswith('image/'):
        content_type = 'application/octet-stream'

    # 构建HTTP响应
    response = HttpResponse(FileWrapper(open(file_path, 'rb')), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{image.file.name}"'

    return response


def image_delete(request):
    uid = request.GET.get('uid')
    exists = LicensePlateInfo.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({'status': False, 'error': '删除失败！！数据不存在！'})
    LicensePlateInfo.objects.filter(id=uid).delete()
    return JsonResponse({'status': True})


def image_edit_find(request):
    edit_id = request.GET.get("edit_id")
    row_dict = LicensePlateInfo.objects.filter(id=edit_id).values("plate_number").first()
    if not row_dict:
        return JsonResponse({'status': False, 'error': '数据不存在或已被删除'})
    result = {
        'status': True,
        'data': row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def image_edit(request):
    plate_number = request.POST.get('plate_number')
    edit_number = request.POST.get('edit_number')
    edit_obj = LicensePlateInfo.objects.filter(id=edit_number)
    if not plate_number:
        return JsonResponse({'status': False, 'error': '输入不能为空！', 'blank': True})
    if not edit_obj:
        return JsonResponse({'status': False, 'error': '该数据不存在或已被删除！'})
    edit_obj.update(plate_number=plate_number)
    return JsonResponse({'status': True})



