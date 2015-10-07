(function() {
    'use strict';

    angular.module('core')
        .factory('Feed', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('feed');

                var service = {
                    data: [],
                    list: list,
                    fetching: false,

                    model: Model

                };

                return service;
                /////////////////////

                function list($page) {
                    return getList($page);
                }

                function getList($page) {
                    $page = ($page == 'undefined') ? 1 : $page;
                    return Model.findAll({'page': $page})
                        .then(function(data) {
                            service.fetching = false;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }

            }]);
}());