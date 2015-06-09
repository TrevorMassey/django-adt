(function() {
    'use strict';

    angular.module('codex')
        .factory('Codex', ['common', 'DS',
            function(common, DS) {

                var Codex = DS.defineResource('codex');

                var service = {
                    data: [],
                    getList: getList
                };

                return service;
                /////////////////////

                function getList() {
                    return Codex.findAll()
                        .then(function(data) {
                            service.data = data;
                            return data;
                        })
                        .catch(function(event) {
                            common.logger.error('error', event, 'Error');
                        });
                }
            }]);

}());