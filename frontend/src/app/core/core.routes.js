(function() {
    'use strict';


    angular.module('core').config(['$stateProvider', '$urlRouterProvider',
        function ($stateProvider, $urlRouterProvider) {
            $stateProvider
                .state('home', {
                    url: '/',
                    templateUrl: '/home.view.html',
                    ncyBreadcrumb: {
                        label: 'Addiction'
                    }
                });


        }]).run([
        '$rootScope',
        '$state',
        '$stateParams',
        'Menus',
        function ($rootScope, $state, $stateParams, Menus) {

            Menus.addMenuItem('topbar', {
                title: 'Addiction',
                state: 'home',
                type: 'dropdown',
                isPublic: true,
                position: 0
            });

            // Add the dropdown list item
            Menus.addSubMenuItem('topbar', 'home', {
                title: 'Dashboard',
                state: 'home'
                //isPublic: false
            });

            Menus.addSubMenuItem('topbar', 'home', {
                title: 'News',
                state: 'news'
                //isPublic: false
            });

            Menus.addSubMenuItem('topbar', 'home', {
                title: 'DKP',
                state: 'home'
                //isPublic: false
            });

            Menus.addSubMenuItem('topbar', 'home', {
                title: 'Awards',
                state: 'awards'
                //isPublic: false
            });


            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;

        }]);

}());