from django.db import models

# Create your models here.
class Post(models.Model): #物件繼承models.Model
    title=models.CharField(max_length=200) #字元/長度
    slug=models.CharField(max_length=200)
    body=models.TextField()#長文字 不用長度
    pub_date=models.DateTimeField(auto_now_add=True)#日期(自動取得現在時間)
    class Meta: 
        ordering=('-pub_date',)#ordering 排序(反向日期排序) 
     
    def __str__(self) -> str: #-- python內建 --
        return   self.title