(function() {
    'use strict';

    angular.module('roster')
        .config(function($breadcrumbProvider) {
            $breadcrumbProvider.setOptions({
                templateUrl: '/breadcrumb.view.html',
                prefixStateName: 'home'
            });
        })
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('roster', {
                        url: '/roster',
                        templateUrl: '/roster.view.html',
                        controller: 'RosterCtrl as vm',
                        resolve: {
                            roster: function (Roster) {
                                return Roster.initialize();
                            }
                        }
                    })

            }])
}());