document.addEventListener('DOMContentLoaded', function() {
    const add_buttons = document.querySelectorAll('.increase-amount');
    const delete_buttons = document.querySelectorAll('.decrease-amount');

    change_quantity(add_buttons, 1);
    change_quantity(delete_buttons, -1);
    

})

function change_quantity(buttons, number){
    buttons.forEach(button => {
        button.addEventListener('click', function(){
            const orderId = button.getAttribute('data-order');
            const dish_id = button.getAttribute('data-quantity');
            const dish_price = button.getAttribute('data-price');
            var quantity_p = document.querySelector(`#quantity${dish_id}`);
            price_p = document.querySelector(`#price${dish_id}`);
            var quantity = parseInt(quantity_p.textContent);
            
            if (quantity > 0 || number > 0) {
                quantity += number;
                quantity_p.textContent = quantity;
                price_p.textContent = `${(dish_price*quantity).toFixed(2)} zł`;
            }
            var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            fetch(`/order/cart/update_dish/${orderId}/${dish_id}/${quantity}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': csrfToken
                },
            })
            .then(response => response.json())
            .then(response => {
                console.log('response', response);       
            })
            .catch(error => {
                console.error('Error', error);
            });
            return false;
        })
    });
}