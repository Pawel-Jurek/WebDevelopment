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
            .then(response => {
                if (response.ok) {
                    return response.text();
                } else {
                    console.error('Response is not OK');
                }
            })
            .then(text => {
                if (text && text.indexOf('DOCTYPE') === -1) {
                    return JSON.parse(text);
                } else {
                    window.location.href = '/accounts/login/';
                }
            })
            .then(response => {
                if (response) {
                    console.log('response', response);
                    var badgeSpan = document.querySelector(".badge");
                    if(badgeSpan){
                        badgeSpan.innerText = response.new_items;
                    } else {
                        var spanElement = document.createElement("span");
                        spanElement.classList.add("badge", "rounded-pill");
                        spanElement.style.backgroundColor = "brown";
                        spanElement.innerText = response.new_items;

                        var container = document.querySelector('#cart');
                        container.appendChild(spanElement);
                    }
                }
            })
            .catch(error => {
                console.error('Error', error);
            });
            return false;
        })
    });
})
