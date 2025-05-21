
# ملف تشغيل للوحدة المشفرة venom.cpython-312.so
import venom

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(venom, 'main'):
    venom.main()
else:
    print("تم استيراد venom بنجاح، ولكن لا توجد دالة main للتشغيل.")
