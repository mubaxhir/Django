from django.db.models import CharField,DateField,Model
from django.urls import reverse
from django_mysql.models import ListCharField
# Create your models here.

class Todo(Model):
    date = DateField('date_purchased')
    products = ListCharField(
        base_field=CharField(max_length=20),
        size=10,
        max_length=(10 * 21)
    )

    # def get_absolute_url(self):
    #     return reverse("todo:todo-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"