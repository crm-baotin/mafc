from django.contrib import admin
from django.http import HttpResponse
from .models import Lead
import openpyxl
from openpyxl.styles import Font


# ===== ACTION: EXPORT EXCEL =====
def export_leads_excel(modeladmin, request, queryset):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Danh sách Lead"

    # Header
    headers = [
        "Họ và tên",
        "Số điện thoại",
        "Khu vực",
        "Nghề nghiệp",
        "Ngày tạo",
    ]

    ws.append(headers)

    # Bold header
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Data
    for lead in queryset:
        ws.append([
            lead.full_name,
            lead.phone,
            lead.location,
            lead.job,
            lead.created_at.strftime("%d/%m/%Y %H:%M"),
        ])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="leads.xlsx"'

    wb.save(response)
    return response


export_leads_excel.short_description = "⬇️ Xuất Excel Lead đã chọn"


# ===== ADMIN =====
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'location',
        'created_at',
    )

    list_filter = (
        'location',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone',
    )

    ordering = ('-created_at',)

    actions = [export_leads_excel]
