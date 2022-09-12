$(document).ready(function() {
    // menu [desktop]
    const navbar = $('.navbar-expand-lg');

    const animateNavbar = () => {
        if ($(this).scrollTop() > 120) {
            navbar.removeClass('pt-4').addClass('bg-white shadow-sm');
        }
        if ($(this).scrollTop() < 120) {
            navbar.removeClass('bg-white shadow-sm').addClass('pt-4');
        }
    }

    if ($(window).innerWidth() > 991) {
        // at the beginning
        animateNavbar();

        // when scroll
        $(window).scroll(function () {
            animateNavbar();
        })
    }

    $('#goBack').click(() => {
        window.history.back();
    });
});