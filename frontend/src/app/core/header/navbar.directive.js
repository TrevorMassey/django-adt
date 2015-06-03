(function() {
    'use strict';

    angular.module('core')
        .directive('navBar', [ function() {
            return {
                restrict: 'EA',
                templateUrl: '/navbar.view.html'
            };
        }]);
}());