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
            const dish_id = button.getAttribute('data-dish_id');
            const dish_price = button.getAttribute('data-price');
            console.log('dishId', dish_id);
            var quantity_p = document.querySelector(`#quantity${dish_id}`);
            console.log('quantity', quantity_p.textContent);
            prices = document.querySelectorAll(`.price${dish_id}`);
            var quantity = parseInt(quantity_p.textContent);
            quantity_in_order_p = document.querySelector(`#dish-quantity-item${dish_id}`);
            var total_sum = document.querySelector('#total_sum');
            
            if (quantity > 0 || number > 0) {
                quantity += number;
                quantity_p.textContent = quantity;
                prices.forEach(price_p =>{
                    price_p.textContent = `${(dish_price*quantity).toFixed(2)} zł`;
                })
                actual_price = parseInt(total_sum.textContent);
                actual_price += number * dish_price;
                total_sum.textContent = actual_price.toFixed(2);
                quantity_in_order_p.innerHTML  =` x${quantity}`;
                
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