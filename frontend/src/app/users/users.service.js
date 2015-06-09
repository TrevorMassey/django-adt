(function() {
    'use strict';

    angular.module('users')
        .factory('User', ['common', 'DS',
            function(common, DS) {

                var User = DS.defineResource({
                    name: 'user',
                    endpoint: 'users'
                });


                return User;
                /////////////////////


            }]);

}());