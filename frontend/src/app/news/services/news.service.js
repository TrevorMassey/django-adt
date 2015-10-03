(function() {
    'use strict';

    angular.module('news')
        .factory('News', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('news');

                var service = {
                    list: [],
                    data: [],
                    initialize: initialize,
                    detail: detail

                };

                return service;
                /////////////////////

                function initialize() {
                    return getList();
                }

                function detail($param) {
                    return getDetail($param);
                }

                function getList() {
                    return Model.findAll()
                        .then(function(data) {
                            service.list = data;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for' + Model.name, error);
                        });
                }

                function getDetail($param) {
                    return Model.find($param)
                        .then(function(data) {
                            service.data = data;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for' + Model.name, error);
                        });
                }
            }]);
}());