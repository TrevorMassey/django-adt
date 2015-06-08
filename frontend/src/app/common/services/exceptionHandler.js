(function() {
    'use strict';

    /***
     ** Catch generic Angular exceptions
     ***********************************/

    angular.module('common')
        .provider('exceptionHandler', function() {
            this.config = {
                appErrorPrefix: undefined
            };

            this.configure = function (appErrorPrefix) {
                this.config.appErrorPrefix = appErrorPrefix;
            };

            this.$get = function() {
                return {
                    config: this.config
                };
            };
        });

    angular.module('common')
        .config(function($provide) {
            $provide.decorator('$exceptionHandler', [
                '$delegate', 'exceptionHandler', '$injector',
                function($delegate, exceptionHandler, $injector) {
                    return function(exception, cause) {

                        /**
                         * Get logger service inside because of circular dependency error with $exceptionHandler **/
                        var logger = $injector.get('logger');

                        var appErrorPrefix = exceptionHandler.config.appErrorPrefix || '';
                        var errorData = {exception: exception, cause: cause};
                        exception.message = appErrorPrefix + exception.message;
                        $delegate(exception, cause);
                        /**
                         * Could add the error to a service's collection,
                         * add errors to $rootScope, log errors to remote web server,
                         * or log locally. Or throw hard. It is entirely up to you.
                         * throw exception;
                         *
                         * @example
                         *     throw { message: 'error message we added' };
                         */
                        logger.error(exception.message, errorData);
                    };
                }]);
        });

}());