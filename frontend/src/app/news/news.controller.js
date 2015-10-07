(function() {
    'use strict';

    angular.module('news')
        .controller('NewsCtrl', [
            'common', 'News', '$scope',
            function(common, News, $scope) {

                var vm = this;
                vm.page = 2;

                News.model.bindAll({}, $scope, 'vm.news');

                vm.loadMoar = function() {
                    // TODO: disable during fetch, and at end of list
                    News.fetching = true;
                    News.list(vm.page);
                    vm.page++;
                };

            }])
        .controller('NewsDetailCtrl', [
            '$scope', 'common', 'News',
            function($scope, common, News) {

                var vm = this;
                vm.detail = News.data;

                News.comments.bindAll({}, $scope, 'vm.detail.comments')

            }]);
}());
