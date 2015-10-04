(function() {
    'use strict';

    angular.module('awards')
        .controller('AwardsCtrl', [
            'common', 'Awards',
            function(common, Awards) {

                var vm = this;
                vm.awards = Awards.data;

            }]);
}());
