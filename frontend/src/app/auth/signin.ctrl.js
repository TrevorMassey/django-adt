(function() {
    'use strict';

    angular.module('auth')
        .controller('SigninCtrl',['$location', 'auth', function($location, auth) {

            if (auth.isAuthenticated()) $location.path('/');
            var vm = this;

            vm.login = function () {
                var credentials = {
                    email: vm.credentials.email,
                    password: vm.credentials.password
                };

                auth.login(credentials)
                    .then(function(response) {
                        vm.credentials = {};
                    })
                    .catch(function(error) {
                        console.log(error);
                    })
            };

        }]);

}());