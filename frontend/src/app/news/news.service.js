(function() {
    'use strict';

    angular.module('news')
        .factory('News', ['DS', function(DS) {
            return DS.defineResource({
                name: 'news'
            });
        }]);
}());