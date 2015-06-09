(function() {
    'use strict';

    angular.module('news')
        .config(['$locationProvider', '$stateProvider', '$urlRouterProvider', '$authProvider',
        function ($locationProvider, $stateProvider, $urlRouterProvider, $authProvider) {
            $stateProvider
                .state('news', {
                    url: '/news',
                    templateUrl: '/news.view.html',
                    abstract: true
                })
                .state('news.list', {
                    url: '',
                    templateUrl: '/news.list.view.html',
                    controller: 'NewsCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'List'
                    }
                })

        }]);
}());