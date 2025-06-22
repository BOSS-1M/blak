
# ملف تشغيل للوحدة المشفرة red_fixed_ready.cpython-312.so
import red_fixed_ready

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(red_fixed_ready, 'main'):
    red_fixed_ready.main()
else:
    print("تم استيراد red_fixed_ready بنجاح، ولكن لا توجد دالة main للتشغيل.")
