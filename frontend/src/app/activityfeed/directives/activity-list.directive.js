(function() {
    'use strict';

    angular.module('core')
        .directive('activityList', [ function() {
            return {
                restrict: 'EA',
                templateUrl: '/right-panel.view.html',
                controller: 'FeedCtrl as vm'
            };
        }]);
}());
