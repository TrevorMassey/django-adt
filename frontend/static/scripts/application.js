/* ng-FitText.js v3.3.3
 * https://github.com/patrickmarabeas/ng-FitText.js
 *
 * Original jQuery project: https://github.com/davatron5000/FitText.js
 *
 * Copyright 2015, Patrick Marabeas http://marabeas.io
 * Released under the MIT license
 * http://opensource.org/licenses/mit-license.php
 *
 * Date: 06/05/2015
 */

(function(window, document, angular, undefined) {

  'use strict';

  angular.module('ngFitText', [])
    .value( 'config', {
      'debounce': false,
      'delay': 250,
      'loadDelay': 10,
      'min': undefined,
      'max': undefined
    })

    .directive('fittext', ['$timeout', 'config', 'fitTextConfig', function($timeout, config, fitTextConfig) {
      return {
        restrict: 'A',
        scope: true,
        link: function(scope, element, attrs) {
          angular.extend(config, fitTextConfig.config);

          element[0].style.display = 'inline-block';
          element[0].style.lineHeight = '1';

          var parent = element.parent();
          var compressor = attrs.fittext || 1;
          var loadDelay = attrs.fittextLoadDelay || config.loadDelay;
          var nl = element[0].querySelectorAll('[fittext-nl],[data-fittext-nl]').length || 1;
          var minFontSize = attrs.fittextMin || config.min || Number.NEGATIVE_INFINITY;
          var maxFontSize = attrs.fittextMax || config.max || Number.POSITIVE_INFINITY;

          var resizer = function() {
            element[0].style.fontSize = '10px';
            var ratio = element[0].offsetHeight / element[0].offsetWidth / nl;
            element[0].style.fontSize = Math.max(
              Math.min((parent[0].offsetWidth - 6) * ratio * compressor,
                parseFloat(maxFontSize)
              ),
              parseFloat(minFontSize)
            ) + 'px';
          };

          $timeout( function() { resizer() }, loadDelay);

          scope.$watch(attrs.ngModel, function() { resizer() });

          config.debounce
            ? angular.element(window).bind('resize', config.debounce(function(){ scope.$apply(resizer)}, config.delay))
            : angular.element(window).bind('resize', function(){ scope.$apply(resizer)});
        }
      }
    }])

    .provider('fitTextConfig', function() {
      var self = this;
      this.config = {};
      this.$get = function() {
        var extend = {};
        extend.config = self.config;
        return extend;
      };
      return this;
    });

})(window, document, angular);
/*
 * angular-ui-bootstrap
 * http://angular-ui.github.io/bootstrap/

 * Version: 0.13.0 - 2015-05-02
 * License: MIT
 */
angular.module("ui.bootstrap", ["ui.bootstrap.tpls","ui.bootstrap.collapse","ui.bootstrap.dropdown","ui.bootstrap.position","ui.bootstrap.bindHtml"]);
angular.module("ui.bootstrap.tpls", []);
angular.module('ui.bootstrap.collapse', [])

  .directive('collapse', ['$animate', function ($animate) {

    return {
      link: function (scope, element, attrs) {
        function expand() {
          element.removeClass('collapse').addClass('collapsing');
          $animate.addClass(element, 'in', {
            to: { height: element[0].scrollHeight + 'px' }
          }).then(expandDone);
        }

        function expandDone() {
          element.removeClass('collapsing');
          element.css({height: 'auto'});
        }

        function collapse() {
          element
            // IMPORTANT: The height must be set before adding "collapsing" class.
            // Otherwise, the browser attempts to animate from height 0 (in
            // collapsing class) to the given height here.
            .css({height: element[0].scrollHeight + 'px'})
            // initially all panel collapse have the collapse class, this removal
            // prevents the animation from jumping to collapsed state
            .removeClass('collapse')
            .addClass('collapsing');

          $animate.removeClass(element, 'in', {
            to: {height: '0'}
          }).then(collapseDone);
        }

        function collapseDone() {
          element.css({height: '0'}); // Required so that collapse works when animation is disabled
          element.removeClass('collapsing');
          element.addClass('collapse');
        }

        scope.$watch(attrs.collapse, function (shouldCollapse) {
          if (shouldCollapse) {
            collapse();
          } else {
            expand();
          }
        });
      }
    };
  }]);

