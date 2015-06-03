(function() {
    'use strict';

    angular.module('core').controller('AppCtrl', [
        '$scope', '$location', 'auth',
        function($scope, $location, auth) {

        $scope.session = { currentUser: {} };
        $scope.site = { title: "Addiction "};
        $scope.isAuthenticated = isAuthenticated;
        $scope.toggleLeftPanel = toggleLeftPanel;
        $scope.toggleRightPanel = toggleRightPanel;
        $scope.leftVisible = true;
        $scope.rightVisible = true;
        $scope.navLocation = '/' + $location.url().split('/')[1];

        ////$scope.isCollapsed = true;
        //
        //$scope.session.currentUser = auth.currentUser;

        $scope.toggleCollapsibleMenu = function() {
            $scope.isCollapsed = !$scope.isCollapsed;
        };
        function isAuthenticated() {
            return auth.isAuthenticated();
        }

        function toggleLeftPanel(e) {
            $scope.leftVisible = !$scope.leftVisible;
            e.stopPropagation();
        }

        function toggleRightPanel(e) {
            $scope.rightVisible = !$scope.rightVisible;
            e.stopPropagation();
        }

        $scope.setLocation = function (viewLocation) {
            console.log(viewLocation);
            $scope.navLocation = viewLocation;
        };

        $scope.isActive = function (viewLocation) {
            return $scope.navLocation === viewLocation;
        }

    }]);

}());
