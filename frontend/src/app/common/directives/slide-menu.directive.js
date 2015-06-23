(function() {
  'use strict';

  var module = angular.module('core');

  module.directive('sidePanel', function() {
    return {
      restrict: 'EA',
      templateUrl: '/side-panel.view.html',
      transclude: true,
      scope: {
        visible: '=',
        alignment: '@'
      }
    };
  })
  .directive('leftPanelHeader', [ function() {
    return {
      restrict: 'EA',
      replace: true,
      templateUrl: '/left-panel-header.view.html'
    };
  }])
  .directive('rightPanelHeader', [ function() {
    return {
      restrict: 'EA',
      replace: true,
      templateUrl: '/right-panel-header.view.html'
    };
  }]);


}());
