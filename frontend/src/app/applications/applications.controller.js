(function() {
    'use strict';

    angular.module('applications').controller('ApplicationsCtrl', [
        '$scope', 'Restangular', '$q',
        function($scope, Restangular, $q) {
            var vm = this;
            vm.applications = {};
            var res = [];

            res.push(Restangular.all('/user/applications').getList());
            res.push(Restangular.all('/game').getList());

            $q.all(res).then(function(data) {
                vm.applications = data[0];
                _.map(vm.applications, function(application) {
                    _.map(data[1], function(game) {
                        if (application.chapter.game == game.id) {
                            application.chapter.game = game;
                        }
                    })
                });
            });
        }]);
}());
