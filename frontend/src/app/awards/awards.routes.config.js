(function() {
    'use strict';

    angular.module('awards')
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('awards', {
                        url: '/awards',
                        templateUrl: '/awards.view.html',
                        controller: 'AwardsCtrl as vm',
                        resolve: {
                            awards: function (Awards) {
                                return Awards.initialize();
                            }
                        },
                        ncyBreadcrumb: {
                            label: 'Awards'
                        }
                    })

            }]);
}());