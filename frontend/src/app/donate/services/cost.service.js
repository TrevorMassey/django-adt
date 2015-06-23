(function() {
    'use strict';

    angular.module('donate')
        .factory('Cost', ['DS', function(DS) {
            return DS.defineResource({
                name: 'cost',
                endpoint: 'donation-costs'
            });
        }])

}());
