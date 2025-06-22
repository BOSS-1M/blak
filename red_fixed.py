
# ملف تشغيل للوحدة المشفرة red_fixed.cpython-312.so
import red_fixed

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(red_fixed, 'main'):
    red_fixed.main()
else:
    print("تم استيراد red_fixed بنجاح، ولكن لا توجد دالة main للتشغيل.")
