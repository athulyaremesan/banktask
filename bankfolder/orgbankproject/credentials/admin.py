from django.contrib import admin
from.models import Person,City,District,AccountType
# Register your models here.
admin.site.register(Person)
admin.site.register(City)
admin.site.register(District)
admin.site.register(AccountType)