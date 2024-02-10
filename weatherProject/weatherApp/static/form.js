document.addEventListener('DOMContentLoaded', function() {
    var input = document.getElementById('cityInput');
    var suggestionsList = document.getElementById('suggestionsList');
    var selectedSuggestionIndex = -1;

    input.addEventListener('input', function() {
        var inputValue = input.value.trim();
        if (inputValue !== '') {
            fetch(`/get_city_suggestions/${inputValue}`)
                .then(response => response.json())
                .then(data => {
                    var suggestions = data.suggestions;
                    updateSuggestionsList(suggestions);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        } else {
            clearSuggestionsList();
        }
    });

    input.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
            event.preventDefault();
            navigateSuggestions(event.key === 'ArrowDown' ? 'down' : 'up');
        } else if (event.key === 'Enter') {
            selectSuggestion();
        }
    });

    function updateSuggestionsList(suggestions) {
        suggestionsList.innerHTML = ''; 
        selectedSuggestionIndex = -1; 
        suggestions.forEach(function(suggestion, index) {
            var listItem = document.createElement('li');
            listItem.textContent = suggestion.description;
            listItem.className = 'list-group-item';
            listItem.addEventListener('click', function() {
                input.value = suggestion.description;
                clearSuggestionsList();
            });
            suggestionsList.appendChild(listItem);
        });
        suggestionsContainer.style.display = 'block';
    }

    function clearSuggestionsList() {
        suggestionsList.innerHTML = ''; 
        suggestionsContainer.style.display = 'none'; 
    }

    function navigateSuggestions(direction) {
        var suggestionItems = suggestionsList.children;
        if (direction === 'down') {
            selectedSuggestionIndex = Math.min(selectedSuggestionIndex + 1, suggestionItems.length - 1);
        } else {
            selectedSuggestionIndex = Math.max(selectedSuggestionIndex - 1, -1);
        }
        Array.from(suggestionItems).forEach(function(item, index) {
            if (index === selectedSuggestionIndex) {
                item.classList.add('active');
                input.value = item.textContent;
            } else {
                item.classList.remove('active');
            }
        });
    }

    function selectSuggestion() {
        if (selectedSuggestionIndex !== -1) {
            var suggestion = suggestionsList.children[selectedSuggestionIndex];
            if (suggestion) {
                input.value = suggestion.textContent;
                clearSuggestionsList();
            }
        }
    }
});
