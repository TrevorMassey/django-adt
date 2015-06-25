(function() {
    'use strict';

    angular.module('awards')
        .controller('AwardsCtrl', [
            'common', 'Award',
            function(common, Award) {
                var vm = this;
                vm.awards = [];

                Award.findAll()
                    .then(function(awards) {
                        vm.awards = awards;
                    });
            }]);
}());
