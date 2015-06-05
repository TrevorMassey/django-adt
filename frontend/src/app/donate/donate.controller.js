(function() {
    'use strict';

    angular.module('donate').controller('DonateCtrl', [
        '$scope', 'Donations', 'Costs',
        function($scope, Donations, Costs) {
            var vm = this;
            vm.goal = {amount : 816, visible: true};
            vm.totalDonations = 0;
            vm.totalCosts = 0;

            vm.donationQuery = function() {
                vm.donations = Donations.query(function () {
                    vm.tallyDonations();
                });
            };
            vm.costs = Costs.query(function() {
                vm.tallyCosts();
            });

            vm.donateButton = function() {
                Donations.save(vm.newDonation, function(donate) {
                    console.log(donate);
                    vm.donationQuery();
                }, function(error) {
                    console.log(error);
                });
            };

            vm.tallyDonations = function() {
                vm.totalDonations = 0;
                angular.forEach(vm.donations, function(donation) {
                    vm.totalDonations += donation.amount;
                });
            };

            vm.tallyCosts = function() {
                angular.forEach(vm.costs, function(cost) {
                    vm.totalCosts += cost.amount;
                })
            };

            vm.donationQuery();
    }]);

}());
