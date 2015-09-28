(function() {
    'use strict';

    angular.module('core')
        .controller('AppCtrl', [
            '$scope', 'common', 'auth', 'Session', '$dragon',
            function($scope, common, auth, Session, $dragon) {

                $scope.currentUser = Session.currentUser;
                $scope.site = { title: "Addiction "};
                $scope.isAuthenticated = isAuthenticated;
                $scope.toggleLeftPanel = toggleLeftPanel;
                $scope.toggleRightPanel = toggleRightPanel;
                $scope.leftVisible = true;
                $scope.rightVisible = true;


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
