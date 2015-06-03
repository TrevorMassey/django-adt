(function() {
    'use strict';

    var API_URL = 'http://localhost:1337';

    var config = {
        API_URL: API_URL
    };

    angular.module('core').value('config', config);

    //angular.module('core').config(function(RestangularProvider) {
    //    RestangularProvider.setBaseUrl('/api/');
    //})

}());
