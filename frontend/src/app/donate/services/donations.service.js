(function() {
    'use strict';

    angular.module('donate')
        .factory('Donations', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('donations');

                var service = {
                    model: Model,
                    data: [],
                    initialize: initialize,
                    save: save

                };

                return service;
                /////////////////////

                function initialize() {
                    return getList();
                }

                function save(data) {
                    return newDonation(data);
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

                function newDonation(data) {
                    return Model.create(data)
                        .then(function(res) {
                            return res;
                        })
                        .catch(function(error) {
                            common.logger.error('Error creating record for ' + Model.name, error);
                        });
                }
            }]);
}());
