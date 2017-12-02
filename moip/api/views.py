import base64

from pip._vendor import requests
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet

from moip.api.serializers import SubscriptionsSerializer
from moip.models import Subscriptions, Client
from moip_django_assinatura.settings import MOIP_TOKEN, MOIP_KEY


class SubscriptionsView(ModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = (AllowAny,)

    @list_route(methods=('post',))
    def create_client(self, request, format=None):
        client = Client.objects.create(name=request.data['fullname'])
        request.data['code'] = client.code
        data = json.dumps(request.data)
        r = requests.post(
            "https://sandbox.moip.com.br/assinaturas/v1/"
            "customers?new_vault=true",
            data=data,
            headers=create_moip_header())
        msg = json.loads(r.text)
        if msg['message'] != "Cliente criado com sucesso":
            client.delete()
        return Response(msg)

    @list_route(methods=('post',))
    def create_subscription(self, request, format=None):
        subscription = Subscriptions.objects.create(
            plano=request.data.get('plan', dict()).get('code'),
            cliente=request.data.get('customer', dict()).get('code'))
        request.data['code'] = subscription.code
        data = json.dumps(request.data)
        register = request.query_params['register']
        r = requests.post(
            "https://sandbox.moip.com.br/assinaturas/"
            "v1/subscriptions?new_customer=" + register,
            data=data,
            headers=create_moip_header())
        return Response(json.loads(r.text))

    @list_route(methods=('get',))
    def get_plans(self, request, format=None):
        r = requests.get("https://sandbox.moip.com.br/assinaturas/v1/plans",
                         headers=create_moip_header()).json()
        plans = [{'code': plan['code'],
                  'name': plan['name']} for plan in r['plans']]
        return Response(plans)

    @list_route(methods=('get',))
    def get_clients(self, request, format=None):
        r = requests.get("https://sandbox.moip.com.br/assinaturas/v1/customers",
                         headers=create_moip_header()).json()
        clients = [{'code': client['code'],
                    'name': client['fullname']} for client in r['customers']]
        return Response(clients)


def create_moip_header():
    token = MOIP_TOKEN + ':' + MOIP_KEY
    headers = {'content-type': 'application/json',
               'Authorization': 'Basic ' +
                                base64.b64encode(token.encode('utf-8')).decode('utf-8')}
    return headers