angular.module('ui.bootstrap.dropdown', ['ui.bootstrap.position'])

.constant('dropdownConfig', {
  openClass: 'open'
})

.service('dropdownService', ['$document', '$rootScope', function($document, $rootScope) {
  var openScope = null;

  this.open = function( dropdownScope ) {
    if ( !openScope ) {
      $document.bind('click', closeDropdown);
      $document.bind('keydown', escapeKeyBind);
    }

    if ( openScope && openScope !== dropdownScope ) {
        openScope.isOpen = false;
    }

    openScope = dropdownScope;
  };

  this.close = function( dropdownScope ) {
    if ( openScope === dropdownScope ) {
      openScope = null;
      $document.unbind('click', closeDropdown);
      $document.unbind('keydown', escapeKeyBind);
    }
  };

  var closeDropdown = function( evt ) {
    // This method may still be called during the same mouse event that
    // unbound this event handler. So check openScope before proceeding.
    if (!openScope) { return; }

    if( evt && openScope.getAutoClose() === 'disabled' )  { return ; }

    var toggleElement = openScope.getToggleElement();
    if ( evt && toggleElement && toggleElement[0].contains(evt.target) ) {
        return;
    }

    var $element = openScope.getElement();
    if( evt && openScope.getAutoClose() === 'outsideClick' && $element && $element[0].contains(evt.target) ) {
      return;
    }

    openScope.isOpen = false;

    if (!$rootScope.$$phase) {
      openScope.$apply();
    }
  };

  var escapeKeyBind = function( evt ) {
    if ( evt.which === 27 ) {
      openScope.focusToggleElement();
      closeDropdown();
    }
  };
}])

.controller('DropdownController', ['$scope', '$attrs', '$parse', 'dropdownConfig', 'dropdownService', '$animate', '$position', '$document', function($scope, $attrs, $parse, dropdownConfig, dropdownService, $animate, $position, $document) {
  var self = this,
      scope = $scope.$new(), // create a child scope so we are not polluting original one
      openClass = dropdownConfig.openClass,
      getIsOpen,
      setIsOpen = angular.noop,
      toggleInvoker = $attrs.onToggle ? $parse($attrs.onToggle) : angular.noop,
      appendToBody = false;

  this.init = function( element ) {
    self.$element = element;

    if ( $attrs.isOpen ) {
      getIsOpen = $parse($attrs.isOpen);
      setIsOpen = getIsOpen.assign;

      $scope.$watch(getIsOpen, function(value) {
        scope.isOpen = !!value;
      });
    }

    appendToBody = angular.isDefined($attrs.dropdownAppendToBody);

    if ( appendToBody && self.dropdownMenu ) {
      $document.find('body').append( self.dropdownMenu );
      element.on('$destroy', function handleDestroyEvent() {
        self.dropdownMenu.remove();
      });
    }
  };

  this.toggle = function( open ) {
    return scope.isOpen = arguments.length ? !!open : !scope.isOpen;
  };

  // Allow other directives to watch status
  this.isOpen = function() {
    return scope.isOpen;
  };

  scope.getToggleElement = function() {
    return self.toggleElement;
  };

  scope.getAutoClose = function() {
    return $attrs.autoClose || 'always'; //or 'outsideClick' or 'disabled'
  };

  scope.getElement = function() {
    return self.$element;
  };

  scope.focusToggleElement = function() {
    if ( self.toggleElement ) {
      self.toggleElement[0].focus();
    }
  };

  scope.$watch('isOpen', function( isOpen, wasOpen ) {
    if ( appendToBody && self.dropdownMenu ) {
      var pos = $position.positionElements(self.$element, self.dropdownMenu, 'bottom-left', true);
      self.dropdownMenu.css({
        top: pos.top + 'px',
        left: pos.left + 'px',
        display: isOpen ? 'block' : 'none'
      });
    }

    $animate[isOpen ? 'addClass' : 'removeClass'](self.$element, openClass);

    if ( isOpen ) {
      scope.focusToggleElement();
      dropdownService.open( scope );
    } else {
      dropdownService.close( scope );
    }

    setIsOpen($scope, isOpen);
    if (angular.isDefined(isOpen) && isOpen !== wasOpen) {
      toggleInvoker($scope, { open: !!isOpen });
    }
  });

  $scope.$on('$locationChangeSuccess', function() {
    scope.isOpen = false;
  });

  $scope.$on('$destroy', function() {
    scope.$destroy();
  });
}])

