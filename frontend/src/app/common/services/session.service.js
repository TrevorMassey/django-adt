(function() {
    'use strict';

    angular.module('common')
        .service('Session', ['localStorageService',
            function(localStorageService) {

                this.create =function (name, email, permissions) {
                    localStorageService
                        .set('session', this.currentUser = {
                            displayName: name,
                            email: email,
                            permissions: permissions
                        });
                };

                this.destroy = function () {
                    localStorageService
                        .remove('session', this.currentUser = {
                            displayName: null,
                            email: null,
                            permissions: null
                        });
                };
            }])

}());