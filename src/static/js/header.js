$(document).ready(function() {
    $("li.nav-item.active").removeClass("active");
    $('a[href="' + location.pathname + '"]').parents("li").addClass("active");
    $("#sidebarCollapse").on("click", function () {
        $("#sidebar").toggleClass("active");
    });
});
