
# ملف تشغيل للوحدة المشفرة rico1.cpython-312.so
import rico1

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(rico1, 'main'):
    rico1.main()
else:
    print("تم استيراد rico1 بنجاح، ولكن لا توجد دالة main للتشغيل.")
