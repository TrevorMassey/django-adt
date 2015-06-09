(function() {
    'use strict';

    angular.module('core')
        .controller('AppCtrl', [
            '$scope', 'common', 'auth', 'Session',
            function($scope, common, auth, Session) {

                $scope.session = { currentUser: {} };
                $scope.site = { title: "Addiction "};
                $scope.isAuthenticated = isAuthenticated;
                $scope.toggleLeftPanel = toggleLeftPanel;
                $scope.toggleRightPanel = toggleRightPanel;
                $scope.leftVisible = true;
                $scope.rightVisible = true;

                $scope.isCollapsed = false;

                //console.log(auth.isAuthenticated());
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

            }]);

}());
