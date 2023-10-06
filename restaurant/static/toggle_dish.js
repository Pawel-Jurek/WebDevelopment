document.addEventListener('DOMContentLoaded', function() {
    const toggle_parts = document.querySelectorAll('.toggle-part');

    toggle_parts.forEach(toggle_part => {
        const card = toggle_part.closest('.card');
        const collapse = card.querySelector('.collapse');

        toggle_part.addEventListener('click', function(){  
            if(collapse.classList.contains('show')){
                collapse.classList.remove('show');
                card.style.width = '300px';
            } else {
                card.style.width = '600px';
                setTimeout(function() {
                    collapse.classList.add('show');
                }, 150);
            }
        });
    });
});

