document.addEventListener('DOMContentLoaded', function(){
    const buttons = document.querySelectorAll('.tick_button')
    buttons.forEach(button => {
        var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        button.addEventListener('click', function(){
            const person_id = button.getAttribute('person-id');
            console.log('id', person_id);
            fetch(`/tick_person/${person_id}`,{
                method: 'PUT',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log('ticked', data.ticked)
                var person_field = document.querySelector(`#person-field${person_id}`);
                button.classList = ['tick_button btn']
                if(data.ticked){
                    button.textContent = 'Untick';
                    person_field.class = 'li-received';
                    button.classList.add('btn-danger');
                } else {
                    button.textContent = 'Tick';
                    button.classList.add('btn-success');
                    person_field.class = 'li-not-received';
                }
            })
            .catch(error => {
                console.error('Error', error);
            });
        })
        
    });
})