$(document).ready(function() {
    $('.sidenav').sidenav(); 
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();

    //CREDITS: The approach of validation select option for a dropdown is taken from
    //StackOverflow: https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown
    $("select[required]").css({display: "block", height: 0, padding: 0, width: 0, position: "absolute"});
    $('textarea#recipe_description,input#recipe_name').characterCounter();
    $('.tooltipped').tooltip();
    $('.modal').modal();

    //Resize button on a home page when it is hovered 
    $("#btn-home").mouseout(function() {
        $(this).css("transform", "scale(1)");   
    });
    $("#btn-home").mouseover(function() {
        $(this).css("transform", "scale(1.05)");
    });
});
