(function() {
    'use strict';

    angular.module('common')
        .factory('common', [
            '$location', 'exception', 'logger', 'localStorageService',
            function($location, exception, logger, localStorageService) {

                var service = {
                    logger: logger,
                    exception: exception,
                    localStorage: localStorageService,
                    extractError: extractError,
                    redirectTo: redirectTo
                };

                return service;
                /////////////////////

                function extractError(errors) {
                    var errorMsgs = [];
                    angular.forEach(errors, function(value, key) {
                        errorMsgs.push(errors[key]);
                    });
                    return errorMsgs.toString();
                }

                function redirectTo(path) {
                    return $location.path(path);
                }

            }]);

    angular.module('common')
        .config(function(localStorageServiceProvider) {
            localStorageServiceProvider.setPrefix('adt');
        });
}());