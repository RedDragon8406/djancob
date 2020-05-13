$(document).ready(function () {
    $("#ls").click(function () {
        $(".hi").slideToggle();
        $("#ls").toggleClass("fa-ellipsis-v");
        $(".itms").toggleClass("list-click");
        $(".cont2").toggleClass("list-click");

    });
    $(window).scroll(function () {
        var width = screen.width;
        var scroll = $(window).scrollTop();
        if (width >= 1200) {
            if (scroll > 575) {
                $(".navbars").css("background-color", "rgb(255, 79, 79)");
                $(".navbars").css("color", "white");
                $(".actives").css("background-color", "white");
                $(".actives").css("color", "black");
                $(".navbars").hover(function () {
                    $(this).css("background-color", "rgb(255, 79, 79)");
                    $(this).css("color", "white");
                    $(".actives").css("background-color", "white");
                });
            }
            else {
                $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                $(".navbars").css("color", "black");
                $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                $(".actives").css("color", "black");
                $(".navbars").hover(function () {
                    $(this).css("background-color", "rgb(255, 79, 79)");
                    $(this).css("color", "white");
                    $(".actives").css("background-color", "white");
                }, function () {
                    $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                    $(".navbars").css("color", "black");
                    $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                    $(".actives").css("color", "black");

                });
                $(".actives").hover(function () {
                    $(this).css("color", "black");
                });
            }
        }
        else {
            if (width > 800) {
                if (width <= 1000) {
                    if (scroll > 650) {
                        $(".navbars").css("background-color", "rgb(255, 79, 79)");
                        $(".navbars").css("color", "white");
                        $(".actives").css("background-color", "white");
                        $(".actives").css("color", "black");
                        $(".navbars").hover(function () {
                            $(this).css("background-color", "rgb(255, 79, 79)");
                            $(this).css("color", "white");
                            $(".actives").css("background-color", "white");
                        });
                    }
                    else {
                        $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                        $(".navbars").css("color", "black");
                        $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                        $(".actives").css("color", "black");
                        $(".navbars").hover(function () {
                            $(this).css("background-color", "rgb(255, 79, 79)");
                            $(this).css("color", "white");
                            $(".actives").css("background-color", "white");
                        }, function () {
                            $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                            $(".navbars").css("color", "black");
                            $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                            $(".actives").css("color", "black");

                        });
                        $(".actives").hover(function () {
                            $(this).css("color", "black");
                        });
                    }
                }
            }
        }
        if (width > 600) {
            if (width <= 800) {
                if (scroll > 650) {
                    $(".navbars").css("background-color", "rgb(255, 79, 79)");
                    $(".navbars").css("color", "white");
                    $(".actives").css("background-color", "white");
                    $(".actives").css("color", "black");
                    $(".navbars").hover(function () {
                        $(this).css("background-color", "rgb(255, 79, 79)");
                        $(this).css("color", "white");
                        $(".actives").css("background-color", "white");
                    });
                }
                else {
                    $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                    $(".navbars").css("color", "black");
                    $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                    $(".actives").css("color", "black");
                    $(".navbars").hover(function () {
                        $(this).css("background-color", "rgb(255, 79, 79)");
                        $(this).css("color", "white");
                        $(".actives").css("background-color", "white");
                    }, function () {
                        $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                        $(".navbars").css("color", "black");
                        $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                        $(".actives").css("color", "black");

                    });
                    $(".actives").hover(function () {
                        $(this).css("color", "black");
                    });
                }
            }
        }
        if (width <= 600) {
            if (scroll > 800) {
                $(".navbars").css("background-color", "rgb(255, 79, 79)");
                $(".navbars").css("color", "white");
                $(".actives").css("background-color", "white");
                $(".actives").css("color", "black");
                $(".navbars").hover(function () {
                    $(this).css("background-color", "rgb(255, 79, 79)");
                    $(this).css("color", "white");
                    $(".actives").css("background-color", "white");
                });
            }
            else {
                $(".navbars").css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                $(".navbars").css("color", "black");
                $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                $(".actives").css("color", "black");
                $(".navbars").hover(function () {
                    $(this).css("background-color", "rgb(255, 79, 79)");
                    $(this).css("color", "white");
                    $(".actives").css("background-color", "white");
                }, function () {
                    $(this).css("background-color", "rgba(255 , 255 , 255 , 0.4)");
                    $(".navbars").css("color", "black");
                    $(".actives").css("background-color", "rgba(255 , 255 , 255 ,0)");
                    $(".actives").css("color", "black");

                });
                $(".actives").hover(function () {
                    $(this).css("color", "black");
                });
            }
        }
    });

});
