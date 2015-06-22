(function() {
    'use strict';

    angular.module('auth')
        .controller('SignupCtrl', [
            'common', 'auth',
            function(common, auth) {
                if (auth.isAuthenticated()) common.redirectTo('/');

                var vm = this;

                vm.credentials = {};

                vm.signup = function () {
                    auth.signup(vm.credentials)
                        .then(function(response) {
                            vm.credentials = {};
                        })
                        .then(auth.storeSession)
                        .catch(common.errorHandler);
                };

            }]);

}());