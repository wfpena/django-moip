(function() {
 'use strict';
 angular.module('app',[
	'ngCookies',
	'ui.router'
 ], function($interpolateProvider){
	// Contorna problema de interpolação da renderização de template do django
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
 })
 .run( function run($http, $cookies ){
	// Evita problemas relacionados ao CSRF
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
 });

 angular.module('app').config(['$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider', function($httpProvider, $locationProvider, $stateProvider, $urlRouterProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

     $urlRouterProvider.otherwise("/");
     $stateProvider.state('cliente', {
        url:'/cliente',
        templateUrl: '/static/views/cliente.html'
      })
      .state('assinatura', {
        url:'/assinatura',
        //controller: 'UserCtrl as vm',
        templateUrl: '/static/views/assinatura.html'
      });

 }])
})();