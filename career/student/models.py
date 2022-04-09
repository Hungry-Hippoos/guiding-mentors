from django.db.models import CharField, ForeignKey, PositiveIntegerField, DateTimeField, BooleanField, CASCADE, TextField, Model, AutoField
# Create your models here.
class StudentBuffer(Model):
    id = AutoField(blank=False, null=False, primary_key=True)
    created_on = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)
    name = CharField(max_length=255,blank=False,null=False)
    age= PositiveIntegerField(blank=False,null=False)
    standard = CharField(max_length=255,blank=False,null=False)
    username = CharField(max_length=255,blank=False, null=False)
    password = CharField(max_length=255,blank=False,null=False)
    school_id = PositiveIntegerField(blank=False,null=False)
    course_id = PositiveIntegerField(blank=False,null=False)
    q1 = CharField(max_length=255,null=True)
    q2 = CharField(max_length=255,null=True)
    q3 = CharField(max_length=255,null=True)
    q4 = CharField(max_length=255,null=True)
    q5 = CharField(max_length=255,null=True)
    q6 = CharField(max_length=255,null=True)
    q7 = CharField(max_length=255,null=True)
    skills=CharField(max_length=255,null=True)
    recommended=CharField(max_length=255,null=True)
    status = PositiveIntegerField(default=1)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def clean(self):
        '''
        find and clean existing entries for user
        '''

    def save(self, *args, **kwargs):
        self.clean()
        super(StudentBuffer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Student Buffer'
        verbose_name = 'Student Buffer'