.directive('dropdown', function() {
  return {
    controller: 'DropdownController',
    link: function(scope, element, attrs, dropdownCtrl) {
      dropdownCtrl.init( element );
    }
  };
})

.directive('dropdownMenu', function() {
  return {
    restrict: 'AC',
    require: '?^dropdown',
    link: function(scope, element, attrs, dropdownCtrl) {
      if ( !dropdownCtrl ) {
        return;
      }
      dropdownCtrl.dropdownMenu = element;
    }
  };
})

.directive('dropdownToggle', function() {
  return {
    require: '?^dropdown',
    link: function(scope, element, attrs, dropdownCtrl) {
      if ( !dropdownCtrl ) {
        return;
      }

      dropdownCtrl.toggleElement = element;

      var toggleDropdown = function(event) {
        event.preventDefault();

        if ( !element.hasClass('disabled') && !attrs.disabled ) {
          scope.$apply(function() {
            dropdownCtrl.toggle();
          });
        }
      };

      element.bind('click', toggleDropdown);

      // WAI-ARIA
      element.attr({ 'aria-haspopup': true, 'aria-expanded': false });
      scope.$watch(dropdownCtrl.isOpen, function( isOpen ) {
        element.attr('aria-expanded', !!isOpen);
      });

      scope.$on('$destroy', function() {
        element.unbind('click', toggleDropdown);
      });
    }
  };
});

angular.module('ui.bootstrap.position', [])

