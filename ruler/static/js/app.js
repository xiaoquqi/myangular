// Declare app level module which depends on filters, and services
angular
  .module('myangular', [
    'ngResource',
    'ngRoute',
    'ui.bootstrap',
    'ui.date'
  ])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'})
      .when('/login', {
          templateUrl: 'views/login.html',
          controller: 'LoginController'
      })
      .otherwise({redirectTo: '/login'});
  }]);
