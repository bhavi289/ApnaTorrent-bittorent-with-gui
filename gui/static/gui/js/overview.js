$(document).ready(function () {
	$('#drinkingCircliful').circliful({
		getText: function () {
			if (this.usesTotal())
				return Math.round(50);
			else
				return 50;
		},
		getInfoText: function () {
			return "% DOWNLOADED";
		},
		'dimension': 250,
		'background-fill-color': '#fff',
		'background-radius': 100,
		'foreground-radius': 110,
		'background-width': 15,
		'background-stroke-color': '#808080',
	});
	$('#drinkingCircliful').circliful('setSetting', 'foreground-color', '#33FF33');
	$('#drinkingCircliful').circliful('animateToValue', 50);
});
