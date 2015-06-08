(function() {
    'use strict';

    angular
        .module('common')
        .factory('exception', ['logger',
            function exception(logger) {
                var service = {
                    catcher: catcher
                };
                return service;

                function catcher(message) {
                    return function(reason) {
                        logger.error(message, reason);
                    };
                }
            }]);
})();