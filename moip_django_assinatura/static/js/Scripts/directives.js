(function() {
    'use strict';
    angular.module('app').directive('clientInfo', function () {
      return {
        restrict: 'E',
        replace: true,
        scope: {
            client: '='
        },
        templateUrl: '/static/views/partials/clientInfo.html'
      }
    });

    angular.module('app').directive('creditCardInfo', function () {
      return {
        restrict: 'E',
        replace: true,
        scope: {
            card: '='
        },
        templateUrl: '/static/views/partials/creditCardInfo.html'
      }
    });

})();