/**
 * A set of utility methods that can be use to retrieve position of DOM elements.
 * It is meant to be used where we need to absolute-position DOM elements in
 * relation to other, existing elements (this is the case for tooltips, popovers,
 * typeahead suggestions etc.).
 */
  .factory('$position', ['$document', '$window', function ($document, $window) {

    function getStyle(el, cssprop) {
      if (el.currentStyle) { //IE
        return el.currentStyle[cssprop];
      } else if ($window.getComputedStyle) {
        return $window.getComputedStyle(el)[cssprop];
      }
      // finally try and get inline style
      return el.style[cssprop];
    }

    /**
     * Checks if a given element is statically positioned
     * @param element - raw DOM element
     */
    function isStaticPositioned(element) {
      return (getStyle(element, 'position') || 'static' ) === 'static';
    }

    /**
     * returns the closest, non-statically positioned parentOffset of a given element
     * @param element
     */
    var parentOffsetEl = function (element) {
      var docDomEl = $document[0];
      var offsetParent = element.offsetParent || docDomEl;
      while (offsetParent && offsetParent !== docDomEl && isStaticPositioned(offsetParent) ) {
        offsetParent = offsetParent.offsetParent;
      }
      return offsetParent || docDomEl;
    };

    return {
      /**
       * Provides read-only equivalent of jQuery's position function:
       * http://api.jquery.com/position/
       */
      position: function (element) {
        var elBCR = this.offset(element);
        var offsetParentBCR = { top: 0, left: 0 };
        var offsetParentEl = parentOffsetEl(element[0]);
        if (offsetParentEl != $document[0]) {
          offsetParentBCR = this.offset(angular.element(offsetParentEl));
          offsetParentBCR.top += offsetParentEl.clientTop - offsetParentEl.scrollTop;
          offsetParentBCR.left += offsetParentEl.clientLeft - offsetParentEl.scrollLeft;
        }

        var boundingClientRect = element[0].getBoundingClientRect();
        return {
          width: boundingClientRect.width || element.prop('offsetWidth'),
          height: boundingClientRect.height || element.prop('offsetHeight'),
          top: elBCR.top - offsetParentBCR.top,
          left: elBCR.left - offsetParentBCR.left
        };
      },

      /**
       * Provides read-only equivalent of jQuery's offset function:
       * http://api.jquery.com/offset/
       */
      offset: function (element) {
        var boundingClientRect = element[0].getBoundingClientRect();
        return {
          width: boundingClientRect.width || element.prop('offsetWidth'),
          height: boundingClientRect.height || element.prop('offsetHeight'),
          top: boundingClientRect.top + ($window.pageYOffset || $document[0].documentElement.scrollTop),
          left: boundingClientRect.left + ($window.pageXOffset || $document[0].documentElement.scrollLeft)
        };
      },

      /**
       * Provides coordinates for the targetEl in relation to hostEl
       */
      positionElements: function (hostEl, targetEl, positionStr, appendToBody) {

        var positionStrParts = positionStr.split('-');
        var pos0 = positionStrParts[0], pos1 = positionStrParts[1] || 'center';

        var hostElPos,
          targetElWidth,
          targetElHeight,
          targetElPos;

        hostElPos = appendToBody ? this.offset(hostEl) : this.position(hostEl);

        targetElWidth = targetEl.prop('offsetWidth');
        targetElHeight = targetEl.prop('offsetHeight');

        var shiftWidth = {
          center: function () {
            return hostElPos.left + hostElPos.width / 2 - targetElWidth / 2;
          },
          left: function () {
            return hostElPos.left;
          },
          right: function () {
            return hostElPos.left + hostElPos.width;
          }
        };

        var shiftHeight = {
          center: function () {
            return hostElPos.top + hostElPos.height / 2 - targetElHeight / 2;
          },
          top: function () {
            return hostElPos.top;
          },
          bottom: function () {
            return hostElPos.top + hostElPos.height;
          }
        };

        switch (pos0) {
          case 'right':
            targetElPos = {
              top: shiftHeight[pos1](),
              left: shiftWidth[pos0]()
            };
            break;
          case 'left':
            targetElPos = {
              top: shiftHeight[pos1](),
              left: hostElPos.left - targetElWidth
            };
            break;
          case 'bottom':
            targetElPos = {
              top: shiftHeight[pos0](),
              left: shiftWidth[pos1]()
            };
            break;
          default:
            targetElPos = {
              top: hostElPos.top - targetElHeight,
              left: shiftWidth[pos1]()
            };
            break;
        }

        return targetElPos;
      }
    };
  }]);

angular.module('ui.bootstrap.bindHtml', [])

  .directive('bindHtmlUnsafe', function () {
    return function (scope, element, attr) {
      element.addClass('ng-binding').data('$binding', attr.bindHtmlUnsafe);
      scope.$watch(attr.bindHtmlUnsafe, function bindHtmlUnsafeWatchAction(value) {
        element.html(value || '');
      });
    };
  });

