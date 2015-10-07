(function() {
    'use strict';

    angular.module('core')
        .controller('FeedCtrl', [
            'common', 'Feed', 'Message', '$scope',
            function(common, Feed, Message, $scope) {

                var vm = this;
                vm.page = 1;


                Feed.model.bindAll({}, $scope, 'vm.feed');

                vm.loadMoar = function() {
                    Feed.fetching = true;
                    Feed.list(vm.page);
                    vm.page++;
                };

                vm.loadMoar();

                vm.post = function(data) {
                    Message.save(data);
                };


            }])
}());
