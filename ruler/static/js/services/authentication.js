'use strict';

angular.module('myangular')
  .factory('AuthenticationService', [
    'Base64', '$http', '$cookieStore', '$rootScope', '$timeout',
    function(Base64, $http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.login = function(username, password, callback) {
            $timeout(function() {
                var response = {
                    success: username === 'test' && password === 'test'
                };
                if(!response.success) {
                    response.message = 'Username or password is incorrect';
                }
                callback(response);
            }, 1000);
        };
    }
  ]); // end factory
