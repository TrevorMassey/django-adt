(function() {
    'use strict';

    angular.module('auth')
        .controller('SignupCtrl',['$location', 'auth', function($location, auth) {

            if (auth.isAuthenticated()) $location.path('/');
            var vm = this;
            vm.credentials = {};

            vm.signup = function () {
                auth.signup(vm.credentials)
                    .then(function(response) {
                        vm.credentials = {};
                    })
                    .catch(function(error) {
                        console.log(error);
                    });
            };

        }]);

}());