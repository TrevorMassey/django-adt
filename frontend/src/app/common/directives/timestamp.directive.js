(function() {
    'use strict';

    angular.module('common').directive('timestamp', ['$filter',
        function() {
            return {
                restrict: 'E',
                templateUrl: '/timestamp.view.html',
                scope: {
                    stamp: '=time'
                },
                controller: function($scope, $filter) {
                    var fullStamp = $filter('amDateFormat')($scope.stamp,'dddd, MMMM Do YYYY, h:mm a');
                    $scope.tooltip = {
                        "title": fullStamp
                    };

                }
            };
        }
    ]);
}());