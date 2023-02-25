/*!
    * Start Bootstrap - SB Admin v7.0.5 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2022 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }


    const dropdownButton = document.getElementById("my-dropdownMenuButton");
    const dropdownMenu = document.querySelector(".my-dropdown-menu");

    dropdownButton.addEventListener("click", function() {
    dropdownMenu.classList.toggle("show");
    });

    dropdownMenu.addEventListener("mouseout", function() {
    dropdownMenu.classList.remove("show");
    });
    dropdownMenu.addEventListener("mouseover", function() {
    dropdownMenu.classList.add("show");
    });


});
