from django.db import models

#Install this library and import it to improve the password security | Parol xavfsizligini yaxshilash uchun ushbu kutubxonani o'rnating va import qiling
from django_cryptography.fields import encrypt
#Run this on terminal to install it | Bu kutubhonani o'rnatish uchun kerak bo'lgan terminal komandasi
#pip install django-cryptography





#If you're facing this error: | Agar siz bu error bilan yuzmayuz kelayotgan bolsangiz:
#ImportError: cannot import name 'baseconv' from 'django.utils'


#Install this: | Buni o'raning:
#pip install "git+https://github.com/saurav-codes/django-cryptography"

# Create your models here.

class Creator(models.Model): #same as user
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=16, unique=True) #Cheking username is unique or not | Username takrorlanmaganligini tekshirish
    email = models.EmailField(max_length=255)
    _password = encrypt(models.CharField(max_length=20)) #Encrypting the password | Parolni yashirish
    
    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name_plural = 'Creators'

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Creator, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'

    
class News_posts(models.Model):
    img_p = models.ImageField(upload_to = 'posts/img') #"p" means post
    videos_p = models.FileField(upload_to = 'posts/videos')
    post = models.ForeignKey(News, on_delete = models.CASCADE) 
    
    def __str__(self):
        return self.post.title
                
    class Meta:
        verbose_name_plural = 'News_posts'

        
class Post_comments(models.Model):
    author = models.ForeignKey(Creator, on_delete = models.CASCADE)
    comment_p = models.ForeignKey(News, on_delete = models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return f"{self.author.username} : {self.comment_p.title}"

    class Meta:
        verbose_name_plural = 'Post_comments'
