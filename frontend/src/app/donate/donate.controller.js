(function() {
    'use strict';

    angular.module('donate')
        .controller('DonateCtrl', [
            'common', 'Donation', 'Cost',
            function(common, Donation, Cost) {
                var vm = this;
                vm.goal = { amount : 816, visible: true };
                vm.totalDonations = 0;
                vm.totalCosts = 0;
                vm.costs = [];

                vm.donationQuery = function() {
                    Donation.findAll()
                        .then(function(data) {
                            vm.donations = data;
                        }).then(vm.tallyDonations);
                };

                Cost.findAll()
                    .then(function(data) {
                        vm.costs = data;
                    }).then(vm.tallyCosts);


                vm.donateButton = function() {
                    Donation.save(vm.newDonation, function(donate) {
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
