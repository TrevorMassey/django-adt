(function() {
    'use strict';

    angular.module('common').directive('avatar', [
        'config',
        function(config) {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    image: '@',
                    color: '@',
                    width: '@',
                    height:'@',
                },
                templateUrl: '/avatar.view.html',
                link: function postLink(scope, element, attrs) {

                }
            };
        }
    ]);
}());