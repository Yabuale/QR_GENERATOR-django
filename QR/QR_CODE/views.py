import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserForm
from django.template import loader
import base64


def generate_qr_code(request):
  if request.method == 'POST':
        url = request.POST.get('url')
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        # Convert the image to bytes for rendering
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        qr_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        context = {
            'url': url,
            'qr_image': qr_image,
        }
        return render(request, 'index.html', context)
  else:
        return render(request, 'index.html')
