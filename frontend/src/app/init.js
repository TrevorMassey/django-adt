(function() {
    'use strict';

//Start by defining the main module and adding the module dependencies
    angular.module(ApplicationConfiguration.applicationModuleName, ApplicationConfiguration.applicationModuleVendorDependencies);

// Setting HTML5 Location Mode
    angular.module(ApplicationConfiguration.applicationModuleName).config([
        '$locationProvider', '$urlRouterProvider',
        function($locationProvider, $urlRouterProvider) {

            $locationProvider.html5Mode(true).hashPrefix('!');

            // For any unmatched url, redirect to '/'
            $urlRouterProvider.otherwise('/');

        }
    ]);

//Then define the init function for starting up the application
    angular.element(document).ready(function() {
        //Fixing facebook bug with redirect
        if (window.location.hash === '#_=_') window.location.hash = '#!';

        //Then init the app
        angular.bootstrap(document, [ApplicationConfiguration.applicationModuleName]);
    });

}());