// Init the application configuration module for AngularJS application
var ApplicationConfiguration = (function() {
    'use strict';

	// Init module configuration options
	var applicationModuleName = 'app';
	var applicationModuleVendorDependencies = [
		//'ngResource',
        //'ngMessages',
		//'ngAnimate',
        'templates',
        'ui.router',
		'satellizer',
		'ui.bootstrap',
		'mgcrea.ngStrap',

        'rx',
		//'angularMoment',
		//'sun.scrollable',
		'ncy-angular-breadcrumb',
		//'angular-loading-bar',
		//'restangular',
		//'ui.tree',
		'ngFitText'
	];

	// Add a new vertical module
	var registerModule = function(moduleName, dependencies) {
		// Create angular module
		angular.module(moduleName, dependencies || []);

		// Add the module to the AngularJS configuration file
		angular.module(applicationModuleName).requires.push(moduleName);
	};

	return {
		applicationModuleName: applicationModuleName,
		applicationModuleVendorDependencies: applicationModuleVendorDependencies,
		registerModule: registerModule
	};
})();

(function() {
    'use strict';

//Start by defining the main module and adding the module dependencies
    angular.module(ApplicationConfiguration.applicationModuleName, ApplicationConfiguration.applicationModuleVendorDependencies);

// Setting HTML5 Location Mode
    angular.module(ApplicationConfiguration.applicationModuleName).config([
        '$locationProvider', '$urlRouterProvider',
        function($locationProvider, $urlRouterProvider) {

            $locationProvider.html5Mode(true).hashPrefix('!');

            // For any unmatched url, redirect to '/'
            $urlRouterProvider.otherwise('/');

        }
    ]);

//Then define the init function for starting up the application
    angular.element(document).ready(function() {
        //Fixing facebook bug with redirect
        if (window.location.hash === '#_=_') window.location.hash = '#!';

        //Then init the app
        angular.bootstrap(document, [ApplicationConfiguration.applicationModuleName]);
    });

}());
(function() {
    'use strict';

    // Use Applicaion configuration module to register a new module
    ApplicationConfiguration.registerModule('auth');

}());
(function() {
    'use strict';

    // Use Applicaion configuration module to register a new module
    ApplicationConfiguration.registerModule('core');

}());
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

(function() {
    'use strict';

    angular.module('core')
        .directive('activityList', [ function() {
            return {
                restrict: 'EA',
                templateUrl: '/right-panel.view.html',
                controller: ['$scope', 'activities', function($scope, activities) {
                    $scope.activities = activities;

                }]
            };
        }]);
}());

(function() {
    'use strict';

    angular.module('core').controller('MessageCtrl', ['$scope', 'auth', 'activities',
        function($scope, auth, activities) {

            $scope.message = {};


            $scope.createMessage = function() {
                alert('Need to implement method');
            };


        }]);

}());

//(function() {
//    'use strict';
//
//// Create the Socket.io wrapper service
//    angular.module('core').service('Message', ['$resource', 'auth', '$state',
//        function($resource, auth, $state) {
//            return $resource('http://localhost:1337/message');
//
//
//        }
//    ]);
//
//}());
(function() {
    'use strict';

    angular.module('auth')
        .config(['$locationProvider', '$stateProvider', '$urlRouterProvider', '$authProvider',
            function ($locationProvider, $stateProvider, $urlRouterProvider, $authProvider) {
                $stateProvider
                    .state('signin', {
                        url: '/signin',
                        templateUrl :  '/signin.view.html',
                        controller: 'SigninCtrl as vm'
                    })
                    .state('signup', {
                        url: '/signup',
                        templateUrl: '/signup.view.html',
                        controller: 'SignupCtrl as vm'
                    })
                    .state('logout', {
                        url: '/logout',
                        template: null,
                        controller: 'LogoutCtrl'
                    });

                $authProvider.httpInterceptor = true;
                $authProvider.withCredentials = true;
                $authProvider.loginRedirect = '/';
                $authProvider.logoutRedirect = '/';
                $authProvider.signupRedirect = '/login';
                $authProvider.loginUrl = 'api-token-auth/';
                $authProvider.signupUrl = 'api-token-auth/';
                $authProvider.loginRoute = '/signin';
                $authProvider.signupRoute = '/signup';

            }]);
}());
(function() {
    'use strict';

    angular.module('auth').factory('auth', [
        'config', '$auth', '$http', '$q',
        function(config, $auth, $http, $q) {
            var service = {
                currentUser: null
            };

            var payload = null;

            angular.extend(service, $auth);
            return service;
        }]);
}());
(function() {
    'use strict';

    angular.module('auth')
        .controller('SigninCtrl',['$location', 'auth', function($location, auth) {

            if (auth.isAuthenticated()) $location.path('/');
            var vm = this;

            vm.login = function () {
                var credentials = {
                    email: vm.credentials.email,
                    password: vm.credentials.password
                };

                auth.login(credentials)
                    .then(function(response) {
                        vm.credentials = {};
                    })
                    .catch(function(error) {
                        console.log(error);
                    })
            };

        }]);

}());
(function() {
    'use strict';

    angular.module('auth')
        .controller('SignupCtrl',['$location', 'auth', function($location, auth) {

            if (auth.isAuthenticated()) $location.path('/');
            var vm = this;
            vm.credentials = {};

            vm.signup = function () {
                auth.signup(vm.credentials)
                    .then(function(response) {
                        vm.credentials = {};
                    })
                    .catch(function(error) {
                        console.log(error);
                    });
            };

        }]);

}());
(function() {
    'use strict';

    var API_URL = 'http://localhost:1337';

    var config = {
        API_URL: API_URL
    };

    angular.module('core').value('config', config);

    //angular.module('core').config(function(RestangularProvider) {
    //    RestangularProvider.setBaseUrl('/api/');
    //})

}());

