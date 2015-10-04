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
                    resolve: {
                            goals: function (Goals) {
                                return Goals.initialize();
                            },
                            costs: function (Costs) {
                                return Costs.initialize();
                            },
                            donations: function (Donations) {
                                return Donations.initialize();
                            }
                        },
                    ncyBreadcrumb: {
                        label: 'Donations'
                    }
                })

        }]);
}());