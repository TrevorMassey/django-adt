(function() {
    'use strict';

    angular.module('codex').controller('CodexCtrl', [
        '$scope', 'Restangular',
        function($scope, Restangular) {
            var vm = this;
            vm.codex = {};
            Restangular.all('codex').getList().then(function(codex) {
                vm.codex = codex;
            });
        }]);
}());
