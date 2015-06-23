(function() {
    'use strict';

    angular.module('core')
        .directive('profileDropdown', [ function() {
            return {
                restrict: 'EA',
                replace: true,
                templateUrl: '/profile.dropdown.view.html'
            };
        }]);

}());