(function() {
    'use strict';

    angular.module('core')
        .controller('HeaderCtrl', [
            '$scope', 'common', 'auth', 'Session', 'Menus',
            function($scope, common, auth, Session, Menus) {

                $scope.menu = Menus.getMenu('topbar');
                $scope.isCollapsed = false;
                $scope.toggledState = false;

                $scope.toggleCollapsibleMenu = function() {
                    $scope.isCollapsed = !$scope.isCollapsed;
                };

            }]);

}());