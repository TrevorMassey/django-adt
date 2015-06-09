(function() {
    'use strict';

    angular.module('auth')
        .controller('SigninCtrl',[
            'common', 'auth',
            function(common, auth) {
                if (auth.isAuthenticated()) common.redirectTo('/');

                var exception = common.exception;
                var logger = common.logger;
                var vm = this;

                vm.login = function () {
                    var credentials = {
                        email: vm.credentials.email,
                        password: vm.credentials.password
                    };

                    auth.login(credentials)
                        .then(function(response) {
                            vm.credentials = {};
                            logger.success('Signed in!', response);
                        })
                        .then(function() {
                            auth.getCurrentUser();
                        })
                        .catch(function(error) {
                            var message = common.extractError(error.data);
                            exception.catcher(message)(error);
                        });
                };

            }]);

}());