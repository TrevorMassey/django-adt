(function() {
    'use strict';

    angular.module('applications')
        .config(['$locationProvider', '$stateProvider', '$urlRouterProvider', '$authProvider',
        function ($locationProvider, $stateProvider, $urlRouterProvider, $authProvider) {
            $stateProvider
                .state('applications', {
                    url: '/applications',
                    templateUrl: '/applications.view.html',
                    controller: 'ApplicationsCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'Applications'
                    }
                })

        }]);
}());