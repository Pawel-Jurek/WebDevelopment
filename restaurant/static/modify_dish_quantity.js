document.addEventListener('DOMContentLoaded', function() {
    const add_buttons = document.querySelectorAll('.increase-amount');
    const delete_buttons = document.querySelectorAll('.decrease-amount');
    //var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    add_buttons.forEach(button => {
        button.addEventListener('click', function(){
            dish_id = button.getAttribute('data-quantity');
            var quantity_p = document.querySelector(`#quantity${dish_id}`);
            console.log('num', quantity_p.textContent);
            num = parseInt(quantity_p.textContent);
            
            num += 1;
            quantity_p.textContent = num;
        })
    });

    delete_buttons.forEach(button => {
        button.addEventListener('click', function(){
            dish_id = button.getAttribute('data-quantity');
            var quantity_p = document.querySelector(`#quantity${dish_id}`);
            num = parseInt(quantity_p.textContent);
            if (num > 0) {
                num -= 1;
            }     
            quantity_p.textContent = num;
        })
    });

})