from import_export import resources
from Bike.models import Bike

class MemberResource(resources.ModelResource):
	class Meta:
		model = Bike