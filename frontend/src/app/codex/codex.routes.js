(function() {
    'use strict';

    angular.module('codex')
        .config(['$locationProvider', '$stateProvider', '$urlRouterProvider', '$authProvider',
        function ($locationProvider, $stateProvider, $urlRouterProvider, $authProvider) {
            $stateProvider
                .state('codex', {
                    url: '/codex',
                    templateUrl: '/codex.view.html',
                    controller: 'CodexCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'Codex'
                    }
                })

        }]);
}());