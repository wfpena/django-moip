(function() {
    'use strict';
    angular.module('app').controller('UserCtrl', function($scope, $http, $element, moipService) {

        var vm = this;
        vm.cliente = {
            "code": "cliente02",
            "email": "nome@exemplo.com.br",
            "fullname": "Nome Sobrenome",
            "cpf": "22222222222",
            "phone_area_code": "11",
            "phone_number": "934343434",
            "birthdate_day": "26",
            "birthdate_month": "04",
            "birthdate_year": "1980",
            "address": {
                "street": "Rua Nome da Rua",
                "number": "100",
                "complement": "Casa",
                "district": "Nome do Bairro",
                "city": "São Paulo",
                "state": "sp",
                "country": "BRA",
                "zipcode": "05015010"
            },
            "billing_info": {
                "credit_card": {
                    "holder_name": "Nome Completo",
                    "number": "4111111111111111",
                    "expiration_month": "04",
                    "expiration_year": "18"
                }
            }
        };

        vm.assinatura = {
            "plan": {
                "code": "plano01"
            },
            "payment_method": "CREDIT_CARD",
            "customer": {
                "code": "cliente01",
                "email": "nome@exemplo.com.br",
                "fullname": "Nome Sobrenome",
                "cpf": "22222222222",
                "phone_number": "934343434",
                "phone_area_code": "11",
                "birthdate_day": "26",
                "birthdate_month": "04",
                "birthdate_year": "1986",
                "address": {
                    "street": "Rua nome da Rua",
                    "number": "170",
                    "complement": "Casa",
                    "district": "Bairro",
                    "city": "São Paulo",
                    "state": "sp",
                    "country": "BRA",
                    "zipcode": "00000000"
                },
                "billing_info": {
                    "credit_card": {
                        "holder_name": "Nome Completo",
                        "number": "4073020000000002",
                        "expiration_month": "04",
                        "expiration_year": "15"
                    }
                }
            }
        }

        vm.newClient = function() {
            moipService.createClient(vm.cliente).then(function (response){
                vm.moip_resp = response.data;
            });
        }

        moipService.listPlans().then(function (response){
            vm.plans = response.data;
        });

        vm.createSubscription = function (){
            moipService.createSubscription(vm.assinatura).then(function (response){
                vm.moip_resp = response.data;
            });
        }

    });
})();