(function() {
    'use strict';

    angular.module('common').directive('username', [
        function() {
            return {
                restrict: 'E',
                templateUrl: '/username.view.html',
                transclude: true
            };
        }
    ]);
}());