document.addEventListener('DOMContentLoaded', function() {
    buttons = document.querySelectorAll('.add-to-cart');
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    buttons.forEach(button => {
        button.addEventListener('click', function(){
            const dishId = button.getAttribute('data-id');

            fetch(`/dishes/add_to_cart/${dishId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': csrfToken
                },
            })
            .then(response => response.json())
            .then(response => {
                console.log('response', response);
                var badgeSpan = document.querySelector(".badge");
                badgeSpan.innerText = response.new_items;
            })
            .catch(error => {
                console.error('Error', error);
            });
            return false;
        })
    });

})