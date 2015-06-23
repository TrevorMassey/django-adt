(function() {
    'use strict';

    angular.module('auth')
        .controller('LogoutCtrl',[
            'common', 'auth', 'Session',
            function(common, auth, Session) {

                    auth.logout()
                        .then(function() {
                            Session.destroy();
                            common.redirectTo('/');
                        })
                        .then(function() {
                            common.logger.info('Signed out!');
                        });

            }]);

}());