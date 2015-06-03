(function() {
    'use strict';

    angular.module('core').controller('MessageCtrl', ['$scope', 'auth', 'activities',
        function($scope, auth, activities) {

            $scope.message = {};


            $scope.createMessage = function() {
                alert('Need to implement method');
            };


        }]);

}());
