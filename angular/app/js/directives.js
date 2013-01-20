define(['app'], function(app) {
	'use strict';

	app.directive('appVersion', ['version', function (version) {
		return function(scope, elm, attrs) {
		elm.text(version);
		};
	}]);
});