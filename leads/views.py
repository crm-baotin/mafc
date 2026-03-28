from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Lead
from .telegram import send_telegram


def submit(request):
    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')

        # ===== CHECK RỖNG =====
        if not phone:
            return redirect('/')

        # ===== CHỐNG SPAM =====
        time_limit = timezone.now() - timedelta(hours=24)

        count = Lead.objects.filter(
            phone=phone,
            created_at__gte=time_limit
        ).count()

        if count >= 2:
            return render(
                request,
                'leads/landing_mafc.html',
                {
                    'spam_warning': 'Số điện thoại này đã gửi yêu cầu nhiều lần trong hôm nay. Vui lòng chờ hoặc liên hệ trực tiếp để được hỗ trợ.'
                }
            )

        # ===== LƯU LEAD =====
        Lead.objects.create(
            full_name=full_name,
            phone=phone,
            location=location,
        )

        # ===== GỬI TELE =====
        now_time = timezone.localtime().strftime("%H:%M – %d/%m/%Y")

        msg = f"""
📥 <b>LEAD MỚI – Bảo Tín</b>

👤 Họ tên: {full_name}
📞 SĐT: {phone}
📍 Khu vực: {location}

⏰ Thời gian: {now_time}
🌐 Nguồn: Bảo Tín Finance
        """

        try:
            send_telegram(msg.strip())
        except:
            pass

        return redirect('/success/')

    return redirect('/')


def home(request):
    return render(request, 'pages/index.html')


def page(request, slug):
    return render(request, f'pages/{slug}.html')

from django.http import HttpResponse

def ping(request):
    return HttpResponse("ok")