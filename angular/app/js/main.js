require.config({
	baseUrl: '/static/js/',
	paths: {
		jquery: '../lib/jquery',
		bootstrap: 'lib/bootstrap/js/bootstrap',
		underscore: 'lib/underscore/underscore',
		angular: '../lib/angular/angular',
		angularResource: '../lib/angular/angular-resource',
		text: '../lib/require/text'
	},
	shim: {
		'angular' : {'exports' : 'angular'},
		'angular-resource' : {deps:['angular']},
		'bootstrap': {deps:['jquery']},
		'underscore': {exports: '_'}
	},
	priority: [
		"angular"
	]
});

require( [
	'angular',
	'app',
	'services',
	'controllers',
	'filters',
	'directives',
	'routes'
], function(angular, app) {
	// hmmm?;
	// angular.element(document).ready(function () {
		angular.bootstrap(document, ['alchemy']);
	// });
});