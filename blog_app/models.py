from django.db import models

# Create your models here.

class TypeDeCulture(models.Model):
    name_culture = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    
    
    
    def __str__(self) -> str:
        return self.name_culture


class CultureAfrica(models.Model):
    type_culture = models.ForeignKey(TypeDeCulture, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=255, unique=True, verbose_name="Titre") 
    image = models.FileField(upload_to='article/', null=True)
    content = models.TextField(null=True,blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    commentary = models.TextField(null=True, blank=True, verbose_name="Votre Commentaire")
    #like = models.ManyToManyField(UserModel, related_name='blog_posts')
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

