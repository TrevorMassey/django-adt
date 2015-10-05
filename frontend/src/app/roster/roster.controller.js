(function() {
    'use strict';

    angular.module('roster')
        .controller('RosterCtrl', [
            'common', 'Roster',
            function(common, Roster) {

                var vm = this;
                vm.roster = Roster.list;


            }])
}());
