(function() {
    'use strict';

    angular.module('media')
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('media', {
                        url: '/media',
                        templateUrl: '/media.view.html'
                    });

            }]);

    angular.module('media')
        .run(['Menus',
            function(Menus) {

                Menus.addMenuItem('topbar', {
                    title: 'Media',
                    state: 'media',
                    //type: 'dropdown',
                    isPublic: true,
                    position: 20
                });


            }
        ]);
}());