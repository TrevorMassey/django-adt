(function() {
    'use strict';

    angular.module('core')
        .directive('onlineUserList', [
            '$document', '$timeout', 'auth', 'rx',
            function($document, $timeout, auth, rx) {
                return {
                    restrict: 'EA',
                    templateUrl: '/online-users-list.view.html',
                    controller: function($scope) {
                        var vm = this;
                        vm.users = { data: [] };
                        var count = 0;

                        var fakeData = [
                            {"_id":"545ab71635fe5a08006d5814","username":"Gromph","email":"wrath625@gmail.com"},
                            {"_id":"54bda4c8b489a1e61072e67b","username":"Dashra","email":"caeadorn@yahoo.com"},
                            {"_id":"54814ee674b2689c93dd0b540","username":"Liminsathil","email":"lim@example.com"},
                            {"_id":"54751aa5ec6c5539da5c2354","username":"Akrylis","email":"unkleara@gmail.com"},
                            {"_id":"546aaa41d2abfe9aab10eb0c","username":"Shadow","email":"shadow@example.com"},
                            {"_id":"545ab585aea9100800421908","username":"Unkle","email":"unkleara@gmail.com"}
                        ];

                        angular.copy(fakeData, vm.users.data);

                        // Rx subscribe to mousemove events as 2.5s interval
                        // Check to see if current user is logged in to mark them online

                        // TODO: add unsubsribe when user is online and subscribe when is active again
                        var mousemove = rx.Observable.fromEvent($document, 'mousemove');


                        var mousemoveSubscription = mousemove.throttle(2500)
                            .filter(function(event) {
                                //if (auth.isAuthenticated() && (event.clientY >= 100))

                                //console.log('client: ' + event.clientY);
                                //console.log('page: ' + event.pageY);
                                //console.log('offset: ' + event.offsetY);
                                    return event;
                            });
                            //.throttle(500).forEach(function () {
                              //  setUserOnline();
                            //});

                        var REFRESH_ONLINE_STATUS_INTERVAL = 250;
                        var onlineUsersSubscription = rx.Observable.interval(1000)
                            .safeApply($scope, function() {
                                angular.forEach(vm.users.data, function (user) {

                                    user.msUntilInactive -= REFRESH_ONLINE_STATUS_INTERVAL;
                                    //user.signedIn = user.msUntilInactive > 0;
                                    user.signedIn = true;
                                });
                            });

                            //add mousemove subscribe as well
                            mousemoveSubscription.subscribe();

                            onlineUsersSubscription.subscribe();


                            //mousemoveSubscription.dispose();
                            //onlineUsersSubscription.dispose();


                    },
                    controllerAs: 'vm',
                    bindToController: true
                };
            }])

}());
