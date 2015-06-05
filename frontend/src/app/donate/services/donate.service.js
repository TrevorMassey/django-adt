(function() {
    'use strict';

    angular.module('donate')
        .factory('Donations', ['$resource',  function($resource) {
            return $resource('http://localhost:1337/donation', {});
        }])
        .factory('Costs', ['$resource', function($resource) {
            return $resource('http://localhost:1337/cost', {});

        }])
        .filter('reverse', function() {
            return function(items) {
                return items.slice().reverse();
            };
        });
}());
