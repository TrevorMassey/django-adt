(function() {
    'use strict';

    angular.module('core').controller('AppCtrl', [
        '$scope', '$location', 'auth', 'toastr', '$dragon',
        function($scope, $location, auth, toastr, $dragon) {

            $scope.session = { currentUser: {} };
            $scope.site = { title: "Addiction "};
            $scope.isAuthenticated = isAuthenticated;
            $scope.toggleLeftPanel = toggleLeftPanel;
            $scope.toggleRightPanel = toggleRightPanel;
            $scope.leftVisible = true;
            $scope.rightVisible = true;
            $scope.navLocation = '/' + $location.url().split('/')[1];
            toastr.success('Hello world!', 'Toastr fun!');
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

            $scope.isActive = function (viewLocation) {
                return $scope.navLocation === viewLocation;
            };


            $dragon.onReady(function() {
                $dragon.subscribe('sys', 'sysinfo', null).then(function(response) {
                    console.log(response.data + ' success');
                });
            });

            $dragon.onChannelMessage(function(channels, message) {
                //console.log(channels, message);
                console.log(message.data);
            });
        }]);

}());
