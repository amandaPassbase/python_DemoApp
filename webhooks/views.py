
from __future__ import print_function
import json
import time
import os
import passbase
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from passbase.rest import ApiException
from pprint import pprint
from .models import User

# Receive Passbase webhook and call Passbase API with Python Server-Side Library
@csrf_exempt
@require_POST
def passbaseWebhook(request):
    # Receive Webhook
    jsondata = request.body
    data = json.loads(jsondata)
    identityAccessKey = data['key']
    print('identitykey:')
    print(identityAccessKey)

    # Call Passbase API
    configuration = passbase.Configuration()
    configuration.api_key['X-API-KEY'] = os.getenv("PASSBASE_SECRET_KEY")
    api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
    id = identityAccessKey

    try:
        api_response = api_instance.get_identity_by_id(id)
        # print(api_response)
        email = api_response.owner.email
        print(email)
        status = api_response.status
        print(status)
        # Store identity access key, email, and status of verification
        identityAccessKey_instance = User.objects.create(identityAccessKey=id)
        email_instance = User.objects.create(email=email)
        status_instance = User.objects.create(status=status)

    except ApiException as e:
        print("Exception when calling IdentityApi->get_identity_by_id: %s\n" % e)

    return HttpResponse(status=200)
