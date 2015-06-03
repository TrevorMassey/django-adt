(function() {
    'use strict';

    angular.module('auth').factory('auth', [
        'config', '$auth', '$http', '$q',
        function(config, $auth, $http, $q) {
            var service = {
                currentUser: null
            };

            var payload = null;

            angular.extend(service, $auth);
            return service;
        }]);
}());