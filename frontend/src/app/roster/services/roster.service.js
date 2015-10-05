(function() {
    'use strict';

    angular.module('roster')
        .factory('Roster', ['common', 'DS',
            function(common, DS) {

                var Chapters = DS.defineResource({
                    name: 'chapters',
                    relations: {
                        hasMany: {
                            divisions: {
                                localKeys: 'divisions',
                                foreignKey: 'chapter'
                            }
                        }
                    }
                });

                var Divisions = DS.defineResource({
                    name: 'divisions',
                    relations: {
                        belongsTo: {
                            chapters: {
                                parent: true,
                                localKey: 'id',
                                localField: 'chapter'
                            }
                        }
                    }
                });

                var service = {
                    data: [],
                    chapters: [],
                    divisions: [],
                    initialize: initialize

                };

                return service;
                /////////////////////

                function initialize() {
                    getChapters();
                    //getDivisions();

                }

                function getChapters() {
                    return Chapters.findAll()
                        .then(function(data) {
                            service.chapters = data;
                            return data;
                        })
                        .catch(function(error) {
                            common.logger.error('Error retrieving data for ' + Model.name, error);
                        });
                }
                //function getChapters() {
                //    return Chapters.findAll()
                //        .then(function(data) {
                //            service.chapters = data;
                //            return data;
                //        })
                //        .catch(function(error) {
                //            common.logger.error('Error retrieving data for ' + Model.name, error);
                //        });
                //}
            }]);
}());