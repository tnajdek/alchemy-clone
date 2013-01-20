define([
	'app',
	'controllers'
], function(app, controller) {
	return app.config(['$routeProvider', function($routeProvider) {
		$routeProvider.when('/itembuilder', {
			templateUrl: '/static/partials/itembuilder.html',
			controller: controller.Itembuilder
		});
		$routeProvider.when('/recipebuilder', {
			templateUrl: '/static/partials/recipebuilder.html',
			controller: controller.Recipebuilder
		});
		$routeProvider.when('/challenge', {
			templateUrl: '/static/partials/challenge.html',
			controller: controller.Challenge
		});
		$routeProvider.when('/', {
			templateUrl: '/static/partials/main.html',
			controller: controller.Main
		});
		$routeProvider.otherwise({
			redirectTo: '/'
		});
	}]);
});