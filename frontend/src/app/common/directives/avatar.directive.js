(function() {
    'use strict';

    angular.module('common').directive('avatar', [
        'config',
        function(config) {
            return {
                restrict: 'E',
                replace: true,
                template: '<img ng-src="https://placeimg.com/50/50/people" />',
                link: function postLink(scope, element, attrs) {

                }
            };
        }
    ]);
}());