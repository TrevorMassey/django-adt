(function() {
    'use strict';

    angular.module('donate')
        .filter('reverse', function() {
            return function(items) {
                return items.slice().reverse();
            };
        });

}());
