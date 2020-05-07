$(document).ready(function() {
    $('.sidenav').sidenav(); 
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $("select[required]").css({display: "block", height: 0, padding: 0, width: 0, position: "absolute"});
    $('textarea#recipe_description,input#recipe_name').characterCounter();
    $('.modal').modal();

 });