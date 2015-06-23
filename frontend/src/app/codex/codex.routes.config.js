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
                        resolve: {
                            codex: function (Codex) {
                                return Codex.initialize();
                            }
                        },
                        ncyBreadcrumb: {
                            label: 'Codex'
                        }
                    });

            }]).run(['Menus',
            function(Menus) {

                Menus.addMenuItem('topbar', {
                    title: 'Codex',
                    state: 'codex',
                    type: 'dropdown',
                    isPublic: true,
                    position: 30
                });

                Menus.addSubMenuItem('topbar', 'codex', {
                    title: 'Create Codex',
                    state: 'codex.create',
                    isPublic: true,
                    roles: ['publicatsdfions.sddddd']
                });
            }
        ]);
}());