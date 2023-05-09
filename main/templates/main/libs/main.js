{% load static %}

$(function () {

    $('.event__btn__block').slick({
        arrows: false,
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2500,
        speed: 1400,
        variableWidth: true,
        leftMode: true,
    });

    $('.vacancy__slider').slick({
        arrows: false,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: false,
        speed: 1400,
        leftMode: true,
    });

    $("#tabs").tabs();

    $(".desc__info__1").hide();
    $(".desc__info__2").hide();
    $(".desc__info__3").hide();
    
    $(".info__btn__1").click(function () {
        $(".events__description__1").hide();

        $(".desc__info__1").fadeIn(1000);
    });
    $(".event__description__info__back__1").click(function () {
        $(".desc__info__1").hide();

        $(".events__description__1").fadeIn(1000);
    });

    $(".info__btn__2").click(function () {
        $(".events__description__2").hide();

        $(".desc__info__2").fadeIn(1000);
    });
    $(".event__description__info__back__2").click(function () {
        $(".desc__info__2").hide();

        $(".events__description__2").fadeIn(1000);
    });

    $(".info__btn__3").click(function () {
        $(".events__description__3").hide();

        $(".desc__info__3").fadeIn(1000);
    });
    $(".event__description__info__back__3").click(function () {
        $(".desc__info__3").hide();

        $(".events__description__3").fadeIn(1000);
    });

    // $(".btn__buy").click(function () {
    //     var pageX = 0;
    //     var pageY = 2652;
    //     window.scrollTo(pageX,pageY);
    // });

    $(".block-1").fadeOut(1);
    $(".block-2").fadeOut(1);
    $(".block-3").fadeOut(1);
    $(".block-4").fadeOut(1);
    $(".block-5").fadeOut(1);
    $(".block-6").fadeOut(1);
    $(".btn__back").fadeOut(1);

    $(".msg__btn__1").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-1").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__2").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-2").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__3").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-3").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__4").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-4").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__5").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-5").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__6").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-6").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__back").click(function () {
        $(".block-1").fadeOut(1);
        $(".block-2").fadeOut(1);
        $(".block-3").fadeOut(1);
        $(".block-4").fadeOut(1);
        $(".block-5").fadeOut(1);
        $(".block-6").fadeOut(1);
        $(".msg__btn__back").fadeOut(1);

        $(".msg__btn__1").fadeIn(100);
        $(".msg__btn__2").fadeIn(100);
        $(".msg__btn__3").fadeIn(100);
        $(".msg__btn__4").fadeIn(100);
        $(".msg__btn__5").fadeIn(100);
        $(".msg__btn__6").fadeIn(100);
    });

    $(".advantages__icon__text__1").hide();
    $(".advantages__icon__text__2").hide();
    $(".advantages__icon__text__3").hide();
    $(".advantages__icon__text__4").hide();

    $(document).ready(function () {
        $(".advantages__icon__1").hover(function () {
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__1").show(800);
        },
            function () {
                $(".advantages__icon__text__1").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__2").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__2").show(800);
        },
            function () {
                $(".advantages__icon__text__2").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__3").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__3").show(800);
        },
            function () {
                $(".advantages__icon__text__3").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__4").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").show(800);
        },
            function () {
                $(".advantages__icon__text__4").hide();
            });
    });

});