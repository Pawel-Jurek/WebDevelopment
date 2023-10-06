document.addEventListener('DOMContentLoaded', function(){
    const confirm_button = document.getElementById('confirm_order')
    const cost = document.querySelector('#total_sum').textContent;
    //var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    confirm_button.addEventListener('click', function(){
        let text = `Twoje zamówienie łącznie kosztuje ${cost}zł. Czy chcesz je potwierdzić?`;
        if (confirm(text) == true) {
            console.log('Order','confirmed');
          }
    })
})
