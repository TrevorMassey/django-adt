(function() {
    'use strict';

    angular.module('news')
        .factory('News', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource('news');

                var Comment = DS.defineResource({
                    name: 'comments',
                    relations: {
                        belongsTo: {
                            news: {
                                parent: true,
                                localKey: 'slug',
                                localField: 'news'
                            }
                        }
                    }
                });

                var service = {
                    list: [],
                    data: [],
                    initialize: initialize,
                    detail: detail,
                    moar: moar,

                    model: Model,
                    comments: Comment,

                };

                return service;
                /////////////////////

                function initialize() {
                    return getList();
                }

                function detail($param) {
                    return getDetail($param);
                }

                function moar($page) {
                    return getMoar($page);
                }

                function getList() {
                    return Model.findAll()
                        .then(function(data) {
                            service.list = data;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }

                function getMoar($page) {
                    return Model.findAll({'page': $page})
                        .then(function(data) {
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }

                function getDetail($param) {
                    return Model.find($param)
                        .then(function(data) {
                            data.comments = Comment.findAll({'slug': $param});
                            return data;
                        })
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