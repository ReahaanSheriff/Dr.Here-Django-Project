from djongo import models
# Create your models here.

class p_det(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()


class d_det(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()


class pat_ap(models.Model):
    ap_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dept = models.CharField(max_length=20)
    mob_no = models.IntegerField()
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    address = models.CharField(max_length=75)
    message = models.CharField(max_length=100)
    doc_name = models.CharField(max_length=30, default='NULL')


class d_profile(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    prof_pic = models.ImageField(upload_to='pics')
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    door_no = models.IntegerField()
    st_name = models.CharField(max_length=100)
    area = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField()
    degree = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    exp = models.IntegerField()
    id_no = models.IntegerField(primary_key=True)
    id_proof = models.ImageField(upload_to='id')
    hos_name = models.CharField(max_length=50)
    hos_door_no = models.IntegerField()
    hos_st_name = models.CharField(max_length=100)
    hos_area = models.CharField(max_length=25)
    hos_city = models.CharField(max_length=25)
    hos_state = models.CharField(max_length=25)
    hos_zip_code = models.IntegerField()
    verified = models.CharField(max_length=10, default='NO')
