from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        self.password
        return self.username

class Team(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    students = models.ManyToManyField(User, related_name="all_students_enrolled", blank=True)

    def __str__(self):
        return self.team_name

class Experiment(models.Model):
    source = models.TextField(blank=True)
    exp_name = models.CharField(max_length=100,blank=True)
    aim = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    calculations = models.ImageField(upload_to='exp_images' ,blank=True)
    precautions = models.TextField(blank=True)

    def __str__(self):
        return self.exp_name


class Experiment_Assignment(models.Model):
    exp = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    due_date = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    student_name = models.CharField(max_length=25, blank=True)
    student_enroll_num = models.CharField(max_length=50, blank=True)
    student_email = models.EmailField(blank=True)
    submission_file = models.FileField(upload_to='submission_files',blank=True)

    def __str__(self):
        self.student_enroll_num
        return self.student_name


class Chat(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    message = models.TextField(blank=True)
    is_file = models.BooleanField(default=False, blank=True)
    chat_file = models.FileField(upload_to='chat_files' ,blank=True)


class User_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email  =models.EmailField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images' ,blank=True)
    organization = models.CharField(max_length=15, default="not selected", blank=True)
    contact = models.CharField(max_length=15 ,default='+911234567890', blank=True)
    teams = models.ManyToManyField(Team, related_name="all_teams_enrolled", blank=True)
    # alerts

    def __str__(self):
        return self.contact  
    