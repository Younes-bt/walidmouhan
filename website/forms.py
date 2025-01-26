from django import forms
from .models import Article, YoutubeVideos, User, Profile

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category','title', 'imgUrl', 'content', 'pdfUrlView', 'resume', 'pdfUrlDownload', 'magazin', 'puplished_day', 'pdfID']  
        labels = {
            'category': 'نوع المقال',
            'title': 'عنوان المقال',
            'imgUrl': 'صورة واجهة المقال',
            'content': 'نص المقال',
            'pdfUrlView': 'رابط الملف',
            'pdfUrlDownload': 'رابط التحميل المباشر للملف',
            'magazin': 'المجلة الناشرة للمقال',
            'puplished_day': 'تاريخ نشر المقال',
            'pdfID': 'رابط الملف',
            'resume': 'ملخص'
            
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'نوع المقال', 'id':'article-cat'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-input-txt', 'placeholder': 'ضع العنوان هنا', 'id':'artcile_title'}),
            'resume': forms.Textarea(attrs={'class': 'form-control form-input-txt', 'placeholder': 'ضع الملخص هنا', 'id':'artcile_resume'}),
            'imgUrl': forms.FileInput(attrs={'class': 'form-control','id':'article-image', 'placeholder': 'ضع العنوان هنا'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id':'artcile_content', 'placeholder': ' قم بكتابة المقال هنا'}),
            'pdfID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط الملف PDF - ID', 'id':'article-id'}),
            'pdfUrlView': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط الملف PDF'}),
            'pdfUrlDownload': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط تحميل الملف PDF'}),
            'magazin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المجلة الناشرة للمقال', 'id':'magazin-id'}),
            'puplished_day': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id':'puplished_day-id'})
        }



class YtbVids(forms.ModelForm):
    class Meta:
        model = YoutubeVideos
        fields = ['vidLink','title']  
        labels = {
            'vidLink': 'رابط الفيديو',
            'title': 'عنوان الفيديو',
        }
        widgets = {
            'vidLink': forms.TextInput(attrs={'class': 'form-control form-input-txt', 'placeholder': 'ضع العنوان هنا', 'id':'video-Link'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-input-txt', 'placeholder': 'ضع العنوان هنا', 'id':'video_title'}),
        }
        

class Profile_edit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'pict', 'city', 'profession', 'university', 'phone']
        labels = {
            'full_name': 'الإسم الكامل',
            'phone':'رقم الهاتف',
            'pict': 'صورة البروفايل',
            'city':'المدينة',
            'profession':'الحالة',
            'university':'الجامعة',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-input-txt', 'placeholder': 'مثال: وليد موحن', 'id':'fullname', 'aria-describedby':"fullname-help"}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-input-txt', 'placeholder': 'مثال: 0606060606', 'id':'phone', 'aria-describedby':"phone-help"}),
            'pict': forms.FileInput(attrs={'class': 'form-control form-input-txt','id':'profilePict', 'aria-describedby':"profilePict-help"}),
            'city': forms.Select(attrs={'class': 'form-control form-input-txt', 'placeholder': 'المدينة', 'id':'city', 'aria-describedby':"city-help"}),
            'profession': forms.Select(attrs={'class': 'form-control form-input-txt', 'placeholder': 'طالب/موظف', 'id':'profession', 'aria-describedby':"profession-help"}),
            'university': forms.Select(attrs={'class': 'form-control form-input-txt', 'placeholder': 'الجامعة/الكلية', 'id':'university', 'aria-describedby':"university-help"}),
        }