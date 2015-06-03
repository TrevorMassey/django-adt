(function() {
    'use strict';

    angular.module('auth')
        .config(['$locationProvider', '$stateProvider', '$urlRouterProvider', '$authProvider',
            function ($locationProvider, $stateProvider, $urlRouterProvider, $authProvider) {
                $stateProvider
                    .state('signin', {
                        url: '/signin',
                        templateUrl :  '/signin.view.html',
                        controller: 'SigninCtrl as vm'
                    })
                    .state('signup', {
                        url: '/signup',
                        templateUrl: '/signup.view.html',
                        controller: 'SignupCtrl as vm'
                    })
                    .state('logout', {
                        url: '/logout',
                        template: null,
                        controller: 'LogoutCtrl'
                    });

                $authProvider.httpInterceptor = true;
                $authProvider.withCredentials = true;
                $authProvider.loginRedirect = '/';
                $authProvider.logoutRedirect = '/';
                $authProvider.signupRedirect = '/login';
                $authProvider.loginUrl = 'api-token-auth/';
                $authProvider.signupUrl = 'api-token-auth/';
                $authProvider.loginRoute = '/signin';
                $authProvider.signupRoute = '/signup';

            }]);
}());