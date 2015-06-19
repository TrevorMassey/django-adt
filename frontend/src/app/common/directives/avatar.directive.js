(function() {
    'use strict';

    angular.module('common').directive('avatar', [
        'config',
        function(config) {
            return {
                restrict: 'E',
                replace: true,
                template: '<img ng-src="" />',
                link: function postLink(scope, element, attrs) {

                }
            };
        }
    ]);
}());