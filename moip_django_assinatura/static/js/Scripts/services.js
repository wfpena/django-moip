(function() {
    'use strict';
    angular.module('app').factory('moipService', function($http) {
        return {
            createClient: function(params) {
                 return $http.post('/api/subscription/create_client/', params);
            },
            createSubscription: function(params, register) {
                 return $http.post('/api/subscription/create_subscription/?register=' + register, params);
            },
            listPlans: function() {
                return $http.get('/api/subscription/get_plans/');
            },
            listClients: function() {
                return $http.get('/api/subscription/get_clients/');
            }
        }
    });

})();