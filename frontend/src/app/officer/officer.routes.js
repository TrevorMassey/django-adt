(function() {
    'use strict';

    angular.module('officer')
        .config(function($breadcrumbProvider) {
            $breadcrumbProvider.setOptions({
                includeAbstract: true
            });
        })
        .config(['$locationProvider', '$stateProvider',
        function ($locationProvider, $stateProvider) {
            $stateProvider
                .state('officer', {
                    url: '/officer',
                    templateUrl: '/officer.view.html',
                    abstract: true
                })
                .state('officer.dashboard', {
                    url: '',
                    templateUrl: '/officer.dashboard.view.html',
                    controller: 'OfficerCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'Dashboard',
                        parent: 'officer'
                    }
                })
                .state('officer.news', {
                    url: '/news',
                    templateUrl: '/officer.news.view.html',
                    abstract: true,
                    ncyBreadcrumb: {
                        label: 'News',
                        parent: 'officer'
                    }
                })
                .state('officer.news.list', {
                    url: '',
                    templateUrl: '/officer.news.list.view.html',
                    ncyBreadcrumb: {
                        label: 'List',
                        parent: 'officer.news'
                    }
                })
                .state('officer.news.create', {
                    url: '/create',
                    templateUrl: '/officer.news.create.view.html',
                    controller: 'NewsCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'Create',
                        parent: 'officer.news'
                    }
                })

        }]);
}());