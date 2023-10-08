document.addEventListener('DOMContentLoaded', function () {
    const confirm_button = document.getElementById('confirm_order');
    if(confirm_button){
        const cost = document.querySelector('#total_sum').textContent;
    const order_id = confirm_button.getAttribute('data-id');
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    confirm_button.addEventListener('click', function () {
        let text = `Twoje zamówienie łącznie kosztuje ${cost} zł. Czy chcesz je potwierdzić?`;

        if (confirm(text)) {
            fetch(`/order/confirm_order/${order_id}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
                .then(response => response.json())
                .then(response => {
                    if (response.status === 'success') {
                        $('#myModal').modal('show');
                    }
                })
                .catch(error => {
                    console.error('Error', error);
                });
        }

        $('#myModal').on('hidden.bs.modal', function () {
            window.location.href = '/';
        });

        return false;
    });
    }  
});

