(function() {
    'use strict';

    angular.module('donate')
        .factory('Goals', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('donation-goals');

                var service = {
                    data: [],
                    initialize: initialize

                };

                return service;
                /////////////////////

                function initialize() {
                    return getList();
                }

                function getList() {
                    return Model.findAll()
                        .then(function(data) {
                            service.data = data;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }
            }]);
}());
