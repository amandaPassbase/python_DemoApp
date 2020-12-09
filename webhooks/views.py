
from __future__ import print_function
import json
import time
import passbase
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from passbase.rest import ApiException
from pprint import pprint
from .models import User

@csrf_exempt
@require_POST
def passbaseWebhook(request):
    jsondata = request.body
    data = json.loads(jsondata)
    identityAccessKey = data['key']
    print(identityAccessKey)

    configuration = passbase.Configuration()
    configuration.api_key['X-API-KEY'] = 'SECRET_API_KEY'

    api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
    id = identityAccessKey
    identityAccessKey_instance = User.objects.create(identityAccessKey=id)
    

    try:
        api_response = api_instance.get_identity_by_id(id)
        print(api_response)
        email = api_response['id']
        print(email)
        status = api_response['status']
        print(status)
        
        email_instance = User.objects.create(name=email)
        status_instance = User.objects.create(status=status)

    except ApiException as e:
        print("Exception when calling IdentityApi->get_identity_by_id: %s\n" % e)

    return HttpResponse(status=200)
