(function() {
    'use strict';

    angular.module('donate')
        .controller('DonateCtrl', [
            '$scope', 'common', 'Donations', 'Costs', 'Goals',
            function($scope, common, Donations, Costs, Goals) {
                var vm = this;
                vm.goals = Goals.data;
                vm.costs = Costs.data;
                vm.donations =  Donations.data;
                Donations.model.bindAll({}, $scope, 'vm.donations');

                vm.totalDonations = 0.00;
                vm.totalCosts = 0.00;

                vm.tally = function() {
                    vm.tallyDonations();
                    vm.tallyCosts();
                    vm.tallyGoals();
                };

                vm.donateButton = function() {
                    Donations.save({'amount': vm.newDonation.amount});
                };

                vm.tallyGoals = function() {
                    angular.forEach(vm.goals, function(goal) {
                        if (goal.end == null) {
                            goal.contributed = 0;
                            angular.forEach(vm.donations, function (donation) {
                                if (donation.created > goal.created) {
                                    goal.contributed -= -donation.amount;
                                }
                            });
                            goal.progress = (100 * goal.contributed) / goal.amount;
                            if (goal.progress > 100) {
                                goal.progress = 100;
                            }
                        }
                    }, vm.goals)
                };

                vm.tallyDonations = function() {
                    vm.totalDonations = 0.00;
                    angular.forEach(vm.donations, function(donation) {
                        vm.totalDonations -= -donation.amount;
                    });
                };

                vm.tallyCosts = function() {
                    angular.forEach(vm.costs, function(cost) {
                        vm.totalCosts -= -cost.amount;
                    })
                };

                vm.tally();
            }]);

}());
