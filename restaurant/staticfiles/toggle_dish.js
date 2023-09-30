document.addEventListener('DOMContentLoaded', function() {
    cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.width = "300px";
        card.addEventListener('click', function(){
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
            
            /*
            const collapse = card.querySelector('.collapse');
            
            // Jeśli jest otwarty, zamknij go
            if (collapse.classList.contains('show')) {
                collapse.classList.remove('show');
                card.classList.remove('col-6');
            } else {
                // Jeśli jest zamknięty, otwórz go i zmień szerokość karty na col-6
                collapse.classList.add('show');
                card.classList.add('col-6');
            }
            */
        })
    });
})