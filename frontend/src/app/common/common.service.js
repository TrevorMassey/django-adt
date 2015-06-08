(function() {
    'use strict';

    angular.module('common').factory('common', [
        'exception', 'logger',
        function(exception, logger) {

            var service = {
                logger: logger,
                exception: exception,
                extractError: extractError
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

        }]);
}());