$(document).ready(function () {
    $("#ls").click(function () {
        $(".hi").slideToggle();
        $("#ls").toggleClass("fa-ellipsis-v");
        $(".itms").toggleClass("list-click");
        $(".cont2").toggleClass("list-click");

    });
    // $(window).scroll(function () {
    //     var width = screen.width;
    //     var scroll = $(window).scrollTop();
    //     if (width >= 1200) {
    //         if (scroll > 575) {
    //             $(".navbars").css("background-color", "white");
    //             $(".navbars").css("color", "black");
    //             $(".actives").css("background-color", "darkgray");
    //             $(".actives").css("color", "black");
    //             $(".navbars").hover(function () {
    //                 $(this).css("background-color", "white");
    //                 $(this).css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //             });
    //         }
    //         else {
    //             $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //             $(".navbars").css("color", "black");
    //             $(".actives").css("background-color", "darkgray");
    //             $(".actives").css("color", "black");
    //             $(".navbars").hover(function () {
    //                 $(this).css("background-color", "white");
    //                 $(this).css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //             }, function () {
    //                 $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                 $(".navbars").css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //                 $(".actives").css("color", "black");

    //             });
    //             $(".actives").hover(function () {
    //                 $(this).css("color", "black");
    //             });
    //         }
    //     }
    //     else {
    //         if (width > 800) {
    //             if (width <= 1000) {
    //                 if (scroll > 650) {
    //                     $(".navbars").css("background-color", "white");
    //                     $(".navbars").css("color", "black");
    //                     $(".actives").css("background-color", "darkgray");
    //                     $(".actives").css("color", "black");
    //                     $(".navbars").hover(function () {
    //                         $(this).css("background-color", "white");
    //                         $(this).css("color", "black");
    //                         $(".actives").css("background-color", "darkgray");
    //                     });
    //                 }
    //                 else {
    //                     $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                     $(".navbars").css("color", "black");
    //                     $(".actives").css("background-color", "darkgray");
    //                     $(".actives").css("color", "black");
    //                     $(".navbars").hover(function () {
    //                         $(this).css("background-color", "white");
    //                         $(this).css("color", "black");
    //                         $(".actives").css("background-color", "darkgray");
    //                     }, function () {
    //                         $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                         $(".navbars").css("color", "black");
    //                         $(".actives").css("background-color", "darkgray");
    //                         $(".actives").css("color", "black");

    //                     });
    //                     $(".actives").hover(function () {
    //                         $(this).css("color", "black");
    //                     });
    //                 }
    //             }
    //         }
    //     }
    //     if (width > 600) {
    //         if (width <= 800) {
    //             if (scroll > 650) {
    //                 $(".navbars").css("background-color", "white");
    //                 $(".navbars").css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //                 $(".actives").css("color", "black");
    //                 $(".navbars").hover(function () {
    //                     $(this).css("background-color", "white");
    //                     $(this).css("color", "black");
    //                     $(".actives").css("background-color", "darkgray");
    //                 });
    //             }
    //             else {
    //                 $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                 $(".navbars").css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //                 $(".actives").css("color", "black");
    //                 $(".navbars").hover(function () {
    //                     $(this).css("background-color", "white");
    //                     $(this).css("color", "black");
    //                     $(".actives").css("background-color", "darkgray");
    //                 }, function () {
    //                     $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                     $(".navbars").css("color", "black");
    //                     $(".actives").css("background-color", "darkgray");
    //                     $(".actives").css("color", "black");

    //                 });
    //                 $(".actives").hover(function () {
    //                     $(this).css("color", "black");
    //                 });
    //             }
    //         }
    //     }
    //     if (width <= 600) {
    //         if (scroll > 800) {
    //             $(".navbars").css("background-color", "white");
    //             $(".navbars").css("color", "black");
    //             $(".actives").css("background-color", "darkgray");
    //             $(".actives").css("color", "black");
    //             $(".navbars").hover(function () {
    //                 $(this).css("background-color", "white");
    //                 $(this).css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //             });
    //         }
    //         else {
    //             $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //             $(".navbars").css("color", "black");
    //             $(".actives").css("background-color", "darkgray");
    //             $(".actives").css("color", "black");
    //             $(".navbars").hover(function () {
    //                 $(this).css("background-color", "white");
    //                 $(this).css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //             }, function () {
    //                 $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
    //                 $(".navbars").css("color", "black");
    //                 $(".actives").css("background-color", "darkgray");
    //                 $(".actives").css("color", "black");

    //             });
    //             $(".actives").hover(function () {
    //                 $(this).css("color", "black");
    //             });
    //         }
    //     }
    // });

});
