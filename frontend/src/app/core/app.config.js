(function() {
    'use strict';

    var app = angular.module('core');

    var appName = 'ADT';
    var config = {
        appErrorPrefix: appName + ' Error: ',
        appTitle: appName,
        API_URL: 'http://localhost:8000'
    };

    app.value('config', config);

    app.config(function(toastrConfig) {
        angular.extend(toastrConfig, {
            timeOut: 3000
        });
    });

    app.config(configure);

    function configure($logProvider, exceptionHandlerProvider, DSProvider) {
        if ($logProvider.debugEnabled) {
            $logProvider.debugEnabled(true);
        }

        exceptionHandlerProvider.configure(config.appErrorPrefix);

        DSProvider.defaults.basePath = '/api/';
        DSProvider.defaults.suffix = '/';

        DSProvider.defaults.deserialize = function (resource, data) {
            return data ? ('data' in data ? ('results' in data.data ? data.data.results : data.data) : data) : data;
        }
    }

}());