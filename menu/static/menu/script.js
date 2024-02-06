document.querySelectorAll('.menu li').forEach(item => {
    item.addEventListener('click', event => {
        const submenu = item.querySelector('.submenu');
        if (submenu) {
            event.preventDefault(); // Предотвращаем стандартное поведение ссылки
            // Сначала скрываем все подменю
            document.querySelectorAll('.submenu').forEach(sub => {
                sub.classList.remove('show');
            });
            // Затем показываем подменю, соответствующее выбранному пункту меню
            submenu.classList.toggle('show');
        }
    });
});