(function() {
    'use strict';

    angular.module('core').controller('AppCtrl', [
        '$scope', '$location', 'auth',
        function($scope, $location, auth) {

        $scope.session = { currentUser: {} };
        $scope.site = { title: "Addiction "};
        $scope.isAuthenticated = isAuthenticated;
        $scope.toggleLeftPanel = toggleLeftPanel;
        $scope.toggleRightPanel = toggleRightPanel;
        $scope.leftVisible = true;
        $scope.rightVisible = true;
        $scope.navLocation = '/' + $location.url().split('/')[1];

        ////$scope.isCollapsed = true;
        //
        //$scope.session.currentUser = auth.currentUser;

        $scope.toggleCollapsibleMenu = function() {
            $scope.isCollapsed = !$scope.isCollapsed;
        };
        function isAuthenticated() {
            return auth.isAuthenticated();
        }

        function toggleLeftPanel(e) {
            $scope.leftVisible = !$scope.leftVisible;
            e.stopPropagation();
        }

        function toggleRightPanel(e) {
            $scope.rightVisible = !$scope.rightVisible;
            e.stopPropagation();
        }

        $scope.setLocation = function (viewLocation) {
            console.log(viewLocation);
            $scope.navLocation = viewLocation;
        };

        $scope.isActive = function (viewLocation) {
            return $scope.navLocation === viewLocation;
        }

    }]);

}());

