$(document).ready(function() {

	var cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	var cardSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]

	var Deck = GoFishBackend.Deck(function(response) {
		return response.GoFishBackend.getJSON(function(jsonResponse) {
			console.log(jsonResponse);
		})
	})
	console.log(Deck)
})
