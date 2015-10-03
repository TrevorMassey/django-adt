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
            'common', 'News',
            function(common, News) {

                var vm = this;
                vm.detail = News.data;
                vm.title = 'test';

            }]);
}());
