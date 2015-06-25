(function() {
    'use strict';

    angular.module('donate')
        .factory('Donation', ['DS',  function(DS) {
            return DS.defineResource({
                name: 'donation',
                endpoint: 'donation-amounts'
            });
        }])

}());
