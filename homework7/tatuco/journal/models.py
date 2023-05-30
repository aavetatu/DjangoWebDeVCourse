from django.db import models
from datetime import datetime
	
class Log(models.Model):
	name = models.CharField(max_length=160)
	created = models.DateField(default=datetime.now, blank=False)
	description = models.TextField(blank=True)
	STATUSES = (
		('NOT COMPLETED', 'Not Completed'),
		('COMPLETED', 'Completed'),
	)
		
	status = models.CharField(max_length=20, null=False, choices=STATUSES, default=STATUSES[0][0])
	
	def __str__(self):
		if self.status:
			return f"{self.name} - {self.get_status_display()}"
		else:
			return self.name

