(function() {
    'use strict';

    angular.module('applications')
        .factory('Application', ['DS', function(DS) {
            return DS.defineResource({
                name: 'applications'
                //endpoint: ''
            });
        }])

}());
