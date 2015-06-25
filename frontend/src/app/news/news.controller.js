(function() {
    'use strict';

    angular.module('news')
        .controller('NewsCtrl', ['News', function(News) {
            var vm = this;
            vm.news = [];

            News.findAll()
                .then(function(data) {
                    vm.news = data;
                });

        }]);

}());
