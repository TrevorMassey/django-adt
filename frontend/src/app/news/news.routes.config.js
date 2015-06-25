(function() {
    'use strict';

    angular.module('news')
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('news', {
                        url: '/news',
                        templateUrl: '/news.view.html'
                    })
                    .state('news.list', {
                        url: '',
                        templateUrl: '/news.list.view.html',
                        controller: 'NewsCtrl as vm',
                        ncyBreadcrumb: {
                            label: 'List'
                        }
                    })

            }]).run(['Menus',
            function(Menus)
            {

                //TODO: Currently added in core.routes but can also add here just remove it in core

                //Menus.addSubMenuItem('topbar', 'home', {
                //    title: 'News',
                //    state: 'news'
                //    //isPublic: false
                //});


            }
        ]);
}());