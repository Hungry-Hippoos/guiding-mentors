from django.db.models import CharField, ForeignKey, PositiveIntegerField, DateTimeField, BooleanField, CASCADE, TextField, Model, FileField
# Create your models here.
class RecordBuffer(Model):
    id = PositiveIntegerField(blank=False, null=False, primary_key=True)
    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)
    file = FileField()
    school_id = PositiveIntegerField(blank=False, null=False)
    status = PositiveIntegerField(default=1)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def clean(self):
        '''
        find and clean existing entries for user
        '''

    def save(self, *args, **kwargs):
        self.clean()
        super(RecordBuffer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Record Buffer'
        verbose_name = 'Record Buffer'
        
class testQuestions(Model):
    id = PositiveIntegerField(blank=False, null=False, primary_key=True)
    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True) 
    question = CharField(max_length=255,blank=False,null=False)
    status = PositiveIntegerField(default=1)

class testOptions(Model):
    id = PositiveIntegerField(blank=False, null=False, primary_key=True)
    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True) 
    value = CharField(max_length=255),
    question_id = PositiveIntegerField(blank=False,null=False)
    status = PositiveIntegerField(default=1)