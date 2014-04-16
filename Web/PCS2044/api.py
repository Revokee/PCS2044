from tastypie.resources import Resource, ModelResource
from string import upper
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse
from tastypie import fields
from tastypie import http 
from django.contrib.auth.models import User

# superclass that adds CORS headers to the generated response from a resource
class CORSResource(Resource):
    """
    Adds CORS headers to resources that subclass this.
    """
    def create_response(self, *args, **kwargs):
        response = super(CORSResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = "Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Type"
        return response
 
    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []
 
        request_method = request.method.lower()
        allows = ','.join(map(str.upper, allowed))
 
        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = "Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Type"
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)
 
        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)
 
        return request_method

#Base Extended Abstract Model
class BaseModelResource(CORSResource, ModelResource):
    """
    Abstract class sample with template data for the models
    """
    class Meta:
        abstract = True
        """
        excludes = ['creation_time', 'modification_time', 'deleted']
        authentication = authorization.ApiKeyAuthenticationExtended()
        serializer = Serializer(formats=['json'])
        paginator_class = Paginator
        cache = SimpleCache()
        """

# common user resource
# TODO: define fields to show
class UserResource(BaseModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username','email'] 
		allowed_methods = ['get']