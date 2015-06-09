(function() {
    'use strict';

    angular.module('codex')
        .config(['$locationProvider', '$stateProvider',
        function ($locationProvider, $stateProvider) {
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