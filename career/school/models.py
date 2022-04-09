from django.db.models import CharField, ForeignKey, PositiveIntegerField, DateTimeField, BooleanField, CASCADE, TextField, Model
# Create your models here.
class SchoolBuffer(Model):
    id = PositiveIntegerField(blank=False, null=False, primary_key=True)
    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)
    name = CharField(max_length=255,blank=False,null=False)
    standard = CharField(max_length=255,blank=False,null=False)
    address = CharField(max_length=255,blank=False,null=False)
    username = CharField(max_length=255,blank=False, null=False)
    password = CharField(max_length=255,blank=False,null=False)
    board_id = PositiveIntegerField(blank=False,null=False)
    status = PositiveIntegerField(default=1)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def clean(self):
        '''
        find and clean existing entries for user
        '''

    def save(self, *args, **kwargs):
        self.clean()
        super(SchoolBuffer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'School Buffer'
        verbose_name = 'School Buffer'
        
