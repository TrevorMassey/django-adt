(function() {
    'use strict';

    angular.module('core')
        .directive('notificationDropdown', [ function() {
            return {
                restrict: 'EA',
                replace: true,
                templateUrl: '/notification.dropdown.view.html'
            };
        }]);

}());