(function() {
    'use strict';


    angular.module('core').config(['$stateProvider', '$urlRouterProvider',
        function ($stateProvider, $urlRouterProvider) {
            $stateProvider
                .state('home', {
                    url: '/',
                    templateUrl: '/home.view.html'
                });


        }]).run([
        '$rootScope',
        '$state',
        '$stateParams',
        function ($rootScope, $state, $stateParams) {
            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;

        }]);

}());
(function() {
    'use strict';

    angular.module('core')
        .directive('onlineUserList', [
            '$document', '$timeout', 'auth', 'rx',
            function($document, $timeout, auth, rx) {
                return {
                    restrict: 'EA',
                    templateUrl: '/online-users-list.view.html',
                    controller: function($scope) {
                        var vm = this;
                        vm.users = { data: [] };
                        var count = 0;

                        var fakeData = [
                            {"_id":"545ab71635fe5a08006d5814","username":"Gromph","email":"wrath625@gmail.com"},
                            {"_id":"54bda4c8b489a1e61072e67b","username":"Dashra","email":"caeadorn@yahoo.com"},
                            {"_id":"54814ee674b2689c93dd0b540","username":"Liminsathil","email":"lim@example.com"},
                            {"_id":"54751aa5ec6c5539da5c2354","username":"Akrylis","email":"unkleara@gmail.com"},
                            {"_id":"546aaa41d2abfe9aab10eb0c","username":"Shadow","email":"shadow@example.com"},
                            {"_id":"545ab585aea9100800421908","username":"Unkle","email":"unkleara@gmail.com"}
                        ];

                        angular.copy(fakeData, vm.users.data);
                        console.log(vm.users.data);
                        // Rx subscribe to mousemove events as 2.5s interval
                        // Check to see if current user is logged in to mark them online

                        // TODO: add unsubsribe when user is online and subscribe when is active again
                        var mousemove = rx.Observable.fromEvent($document, 'mousemove');


                        var mousemoveSubscription = mousemove.throttle(2500)
                            .filter(function(event) {
                                //if (auth.isAuthenticated() && (event.clientY >= 100))

                                //console.log('client: ' + event.clientY);
                                //console.log('page: ' + event.pageY);
                                //console.log('offset: ' + event.offsetY);
                                    return event;
                            });
                            //.throttle(500).forEach(function () {
                              //  setUserOnline();
                            //});

                        var REFRESH_ONLINE_STATUS_INTERVAL = 250;
                        var onlineUsersSubscription = rx.Observable.interval(1000)
                            .safeApply($scope, function() {
                                angular.forEach(vm.users.data, function (user) {

                                    user.msUntilInactive -= REFRESH_ONLINE_STATUS_INTERVAL;
                                    //user.signedIn = user.msUntilInactive > 0;
                                    user.signedIn = true;
                                });
                            });

                            //add mousemove subscribe as well
                            mousemoveSubscription.subscribe();

                            onlineUsersSubscription.subscribe();


                            //mousemoveSubscription.dispose();
                            //onlineUsersSubscription.dispose();


                    },
                    controllerAs: 'vm',
                    bindToController: true
                };
            }])

}());

angular.module('auth')
  .directive('passwordMatch', function() {
    return {
      require: 'ngModel',
      scope: {
        otherModelValue: '=passwordMatch'
      },
      link: function(scope, element, attributes, ngModel) {
        ngModel.$validators.compareTo = function(modelValue) {
          return modelValue === scope.otherModelValue;
        };
        scope.$watch('otherModelValue', function() {
          ngModel.$validate();
        });
      }
    };
  });


