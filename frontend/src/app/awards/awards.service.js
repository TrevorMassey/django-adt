(function() {
    'use strict';

    angular.module('awards')
        .factory('Award', ['DS', function(DS) {
            return DS.defineResource({
                name: 'awards'
            });
        }]);
}());