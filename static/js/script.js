$(document).ready(function() {
    $(".dropdown-button").dropdown({ hover: true });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('ul.tabs').tabs();
    $('select').formSelect(); //Pour le choix multiple
    //$('.datepicker').datepicker();//Pour date naissance
    //$('ul.tabs').tabs('select_tab', 'tab_id');
    $('.modal').modal();

});
$(document).ready(function() {

});



function nospaces(t) {

    if (t.value.match(/\s/g)) {

        alert('Désolé, vous n\'êtes pas autorisé à entrer des espaces');

        t.value = t.value.replace(/\s/g, '');

    }
};