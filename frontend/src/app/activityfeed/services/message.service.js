(function() {
    'use strict';

    angular.module('core')
        .factory('Message', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('feed-posts');

                var service = {
                    save: save,
                    model: Model
                };

                return service;
                /////////////////////

                function save(data) {
                    return newPost(data);
                }

                function newPost(data) {
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