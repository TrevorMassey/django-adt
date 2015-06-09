(function() {
    'use strict';

    angular.module('auth')
        .controller('SignupCtrl', [
            'common', '$location', 'auth',
            function(common, $location, auth) {
                if (auth.isAuthenticated()) $location.path('/');

                var exception = common.exception;
                var vm = this;

                vm.credentials = {};

                vm.signup = function () {
                    auth.signup(vm.credentials)
                        .then(function(response) {
                            vm.credentials = {};
                        })
                        .catch(function(error) {
                            var message = common.extractError(error.data);
                            exception.catcher(message)(error)
                        });
                };

            }]);

}());