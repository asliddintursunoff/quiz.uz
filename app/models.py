from django.db import models
# from ckeditor.fields  import RichTextField

class Fanlar(models.Model):
    fan = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to="rasm")
    
    def __str__(self):
        return self.fan
    
    class Meta:
        verbose_name = "Test nomi "
        verbose_name_plural = "Test nomlari "      



    
#     class Meta:
#         verbose_name = "Daraja "
#         verbose_name_plural = "Test Darajalari "    
        
              
class Test(models.Model):
    fan = models.ForeignKey(Fanlar,on_delete=models.CASCADE)
    
    savol = models.TextField( )
    javob1 = models.CharField( max_length=200)
    javob2 = models.CharField( max_length=200)
    javob3 = models.CharField( max_length=500)
    tugri_javob = models.CharField( max_length=500)
    
    def ID(self):
        return self.id
    
    class Meta:
        verbose_name = "Test "
        verbose_name_plural = "Testlar "   

class Level(models.Model):
    pass
