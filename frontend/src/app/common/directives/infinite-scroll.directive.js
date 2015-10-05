// This was an angular-only directive I found.  Apparently it only works if you have an elemeny with overflow: auto CSS applied to it.  worthless


//(function() {
//  'use strict';
//angular.module('common')
//    .directive('infiniteScroll', [ "$window", function ($window) {
//        return {
//            link:function (scope, element, attrs) {
//                var offset = parseInt(attrs.threshold) || 100;
//                var e = element[0];
//
//                element.bind('scroll', function () {
//                    if (scope.$eval(attrs.canLoad) && e.scrollTop + e.offsetHeight >= e.scrollHeight - offset) {
//                        scope.$apply(attrs.infiniteScroll);
//                    }
//                });
//            }
//        };
//    }]);
//}());