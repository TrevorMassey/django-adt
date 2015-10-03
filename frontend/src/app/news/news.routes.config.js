(function() {
    'use strict';

    angular.module('news')
        .config(function($breadcrumbProvider) {
            $breadcrumbProvider.setOptions({
                templateUrl: '/breadcrumb.view.html',
                prefixStateName: 'home'
            });
        })
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('news', {
                        url: '/news',
                        templateUrl: '/news.view.html',
                        controller: 'NewsCtrl as vm',
                        resolve: {
                            news: function (News) {
                                return News.initialize();
                            }
                        }
                    })
                    .state('news.item', {
                        url: '/:newsSlug',
                        views: {
                            "@" : {
                                templateUrl: '/news.item.view.html',
                                controller: 'NewsDetailCtrl as vm',
                            }
                        },
                        resolve: {
                            news: function (News, $stateParams) {
                                return News.detail($stateParams.newsSlug);
                            }
                        },
                        ncyBreadcrumb: {
                            label: '{{vm.detail.title}}'
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