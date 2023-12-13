from django.db import models

# Create your models here.
class Post(models.Model): #物件繼承models.Model
    title=models.CharField(max_length=200) #字元/長度
    slug=models.CharField(max_length=200)
    body=models.TextField()#長文字 不用長度
    category=models.TextField(null=True)
    pub_date=models.DateTimeField(auto_now_add=True)#日期(自動取得現在時間)
    class Meta: 
        ordering=('-pub_date',)#ordering 排序(反向日期排序) 
     
    def __str__(self) -> str: #-- python內建 --
        return   self.title
    
class Comment(models.Model):
        post=models.ForeignKey(Post,on_delete=models.CASCADE)
        text=models.CharField(max_length=200)
        pub_date=models.DateTimeField(auto_now_add=True)

    
class Product(models.Model):
    SIZES = (
        ('S', 'Smaill'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES) #choices下拉式選單
    result=models.BooleanField()