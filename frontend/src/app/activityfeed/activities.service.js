(function() {
   'use strict';

// Create the Socket.io wrapper service
   angular.module('core').service('activities', ['auth', '$state',
       function(auth, $state) {

         var activities = {
           data: []
         };


         return activities;
       }
   ]);

}());
