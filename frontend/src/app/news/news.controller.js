(function() {
    'use strict';

    angular.module('news')
        .controller('NewsCtrl', [
            'common', 'News',
            function(common, News) {

                var vm = this;
                vm.news = News.list;


            }])
        .controller('NewsDetailCtrl', [
            '$scope', 'common', 'News',
            function($scope, common, News) {

                var vm = this;
                vm.detail = News.data;

                News.comments.bindAll({}, $scope, 'vm.detail.comments')

            }]);
}());
