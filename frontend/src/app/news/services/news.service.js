(function() {
    'use strict';

    angular.module('news')
        .factory('News', ['common', 'DS',
            function(common, DS) {

                var Model = DS.defineResource( 'news');

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
                    data: [],
                    list: list,
                    detail: detail,

                    fetching: false,

                    model: Model,
                    comments: Comment

                };

                return service;
                /////////////////////

                function list($page) {
                    return getList($page);
                }

                function detail($param) {
                    return getDetail($param);
                }

                function getList($page) {
                    $page = ($page == 'undefined') ? 1 : $page;
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
                            service.fetching = false;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }
            }]);
}());