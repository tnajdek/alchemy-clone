define([
	'app',
	'controllers'
], function(app, controller) {
	return app.config(['$routeProvider', function($routeProvider) {
		$routeProvider.when('/itembuilder', {
			templateUrl: 'partials/itembuilder.html',
			controller: controller.Itembuilder
		});
		$routeProvider.when('/recipebuilder', {
			templateUrl: 'partials/recipebuilder.html',
			controller: 'Recipebuilder'
		});
		$routeProvider.when('/challenge', {
			templateUrl: 'partials/challenge.html',
			controller: 'Challenge'
		});
		$routeProvider.otherwise({
			templateUrl: 'partials/main.html',
			controller: 'Main'
		});
	}]);
});