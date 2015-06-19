(function() {
    'use strict';

    angular.module('core')
        .directive('adtHeader', [ function() {
            return {
                restrict: 'EA',
                replace: true,
                templateUrl: '/header.view.html',
                controller: 'HeaderCtrl'
            };
        }]);

    angular.module('core')
        .directive('navBar', [ function() {
            return {
                restrict: 'EA',
                //replace: true,
                templateUrl: '/navbar.view.html'
            };
        }]);


    angular.module('core')
        .directive('mainMenu', [ function() {
            return {
                restrict: 'EA',
                replace: true,
                transclude: true,
                templateUrl: '/main-menu.view.html'
            };
        }]);

}());