(function() {
    'use strict';

    angular.module('codex')
        .controller('CodexCtrl', [
            'common', 'Codex',
            function(common, Codex) {

                var vm = this;
                vm.codex = Codex.data;

            }]);
}());
