(function() {
    'use strict';

    angular.module('donate')
        .config(['$locationProvider', '$stateProvider',
        function ($locationProvider, $stateProvider) {
            $stateProvider
                .state('donate', {
                    url: '/donate',
                    templateUrl: '/donate.view.html',
                    controller: 'DonateCtrl as vm',
                    ncyBreadcrumb: {
                        label: 'Donate'
                    }
                })

        }]);
}());