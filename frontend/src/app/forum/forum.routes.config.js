(function() {
    'use strict';

    angular.module('forum')
        .config(['$locationProvider', '$stateProvider',
            function ($locationProvider, $stateProvider) {
                $stateProvider
                    .state('forum', {
                        url: '/forum',
                        templateUrl: '/forum.view.html'
                    });

            }]);

    angular.module('forum')
        .run(['Menus',
            function(Menus) {

                Menus.addMenuItem('topbar', {
                    title: 'Forum',
                    state: 'forum',
                    //type: 'dropdown',
                    isPublic: true,
                    position: 20
                });


            }
        ]);
}());