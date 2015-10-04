(function() {
    'use strict';

    angular.module('core')
        .directive('newsImage', [ function() {
            return function(scope, element, attrs){
                var url = attrs.newsImage;
                element.css({
                    'background-image': 'url(' + url +')',
                });
            };
        }]);

}());