(function() {
    'use strict';

    angular.module('common').directive('avatar', [
        'config',
        function(config) {
            return {
                restrict: 'E',
                template: '<img ng-src="https://placeimg.com/50/50/people" />',
                replace: true,
                link: function postLink(scope, element, attrs) {

                }
            };
        }
    ]);
}());