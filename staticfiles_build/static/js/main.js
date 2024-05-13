const togglebtn = document.querySelector('.toggle-btn')
        const togglebtnIcon = document.querySelector('.toggle-btn i')
        const dropDown = document.querySelector('.drop_down')

        togglebtn.onclick = function() {
            dropDown.classList.toggle('open')

            const isOpen = dropDown.classList.contains('open')

            togglebtnIcon.classList = isOpen
            ? 'fa-solid fa-xmark'
            : 'fa-solid fa-bars'
        }