angular.module('auth')
  .directive('passwordStrength', function() {
    return {
      restrict: 'A',
      require: 'ngModel',
      link: function(scope, element, attrs, ngModel) {
        var indicator = element.children();
        var dots = Array.prototype.slice.call(indicator.children());
        var weakest = dots.slice(-1)[0];
        var weak = dots.slice(-2);
        var strong = dots.slice(-3);
        var strongest = dots.slice(-4);

        element.after(indicator);

        element.bind('keyup', function() {
          var matches = {
                positive: {},
                negative: {}
              },
              counts = {
                positive: {},
                negative: {}
              },
              tmp,
              strength = 0,
              letters = 'abcdefghijklmnopqrstuvwxyz',
              numbers = '01234567890',
              symbols = '\\!@#$%&/()=?¿',
              strValue;

          angular.forEach(dots, function(el) {
            el.style.backgroundColor = '#ebeef1';
          });
          
          if (ngModel.$viewValue) {
            // Increase strength level
            matches.positive.lower = ngModel.$viewValue.match(/[a-z]/g);
            matches.positive.upper = ngModel.$viewValue.match(/[A-Z]/g);
            matches.positive.numbers = ngModel.$viewValue.match(/\d/g);
            matches.positive.symbols = ngModel.$viewValue.match(/[$-/:-?{-~!^_`\[\]]/g);
            matches.positive.middleNumber = ngModel.$viewValue.slice(1, -1).match(/\d/g);
            matches.positive.middleSymbol = ngModel.$viewValue.slice(1, -1).match(/[$-/:-?{-~!^_`\[\]]/g);

            counts.positive.lower = matches.positive.lower ? matches.positive.lower.length : 0;
            counts.positive.upper = matches.positive.upper ? matches.positive.upper.length : 0;
            counts.positive.numbers = matches.positive.numbers ? matches.positive.numbers.length : 0;
            counts.positive.symbols = matches.positive.symbols ? matches.positive.symbols.length : 0;

            counts.positive.numChars = ngModel.$viewValue.length;
            tmp += (counts.positive.numChars >= 8) ? 1 : 0;

            counts.positive.requirements = (tmp >= 3) ? tmp : 0;
            counts.positive.middleNumber = matches.positive.middleNumber ? matches.positive.middleNumber.length : 0;
            counts.positive.middleSymbol = matches.positive.middleSymbol ? matches.positive.middleSymbol.length : 0;

            // Decrease strength level
            matches.negative.consecLower = ngModel.$viewValue.match(/(?=([a-z]{2}))/g);
            matches.negative.consecUpper = ngModel.$viewValue.match(/(?=([A-Z]{2}))/g);
            matches.negative.consecNumbers = ngModel.$viewValue.match(/(?=(\d{2}))/g);
            matches.negative.onlyNumbers = ngModel.$viewValue.match(/^[0-9]*$/g);
            matches.negative.onlyLetters = ngModel.$viewValue.match(/^([a-z]|[A-Z])*$/g);

            counts.negative.consecLower = matches.negative.consecLower ? matches.negative.consecLower.length : 0;
            counts.negative.consecUpper = matches.negative.consecUpper ? matches.negative.consecUpper.length : 0;
            counts.negative.consecNumbers = matches.negative.consecNumbers ? matches.negative.consecNumbers.length : 0;

            // Calculations
            strength += counts.positive.numChars * 4;
            if (counts.positive.upper) {
              strength += (counts.positive.numChars - counts.positive.upper) * 2;
            }
            if (counts.positive.lower) {
              strength += (counts.positive.numChars - counts.positive.lower) * 2;
            }
            if (counts.positive.upper || counts.positive.lower) {
              strength += counts.positive.numbers * 4;
            }
            strength += counts.positive.symbols * 6;
            strength += (counts.positive.middleSymbol + counts.positive.middleNumber) * 2;
            strength += counts.positive.requirements * 2;

            strength -= counts.negative.consecLower * 2;
            strength -= counts.negative.consecUpper * 2;
            strength -= counts.negative.consecNumbers * 2;

            if (matches.negative.onlyNumbers) {
              strength -= counts.positive.numChars;
            }
            if (matches.negative.onlyLetters) {
              strength -= counts.positive.numChars;
            }

            strength = Math.max(0, Math.min(100, Math.round(strength)));

            if (strength > 85) {
              angular.forEach(strongest, function(el) {
                el.style.backgroundColor = '#008cdd';
              });
            } else if (strength > 65) {
              angular.forEach(strong, function(el) {
                el.style.backgroundColor = '#6ead09';
              });
            } else if (strength > 30) {
              angular.forEach(weak, function(el) {
                el.style.backgroundColor = '#e09115';
              });
            } else {
              weakest.style.backgroundColor = '#e01414';
            }
          }
        });
      },
      template: '<span class="password-strength-indicator"><span></span><span></span><span></span><span></span></span>'
    };
  });
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
      templateUrl: '/left-panel-header.view.html'
    };
  }])
  .directive('rightPanelHeader', [ function() {
    return {
      restrict: 'EA',
      templateUrl: '/right-panel-header.view.html'
    };
  }]);


}());

(function() {
    'use strict';

    angular.module('core')
        .directive('navBar', [ function() {
            return {
                restrict: 'EA',
                templateUrl: '/navbar.view.html'
            };
        }]);
}());