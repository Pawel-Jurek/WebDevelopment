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
                var badgeSpan = document.querySelector(".cart");
                if(badgeSpan){
                    badgeSpan.innerText = response.new_items;
                } else {
                    var spanElement = document.createElement("span");
                    spanElement.classList.add("badge", "rounded-pill");
                    spanElement.style.backgroundColor = "brown";
                    spanElement.innerText = response.new_items;

                    var container = document.getElementById("badge"); 
                    container.appendChild(spanElement);
                }          
            })
            .catch(error => {
                console.error('Error', error);
            });
            return false;
        })
    });

})