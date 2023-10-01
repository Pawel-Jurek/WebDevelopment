document.addEventListener('DOMContentLoaded', function() {
    const toggle_parts = document.querySelectorAll('.toggle-part');

    toggle_parts.forEach(toggle_part => {
        const card = toggle_part.closest('.card');

        toggle_part.addEventListener('click', function(){
            const collapse = card.querySelector('.collapse');
            
            if(card.classList.contains('opened')){
                card.classList.remove('opened');
                collapse.classList.remove('show');
                card.style.width = '300px';
            } else {
                card.classList.add('opened');
                collapse.classList.add('show');
                card.style.width = '600px';
            }
        });
    });
});