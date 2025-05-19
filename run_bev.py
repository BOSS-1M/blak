
# ملف تشغيل للوحدة المشفرة bev.cpython-312.so
import bev

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(bev, 'main'):
    bev.main()
else:
    print("تم استيراد bev بنجاح، ولكن لا توجد دالة main للتشغيل.")
