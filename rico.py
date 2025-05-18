
# ملف تشغيل للوحدة المشفرة ricoz.cpython-312.so
import ricoz

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(ricoz, 'main'):
    ricoz.main()
else:
    print("تم استيراد ricoz بنجاح، ولكن لا توجد دالة main للتشغيل.")
