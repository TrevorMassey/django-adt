(function() {
    'use strict';

    angular.module('about')
        .config(function($breadcrumbProvider) {
            $breadcrumbProvider.setOptions({
                templateUrl: '/breadcrumb.view.html',
                prefixStateName: 'home'
            });
        })
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('about', {
                        url: '/about',
                        templateUrl: '/about.view.html',
                        ncyBreadcrumb: {
                            label: 'About'
                        }
                    })
                    .state('about.membership', {
                        url: '/membership',
                        views: {
                            "@" : {
                                templateUrl: '/about.membership.view.html'
                            }
                        },
                        ncyBreadcrumb: {
                            label: 'Membership'
                        }
                    });


            }]);

    angular.module('about')
        .run(['Menus',
            function(Menus) {

                // ADDICTION, FORUM, MEDIA, CODEX, /** ABOUT **/

                Menus.addMenuItem('topbar', {
                    title: 'About',
                    state: 'about',
                    //mainState: 'about',
                    type: 'dropdown',
                    isPublic: true,
                    position: 90
                });

                Menus.addSubMenuItem('topbar', 'about', {
                    title: 'Membership',
                    state: 'about.membership',
                    isPublic: true
                });

            }
        ]);
}());